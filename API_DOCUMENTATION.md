# SEO Automation Suite - API Documentation

## Overview

The SEO Automation Suite API provides comprehensive tools for SEO agencies to automate and optimize their workflows. This RESTful API uses JWT authentication and supports various SEO operations including meta tag generation, broken link detection, competitor analysis, and SERP tracking.

**Base URL**: `http://localhost:8000` (development)  
**API Version**: 1.0.0

## Interactive Documentation

Once the server is running, you can access:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

## Authentication

Most endpoints require JWT Bearer token authentication.

### Getting Started

1. **Register** a new account
2. **Login** to receive an access token
3. Include the token in subsequent requests

### Authentication Header Format

```
Authorization: Bearer <your_jwt_token>
```

---

## API Endpoints

### 🔐 Authentication (`/auth`)

#### POST `/auth/register`
Register a new user account.

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "securePassword123",
  "name": "John Doe"
}
```

**Response (200):**
```json
{
  "user_id": "uuid-string",
  "email": "user@example.com",
  "role": "manager"
}
```

**Errors:**
- `400`: Email already registered

---

#### POST `/auth/login`
Authenticate and receive JWT token.

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "securePassword123"
}
```

**Response (200):**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "Bearer",
  "expires_in": 3600
}
```

**Errors:**
- `401`: Invalid credentials

---

#### GET `/auth/me`
Get current authenticated user's profile.

**Headers:** `Authorization: Bearer <token>`

**Response (200):**
```json
{
  "user_id": "uuid-string",
  "email": "user@example.com",
  "role": "manager",
  "created_at": "2024-01-15T10:30:00"
}
```

---

#### POST `/auth/logout`
Logout current user.

**Response (200):**
```json
{
  "message": "Logged out successfully"
}
```

---

#### POST `/auth/forgot-password`
Request password reset email.

**Request Body:**
```json
{
  "email": "user@example.com"
}
```

**Response (200):**
```json
{
  "message": "Password reset email sent"
}
```

---

#### POST `/auth/reset-password`
Reset user password.

**Response (200):**
```json
{
  "message": "Password reset successful"
}
```

---

### 📁 Projects (`/projects`)

#### POST `/projects`
Create a new SEO project.

**Headers:** `Authorization: Bearer <token>`

**Request Body:**
```json
{
  "name": "My Website SEO",
  "domain": "example.com"
}
```

**Response (200):**
```json
{
  "project_id": "uuid-string",
  "name": "My Website SEO",
  "domain": "example.com",
  "created_at": "2024-01-15T10:30:00"
}
```

---

#### GET `/projects`
List all projects for authenticated user.

**Headers:** `Authorization: Bearer <token>`

**Response (200):**
```json
[
  {
    "project_id": "uuid-string",
    "name": "My Website SEO",
    "domain": "example.com",
    "created_at": "2024-01-15T10:30:00"
  }
]
```

---

#### GET `/projects/{project_id}`
Get specific project details.

**Headers:** `Authorization: Bearer <token>`

**Response (200):**
```json
{
  "project_id": "uuid-string",
  "name": "My Website SEO",
  "domain": "example.com",
  "created_at": "2024-01-15T10:30:00"
}
```

**Errors:**
- `404`: Project not found

---

#### PUT `/projects/{project_id}`
Update project details.

**Headers:** `Authorization: Bearer <token>`

**Request Body:**
```json
{
  "name": "Updated Project Name",
  "domain": "newdomain.com"
}
```

**Response (200):**
```json
{
  "message": "Project updated successfully"
}
```

---

#### DELETE `/projects/{project_id}`
Delete a project.

**Headers:** `Authorization: Bearer <token>`

**Response (200):**
```json
{
  "message": "Project deleted successfully"
}
```

---

#### POST `/projects/{project_id}/invite`
Invite team member to project.

**Headers:** `Authorization: Bearer <token>`

**Response (200):**
```json
{
  "message": "Invitation sent"
}
```

---

### 🏷️ Meta Tags (`/meta`)

#### POST `/meta/generate`
Generate AI-powered meta tags using Google Gemini.

**Headers:** `Authorization: Bearer <token>`

**Request Body:**
```json
{
  "project_id": "uuid-string",
  "url": "https://example.com/page",
  "content": "Optional page content text"
}
```

**Response (200):**
```json
{
  "message": "Meta tag generation started",
  "status": "processing"
}
```

**Note:** This is an asynchronous operation. The meta tags are generated in the background.

---

#### GET `/meta/{project_id}`
Get all meta tags for a project.

**Headers:** `Authorization: Bearer <token>`

**Response (200):**
```json
{
  "meta_tags": [
    {
      "id": "uuid-string",
      "url": "https://example.com/page",
      "title": "Generated Title",
      "description": "Generated description",
      "keywords": ["keyword1", "keyword2"]
    }
  ]
}
```

---

#### GET `/meta/{project_id}/{meta_id}`
Get specific meta tag details.

**Headers:** `Authorization: Bearer <token>`

**Response (200):**
```json
{
  "id": "uuid-string",
  "url": "https://example.com/page",
  "title": "Generated Title",
  "description": "Generated description",
  "keywords": ["keyword1", "keyword2"],
  "created_at": "2024-01-15T10:30:00"
}
```

**Errors:**
- `404`: Meta tag not found

---

#### DELETE `/meta/{project_id}/{meta_id}`
Delete a meta tag.

**Headers:** `Authorization: Bearer <token>`

**Response (200):**
```json
{
  "message": "Meta tag deleted successfully"
}
```

---

### 🔗 Broken Links (`/links`)

#### POST `/links/scan`
Start scanning for broken links on a domain.

**Headers:** `Authorization: Bearer <token>`

**Request Body:**
```json
{
  "project_id": "uuid-string",
  "domain": "example.com"
}
```

**Response (200):**
```json
{
  "scan_id": "uuid-string",
  "status": "queued"
}
```

**Note:** This is an asynchronous operation using Apify.

---

#### GET `/links/scan/{scan_id}`
Get scan status and progress.

**Headers:** `Authorization: Bearer <token>`

**Response (200):**
```json
{
  "scan_id": "uuid-string",
  "status": "completed",
  "progress": 100
}
```

**Status values:** `queued`, `processing`, `completed`, `failed`

---

#### GET `/links/{project_id}`
Get all broken links for a project.

**Headers:** `Authorization: Bearer <token>`

**Response (200):**
```json
{
  "project_id": "uuid-string",
  "broken_links": [
    {
      "source_url": "https://example.com/page1",
      "broken_url": "https://example.com/missing",
      "status_code": 404
    }
  ]
}
```

---

#### GET `/links/{project_id}/export`
Export broken links to CSV.

**Headers:** `Authorization: Bearer <token>`

**Response (200):**
```json
{
  "message": "Export functionality",
  "format": "csv"
}
```

---

### 🎯 Competitor Analysis (`/competitor`)

#### POST `/competitor/analyze`
Analyze competitor content and identify gaps.

**Headers:** `Authorization: Bearer <token>`

**Request Body:**
```json
{
  "project_id": "uuid-string",
  "competitor_urls": [
    "https://competitor1.com",
    "https://competitor2.com"
  ],
  "target_url": "https://mysite.com"
}
```

**Response (200):**
```json
{
  "message": "Competitor analysis started",
  "status": "processing"
}
```

**Note:** This is an asynchronous operation using AI clustering.

---

#### GET `/competitor/{project_id}`
Get all competitor analyses for a project.

**Headers:** `Authorization: Bearer <token>`

**Response (200):**
```json
{
  "analyses": [
    {
      "id": "uuid-string",
      "competitor_url": "https://competitor.com",
      "similarity_score": 0.85,
      "analyzed_at": "2024-01-15T10:30:00"
    }
  ]
}
```

---

#### GET `/competitor/report/{analysis_id}`
Get detailed analysis report.

**Headers:** `Authorization: Bearer <token>`

**Response (200):**
```json
{
  "analysis_id": "uuid-string",
  "similarity_score": 0.85,
  "keyword_gap": ["keyword1", "keyword2"],
  "topic_clusters": [
    {
      "cluster": "Technology",
      "keywords": ["AI", "ML", "automation"]
    }
  ]
}
```

**Errors:**
- `404`: Analysis not found

---

#### DELETE `/competitor/report/{analysis_id}`
Delete an analysis report.

**Headers:** `Authorization: Bearer <token>`

**Response (200):**
```json
{
  "message": "Analysis deleted successfully"
}
```

---

### 📊 SERP Comparator (`/serp`)

#### POST `/serp/compare`
Compare search engine rankings for keywords.

**Headers:** `Authorization: Bearer <token>`

**Request Body:**
```json
{
  "project_id": "uuid-string",
  "keywords": ["seo tools", "keyword research"],
  "location": "United States"
}
```

**Response (200):**
```json
{
  "comparison_id": "uuid-string",
  "status": "processing"
}
```

**Note:** This is an asynchronous operation using Apify SERP scraper.

---

#### GET `/serp/{project_id}`
Get all SERP data for a project.

**Headers:** `Authorization: Bearer <token>`

**Response (200):**
```json
{
  "serp_data": [
    {
      "keyword": "seo tools",
      "position": 5,
      "url": "https://mysite.com",
      "detected_at": "2024-01-15T10:30:00"
    }
  ]
}
```

---

#### GET `/serp/history/{keyword}`
Get ranking history for a specific keyword.

**Headers:** `Authorization: Bearer <token>`

**Response (200):**
```json
{
  "keyword": "seo tools",
  "history": [
    {
      "position": 5,
      "url": "https://mysite.com",
      "detected_at": "2024-01-15T10:30:00"
    },
    {
      "position": 7,
      "url": "https://mysite.com",
      "detected_at": "2024-01-14T10:30:00"
    }
  ]
}
```

---

#### GET `/serp/compare/{comparison_id}`
Get comparison results.

**Headers:** `Authorization: Bearer <token>`

**Response (200):**
```json
{
  "comparison_id": "uuid-string",
  "status": "completed"
}
```

---

#### DELETE `/serp/{comparison_id}`
Delete a comparison.

**Headers:** `Authorization: Bearer <token>`

**Response (200):**
```json
{
  "message": "Comparison deleted successfully"
}
```

---

## Error Responses

All endpoints may return the following error responses:

### 400 Bad Request
```json
{
  "detail": "Error message describing what went wrong"
}
```

### 401 Unauthorized
```json
{
  "detail": "Not authenticated"
}
```

### 403 Forbidden
```json
{
  "detail": "Not enough permissions"
}
```

### 404 Not Found
```json
{
  "detail": "Resource not found"
}
```

### 422 Validation Error
```json
{
  "detail": [
    {
      "loc": ["body", "field_name"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

### 500 Internal Server Error
```json
{
  "detail": "Internal server error"
}
```

---

## Rate Limiting

API requests are rate-limited to ensure system stability:

- **Authenticated requests**: 100 requests per minute
- **Unauthenticated requests**: 20 requests per minute

Rate limit headers are included in responses:
```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1642248000
```

---

## Webhooks

Configure webhooks to receive notifications for asynchronous operations:

- Meta tag generation completed
- Link scan completed
- Competitor analysis completed
- SERP comparison completed

Webhook configuration coming soon.

---

## SDKs and Client Libraries

Official client libraries:

- **Python**: Coming soon
- **JavaScript/TypeScript**: Coming soon
- **PHP**: Coming soon

---

## Support and Resources

- **GitHub**: [Repository URL]
- **Documentation**: http://localhost:8000/docs
- **Support Email**: support@example.com

---

## Changelog

### Version 1.0.0 (Current)
- Initial API release
- Authentication system
- Project management
- Meta tag generation with Gemini AI
- Broken link detection with Apify
- Competitor analysis with NLP
- SERP tracking and comparison

---

## Testing the API

### Using cURL

**Register:**
```bash
curl -X POST "http://localhost:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"test123","name":"Test User"}'
```

**Login:**
```bash
curl -X POST "http://localhost:8000/auth/login" \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"test123"}'
```

**Create Project:**
```bash
curl -X POST "http://localhost:8000/projects" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"name":"Test Project","domain":"example.com"}'
```

### Using Python

```python
import requests

# Login
response = requests.post(
    "http://localhost:8000/auth/login",
    json={"email": "test@example.com", "password": "test123"}
)
token = response.json()["access_token"]

# Create project
headers = {"Authorization": f"Bearer {token}"}
response = requests.post(
    "http://localhost:8000/projects",
    headers=headers,
    json={"name": "Test Project", "domain": "example.com"}
)
print(response.json())
```

### Using JavaScript

```javascript
// Login
const loginResponse = await fetch('http://localhost:8000/auth/login', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    email: 'test@example.com',
    password: 'test123'
  })
});
const { access_token } = await loginResponse.json();

// Create project
const projectResponse = await fetch('http://localhost:8000/projects', {
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${access_token}`,
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    name: 'Test Project',
    domain: 'example.com'
  })
});
const project = await projectResponse.json();
console.log(project);
```

---

## Best Practices

1. **Always use HTTPS** in production
2. **Store tokens securely** - never commit them to version control
3. **Handle token expiration** - implement token refresh logic
4. **Use appropriate HTTP methods** - GET for reading, POST for creating, PUT for updating, DELETE for removing
5. **Validate input** on the client side before sending requests
6. **Handle errors gracefully** - check status codes and error messages
7. **Implement retry logic** for failed requests with exponential backoff
8. **Monitor rate limits** to avoid being throttled

---

*Last updated: November 12, 2025*
