# Swagger/OpenAPI Setup Guide

## Overview

Your FastAPI application now has comprehensive Swagger/OpenAPI documentation automatically generated and enhanced with detailed descriptions, examples, and interactive testing capabilities.

## What's Been Added

### 1. Enhanced FastAPI Configuration (`app/main.py`)

- Detailed API description with markdown formatting
- Contact information
- License details
- Custom documentation URLs
- Comprehensive feature overview

### 2. Endpoint Documentation

All API endpoints now include:
- **Summary**: Brief description of what the endpoint does
- **Description**: Detailed explanation
- **Docstrings**: Additional context and parameter details
- **Response models**: Structured response schemas
- **Example requests**: Sample JSON payloads in Pydantic models

### 3. Request/Response Examples

All Pydantic models now include example data using `Config.json_schema_extra`:
- Authentication requests (register, login)
- Project creation
- Meta tag generation
- Link scanning
- Competitor analysis
- SERP comparison

### 4. Documentation Files

Created comprehensive documentation:
- **API_DOCUMENTATION.md**: Complete API reference with all endpoints, examples, and error codes
- **API_QUICKSTART.md**: Step-by-step guide to get started in 5 minutes
- **postman_collection.json**: Ready-to-import Postman collection for testing
- **SWAGGER_SETUP.md**: This file

## Accessing the Documentation

### Swagger UI (Interactive)
```
http://localhost:8000/docs
```

Features:
- Try out API calls directly from the browser
- See request/response schemas
- Authenticate with JWT tokens
- View all available endpoints organized by tags

### ReDoc (Alternative View)
```
http://localhost:8000/redoc
```

Features:
- Clean, readable documentation
- Better for reading and understanding
- Organized by tags
- Search functionality

### OpenAPI JSON Schema
```
http://localhost:8000/openapi.json
```

Use this to:
- Generate client SDKs
- Import into API testing tools
- Integrate with API gateways
- Share with frontend developers

## Using Swagger UI

### Step 1: Start the Server

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Step 2: Open Swagger UI

Navigate to http://localhost:8000/docs in your browser.

### Step 3: Authenticate

1. Click the **"Authorize"** button at the top right
2. First, register a user:
   - Find `POST /auth/register`
   - Click "Try it out"
   - Fill in the example data
   - Click "Execute"
3. Then login:
   - Find `POST /auth/login`
   - Click "Try it out"
   - Use the same credentials
   - Click "Execute"
   - Copy the `access_token` from the response
4. Click **"Authorize"** again
5. Enter: `Bearer <your_access_token>`
6. Click "Authorize" and "Close"

### Step 4: Test Endpoints

Now you can test any protected endpoint:
1. Find the endpoint you want to test
2. Click "Try it out"
3. Modify the request body if needed
4. Click "Execute"
5. View the response

## Features of the Documentation

### 1. Organized by Tags

Endpoints are grouped into logical sections:
- 🔐 Authentication
- 📁 Projects
- 🏷️ Meta Tags
- 🔗 Broken Links
- 🎯 Competitor Analysis
- 📊 SERP Comparator

### 2. Request Examples

Every endpoint shows example request bodies:

```json
{
  "email": "user@example.com",
  "password": "securePassword123",
  "name": "John Doe"
}
```

### 3. Response Schemas

Clear response structures with field types and descriptions.

### 4. Error Responses

Common HTTP status codes documented:
- 200: Success
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found
- 422: Validation Error
- 500: Internal Server Error

### 5. Authentication Flow

Visual indication of which endpoints require authentication with a lock icon 🔒.

## Importing into Postman

### Option 1: Import OpenAPI JSON

1. Open Postman
2. Click "Import"
3. Select "Link"
4. Enter: `http://localhost:8000/openapi.json`
5. Click "Continue" and "Import"

### Option 2: Import Collection File

1. Open Postman
2. Click "Import"
3. Select "File"
4. Choose `postman_collection.json`
5. Click "Import"

The collection includes:
- All endpoints organized by feature
- Environment variables for base URL and tokens
- Auto-save of access token after login
- Auto-save of project ID after creation

## Generating Client SDKs

Use the OpenAPI schema to generate client libraries:

### Python Client
```bash
openapi-generator-cli generate \
  -i http://localhost:8000/openapi.json \
  -g python \
  -o ./client-python
```

### TypeScript/JavaScript Client
```bash
openapi-generator-cli generate \
  -i http://localhost:8000/openapi.json \
  -g typescript-axios \
  -o ./client-typescript
```

### Other Languages
OpenAPI Generator supports 50+ languages including:
- Java
- C#
- Go
- Ruby
- PHP
- Swift
- Kotlin

## Customizing Documentation

### Adding More Details to Endpoints

Edit the router files and add more information:

```python
@router.post("/endpoint",
    summary="Short description",
    description="Longer description with details",
    response_description="What the response contains",
    tags=["Custom Tag"],
    status_code=201
)
async def my_endpoint():
    """
    Even more detailed documentation in docstring.
    
    - **param1**: Description of parameter 1
    - **param2**: Description of parameter 2
    """
    pass
```

### Adding Examples to Models

```python
class MyModel(BaseModel):
    field1: str
    field2: int
    
    class Config:
        json_schema_extra = {
            "example": {
                "field1": "example value",
                "field2": 42
            }
        }
```

### Customizing Main App Description

Edit `app/main.py` and modify the `description` parameter in the `FastAPI()` constructor.

## Best Practices

1. **Keep descriptions concise** - Use summary for one-liners, description for details
2. **Provide examples** - Always include example request/response data
3. **Document errors** - List possible error responses
4. **Use tags** - Group related endpoints together
5. **Version your API** - Update version number when making breaking changes
6. **Add deprecation warnings** - Mark old endpoints as deprecated before removing

## Security Considerations

### In Production

1. **Disable docs in production** (optional):
```python
app = FastAPI(
    docs_url=None if settings.ENVIRONMENT == "production" else "/docs",
    redoc_url=None if settings.ENVIRONMENT == "production" else "/redoc"
)
```

2. **Protect docs with authentication**:
```python
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBasic

security = HTTPBasic()

def verify_docs_access(credentials = Depends(security)):
    if credentials.username != "admin" or credentials.password != "secret":
        raise HTTPException(status_code=401)
    return credentials

app = FastAPI(
    docs_url="/docs",
    dependencies=[Depends(verify_docs_access)]
)
```

3. **Use HTTPS** - Always serve docs over HTTPS in production

## Troubleshooting

### Docs Not Loading

1. Check server is running: `curl http://localhost:8000/health`
2. Verify docs URL: http://localhost:8000/docs
3. Check browser console for errors
4. Clear browser cache

### Authentication Not Working

1. Make sure you're using the correct format: `Bearer <token>`
2. Check token hasn't expired
3. Verify token is copied completely
4. Try logging in again

### Examples Not Showing

1. Verify `Config.json_schema_extra` is properly formatted
2. Check for JSON syntax errors
3. Restart the server

## Additional Resources

- **FastAPI Documentation**: https://fastapi.tiangolo.com/
- **OpenAPI Specification**: https://swagger.io/specification/
- **Swagger UI**: https://swagger.io/tools/swagger-ui/
- **ReDoc**: https://github.com/Redocly/redoc
- **OpenAPI Generator**: https://openapi-generator.tech/

## Support

For issues or questions:
- Check the [API_DOCUMENTATION.md](API_DOCUMENTATION.md)
- Review [API_QUICKSTART.md](API_QUICKSTART.md)
- Test with Postman collection
- Check server logs

---

Your API is now fully documented and ready for development! 🚀
