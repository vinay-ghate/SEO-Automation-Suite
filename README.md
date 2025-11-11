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
📖 See [docs/ENVIRONMENT_SETUP.md](docs/ENVIRONMENT_SETUP.md) for detailed configuration guide

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
- See [docs/SECURITY.md](docs/SECURITY.md) for security best practices
- See [docs/ENVIRONMENT_SETUP.md](docs/ENVIRONMENT_SETUP.md) for configuration guide

## API Documentation

Comprehensive API documentation is available:

- **Interactive Swagger UI**: http://localhost:8000/docs
- **ReDoc Documentation**: http://localhost:8000/redoc
- **Full API Guide**: [docs/API_DOCUMENTATION.md](docs/API_DOCUMENTATION.md)
- **Quick Start Guide**: [docs/API_QUICKSTART.md](docs/API_QUICKSTART.md)
- **Postman Collection**: [postman_collection.json](postman_collection.json)

### Quick Start

1. Register and login to get an access token
2. Create a project
3. Use the token in Authorization header: `Bearer <token>`
4. Explore endpoints in Swagger UI

See [docs/API_QUICKSTART.md](docs/API_QUICKSTART.md) for detailed examples.

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

- **Quick Start**: [docs/QUICK_DEPLOY.md](docs/QUICK_DEPLOY.md) - Deploy in 3 commands
- **Full Guide**: [docs/DEPLOYMENT_GUIDE.md](docs/DEPLOYMENT_GUIDE.md) - Comprehensive deployment instructions
- **Checklist**: [docs/DEPLOYMENT_CHECKLIST.md](docs/DEPLOYMENT_CHECKLIST.md) - Pre/post deployment checklist

### Supported Platforms

- ✅ VPS (DigitalOcean, Linode, Vultr, AWS EC2)
- ✅ Docker / Docker Compose
- ✅ Google Cloud Run
- ✅ AWS ECS
- ✅ Heroku
- ✅ Railway

## 📚 Documentation

**All documentation is in the [docs/](docs/) directory.**

### Quick Links

- 🚀 **[Deploy Now](docs/DEPLOY_NOW.md)** - Copy-paste deployment commands
- 📖 **[Documentation Index](docs/README.md)** - Complete documentation guide
- 🔌 **[API Documentation](docs/API_DOCUMENTATION.md)** - Complete API reference
- ⚡ **[API Quick Start](docs/API_QUICKSTART.md)** - Get started in 5 minutes
- ⚙️ **[Environment Setup](docs/ENVIRONMENT_SETUP.md)** - Configuration guide
- 🔒 **[Security Guide](docs/SECURITY.md)** - Security best practices
- 🚀 **[Deployment Guide](docs/DEPLOYMENT_GUIDE.md)** - Server deployment
- ✅ **[Quick Deploy](docs/QUICK_DEPLOY.md)** - Fast deployment guide

**Browse all documentation**: [docs/README.md](docs/README.md)

## License

MIT
