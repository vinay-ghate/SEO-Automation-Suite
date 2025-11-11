from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, projects, meta, links, competitor, serp
from app.config import settings

app = FastAPI(
    title="SEO Automation Suite API",
    description="""
## AI-Powered SEO Tools for Agencies

This API provides comprehensive SEO automation tools including:

* **Authentication** - User registration, login, and JWT-based authentication
* **Project Management** - Create and manage SEO projects
* **Meta Tag Generation** - AI-powered meta tag generation using Gemini
* **Broken Link Detection** - Scan and identify broken links on websites
* **Competitor Analysis** - Analyze competitor content and identify gaps
* **SERP Comparison** - Track and compare search engine rankings

### Authentication

Most endpoints require authentication using JWT Bearer tokens. 
1. Register a new account at `/auth/register`
2. Login at `/auth/login` to receive an access token
3. Include the token in the Authorization header: `Bearer <token>`

### Rate Limits

API requests are rate-limited to ensure fair usage and system stability.

### Support

For issues or questions, contact your system administrator.
    """,
    version="1.0.0",
    contact={
        "name": "API Support",
        "email": "support@example.com",
    },
    license_info={
        "name": "Proprietary",
    },
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(projects.router, prefix="/projects", tags=["Projects"])
app.include_router(meta.router, prefix="/meta", tags=["Meta Tags"])
app.include_router(links.router, prefix="/links", tags=["Broken Links"])
app.include_router(competitor.router, prefix="/competitor", tags=["Competitor Analysis"])
app.include_router(serp.router, prefix="/serp", tags=["SERP Comparator"])

@app.get("/")
async def root():
    return {"message": "SEO Automation Suite API", "version": "1.0.0"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
