# SEO Automation Suite for Agencies

AI-powered SEO tools suite with meta tag generation, broken link detection, competitor analysis, and SERP tracking.

## Features

- **Meta Tag Generator**: AI-optimized meta tags with CTR scoring
- **Broken Link Finder**: Automated link checking and redirect detection
- **Competitor NLP Analyzer**: Semantic similarity and keyword gap analysis
- **SERP Comparator**: Keyword ranking tracking and comparison
- **Task Scheduler**: Automated recurring scans and reports
- **Multi-user Support**: Role-based access control

## Tech Stack

- FastAPI
- PostgreSQL
- Celery + Redis
- Google Gemini AI
- Apify Web Scraping
- SQLAlchemy ORM

## Installation

### Quick Start

1. **Clone the repository**
```bash
git clone <repository-url>
cd seo-automation-suite
```

2. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env with your actual credentials
```
📖 See [ENVIRONMENT_SETUP.md](ENVIRONMENT_SETUP.md) for detailed configuration guide

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run with Docker**
```bash
docker-compose up -d
```

5. **Access the application**
- API: http://localhost:8000
- Interactive API docs: http://localhost:8000/docs

### Important Security Notes

⚠️ **Never commit your `.env` file!** It contains sensitive credentials.

- All API keys must be in `.env` file
- See [SECURITY.md](SECURITY.md) for security best practices
- See [ENVIRONMENT_SETUP.md](ENVIRONMENT_SETUP.md) for configuration guide

## API Documentation

Comprehensive API documentation is available:

- **Interactive Swagger UI**: http://localhost:8000/docs
- **ReDoc Documentation**: http://localhost:8000/redoc
- **Full API Guide**: [API_DOCUMENTATION.md](API_DOCUMENTATION.md)
- **Quick Start Guide**: [API_QUICKSTART.md](API_QUICKSTART.md)
- **Postman Collection**: [postman_collection.json](postman_collection.json)

### Quick Start

1. Register and login to get an access token
2. Create a project
3. Use the token in Authorization header: `Bearer <token>`
4. Explore endpoints in Swagger UI

See [API_QUICKSTART.md](API_QUICKSTART.md) for detailed examples.

## API Endpoints

### Authentication
- POST /auth/register
- POST /auth/login
- GET /auth/me

### Projects
- POST /projects
- GET /projects
- GET /projects/{project_id}

### Meta Tags
- POST /meta/generate
- GET /meta/{project_id}

### Broken Links
- POST /links/scan
- GET /links/{project_id}

### Competitor Analysis
- POST /competitor/analyze
- GET /competitor/{project_id}

### SERP Tracking
- POST /serp/compare
- GET /serp/{project_id}

## Development

Run locally:
```bash
uvicorn app.main:app --reload
```

Run Celery worker:
```bash
celery -A app.workers.celery_app worker --loglevel=info
```

## 🚀 Deployment

### Quick Deploy to Server

```bash
# 1. Setup server (one-time)
curl -fsSL https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/setup-server.sh | bash

# 2. Configure environment
cd ~/seo-automation-suite
nano .env

# 3. Deploy
./deploy.sh
```

**Done!** Access at `http://your-server-ip:8000`

### Deployment Guides

- **Quick Start**: [QUICK_DEPLOY.md](QUICK_DEPLOY.md) - Deploy in 3 commands
- **Full Guide**: [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) - Comprehensive deployment instructions
- **Checklist**: [DEPLOYMENT_CHECKLIST.md](DEPLOYMENT_CHECKLIST.md) - Pre/post deployment checklist

### Supported Platforms

- ✅ VPS (DigitalOcean, Linode, Vultr, AWS EC2)
- ✅ Docker / Docker Compose
- ✅ Google Cloud Run
- ✅ AWS ECS
- ✅ Heroku
- ✅ Railway

## 📚 Documentation

- [API Documentation](API_DOCUMENTATION.md) - Complete API reference
- [API Quick Start](API_QUICKSTART.md) - Get started in 5 minutes
- [Environment Setup](ENVIRONMENT_SETUP.md) - Configuration guide
- [Security Guide](SECURITY.md) - Security best practices
- [Deployment Guide](DEPLOYMENT_GUIDE.md) - Server deployment
- [Quick Deploy](QUICK_DEPLOY.md) - Fast deployment guide

## License

MIT
