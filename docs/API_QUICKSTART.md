# API Quick Start Guide

## Getting Started in 5 Minutes

This guide will help you get up and running with the SEO Automation Suite API quickly.

## Prerequisites

- Python 3.9+
- PostgreSQL database
- Redis (for Celery tasks)
- API keys for Gemini and Apify

## 1. Start the Server

```bash
# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your configuration

# Run database migrations
alembic upgrade head

# Start the FastAPI server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The server will start at `http://localhost:8000`

## 2. Access Interactive Documentation

Open your browser and navigate to:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

The Swagger UI provides an interactive interface where you can:
- View all available endpoints
- See request/response schemas
- Test API calls directly from the browser
- Authenticate and try protected endpoints

## 3. Register and Login

### Step 1: Register a New Account

**Using Swagger UI:**
1. Go to http://localhost:8000/docs
2. Find `POST /auth/register`
3. Click "Try it out"
4. Enter your details:
```json
{
  "email": "your@email.com",
  "password": "yourPassword123",
  "name": "Your Name"
}
```
5. Click "Execute"

**Using cURL:**
```bash
curl -X POST "http://localhost:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "your@email.com",
    "password": "yourPassword123",
    "name": "Your Name"
  }'
```

### Step 2: Login to Get Access Token

**Using Swagger UI:**
1. Find `POST /auth/login`
2. Click "Try it out"
3. Enter credentials:
```json
{
  "email": "your@email.com",
  "password": "yourPassword123"
}
```
4. Click "Execute"
5. Copy the `access_token` from the response

**Using cURL:**
```bash
curl -X POST "http://localhost:8000/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "your@email.com",
    "password": "yourPassword123"
  }'
```

Response:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "Bearer",
  "expires_in": 3600
}
```

### Step 3: Authorize in Swagger UI

1. Click the "Authorize" button at the top of the Swagger UI
2. Enter: `Bearer YOUR_ACCESS_TOKEN`
3. Click "Authorize"
4. Now all protected endpoints will include your token automatically

## 4. Create Your First Project

**Using Swagger UI:**
1. Find `POST /projects`
2. Click "Try it out"
3. Enter project details:
```json
{
  "name": "My First Project",
  "domain": "example.com"
}
```
4. Click "Execute"

**Using cURL:**
```bash
curl -X POST "http://localhost:8000/projects" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "My First Project",
    "domain": "example.com"
  }'
```

Response:
```json
{
  "project_id": "123e4567-e89b-12d3-a456-426614174000",
  "name": "My First Project",
  "domain": "example.com",
  "created_at": "2024-01-15T10:30:00"
}
```

Save the `project_id` for the next steps!

## 5. Try Key Features

### Generate Meta Tags

```bash
curl -X POST "http://localhost:8000/meta/generate" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "project_id": "YOUR_PROJECT_ID",
    "url": "https://example.com/page",
    "content": "Your page content here"
  }'
```

### Scan for Broken Links

```bash
curl -X POST "http://localhost:8000/links/scan" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "project_id": "YOUR_PROJECT_ID",
    "domain": "example.com"
  }'
```

### Analyze Competitors

```bash
curl -X POST "http://localhost:8000/competitor/analyze" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "project_id": "YOUR_PROJECT_ID",
    "competitor_urls": [
      "https://competitor1.com",
      "https://competitor2.com"
    ],
    "target_url": "https://mysite.com"
  }'
```

### Compare SERP Rankings

```bash
curl -X POST "http://localhost:8000/serp/compare" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "project_id": "YOUR_PROJECT_ID",
    "keywords": ["seo tools", "keyword research"],
    "location": "United States"
  }'
```

## 6. Check Results

Most operations are asynchronous. Check results using:

```bash
# Get meta tags
curl -X GET "http://localhost:8000/meta/YOUR_PROJECT_ID" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"

# Get broken links
curl -X GET "http://localhost:8000/links/YOUR_PROJECT_ID" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"

# Get competitor analyses
curl -X GET "http://localhost:8000/competitor/YOUR_PROJECT_ID" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"

# Get SERP data
curl -X GET "http://localhost:8000/serp/YOUR_PROJECT_ID" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## Python Example

Here's a complete Python example:

```python
import requests
import time

BASE_URL = "http://localhost:8000"

# 1. Register
register_response = requests.post(
    f"{BASE_URL}/auth/register",
    json={
        "email": "test@example.com",
        "password": "test123",
        "name": "Test User"
    }
)
print("Registered:", register_response.json())

# 2. Login
login_response = requests.post(
    f"{BASE_URL}/auth/login",
    json={
        "email": "test@example.com",
        "password": "test123"
    }
)
token = login_response.json()["access_token"]
headers = {"Authorization": f"Bearer {token}"}
print("Logged in, token:", token[:20] + "...")

# 3. Create Project
project_response = requests.post(
    f"{BASE_URL}/projects",
    headers=headers,
    json={
        "name": "Test Project",
        "domain": "example.com"
    }
)
project = project_response.json()
project_id = project["project_id"]
print("Created project:", project_id)

# 4. Generate Meta Tags
meta_response = requests.post(
    f"{BASE_URL}/meta/generate",
    headers=headers,
    json={
        "project_id": project_id,
        "url": "https://example.com",
        "content": "Sample content"
    }
)
print("Meta generation started:", meta_response.json())

# 5. Wait and check results
time.sleep(5)  # Wait for processing
meta_results = requests.get(
    f"{BASE_URL}/meta/{project_id}",
    headers=headers
)
print("Meta tags:", meta_results.json())

# 6. Get all projects
projects = requests.get(
    f"{BASE_URL}/projects",
    headers=headers
)
print("All projects:", projects.json())
```

## JavaScript/Node.js Example

```javascript
const BASE_URL = 'http://localhost:8000';

async function main() {
  // 1. Register
  const registerRes = await fetch(`${BASE_URL}/auth/register`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      email: 'test@example.com',
      password: 'test123',
      name: 'Test User'
    })
  });
  console.log('Registered:', await registerRes.json());

  // 2. Login
  const loginRes = await fetch(`${BASE_URL}/auth/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      email: 'test@example.com',
      password: 'test123'
    })
  });
  const { access_token } = await loginRes.json();
  const headers = {
    'Authorization': `Bearer ${access_token}`,
    'Content-Type': 'application/json'
  };
  console.log('Logged in');

  // 3. Create Project
  const projectRes = await fetch(`${BASE_URL}/projects`, {
    method: 'POST',
    headers,
    body: JSON.stringify({
      name: 'Test Project',
      domain: 'example.com'
    })
  });
  const project = await projectRes.json();
  console.log('Created project:', project.project_id);

  // 4. Generate Meta Tags
  const metaRes = await fetch(`${BASE_URL}/meta/generate`, {
    method: 'POST',
    headers,
    body: JSON.stringify({
      project_id: project.project_id,
      url: 'https://example.com',
      content: 'Sample content'
    })
  });
  console.log('Meta generation:', await metaRes.json());

  // 5. Get all projects
  const projectsRes = await fetch(`${BASE_URL}/projects`, { headers });
  console.log('All projects:', await projectsRes.json());
}

main();
```

## Common Issues

### 401 Unauthorized
- Make sure you're including the Bearer token in the Authorization header
- Check if your token has expired (default: 60 minutes)
- Login again to get a fresh token

### 422 Validation Error
- Check that all required fields are provided
- Verify field types match the schema
- Review the error details in the response

### 500 Internal Server Error
- Check server logs for details
- Verify database connection
- Ensure all environment variables are set correctly

## Next Steps

- Read the full [API Documentation](API_DOCUMENTATION.md)
- Explore all endpoints in Swagger UI
- Set up webhooks for async operations
- Integrate with your application

## Support

- Interactive Docs: http://localhost:8000/docs
- Full Documentation: [API_DOCUMENTATION.md](API_DOCUMENTATION.md)
- Issues: Report on GitHub

---

Happy coding! 🚀
