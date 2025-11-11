# 📁 Project Structure

## Overview

```
seo-automation-suite/
├── 📁 app/                      # Application code
│   ├── 📁 routers/              # API endpoints
│   ├── 📁 models/               # Database models
│   ├── 📁 services/             # Business logic
│   ├── 📁 integrations/         # External API clients
│   ├── 📁 workers/              # Celery tasks
│   ├── 📁 nlp/                  # NLP & ML utilities
│   ├── 📁 utils/                # Helper functions
│   ├── 📄 main.py               # FastAPI application
│   ├── 📄 config.py             # Configuration
│   └── 📄 dependencies.py       # Dependency injection
│
├── 📁 docs/                     # 📚 All documentation
│   ├── 📄 README.md             # Documentation index
│   ├── 🚀 Deployment docs
│   ├── 🔐 Security docs
│   ├── 🔌 API docs
│   └── 📋 Project docs
│
├── 📄 README.md                 # Project overview
├── 📄 requirements.txt          # Python dependencies
├── 📄 .env.example              # Environment template
├── 📄 .env                      # Your credentials (not in git)
│
├── 🐳 Docker files
│   ├── 📄 Dockerfile            # Application container
│   ├── 📄 docker-compose.yml   # Development setup
│   └── 📄 docker-compose.prod.yml # Production setup
│
├── 🚀 Deployment files
│   ├── 📄 deploy.sh             # Deployment script
│   ├── 📄 setup-server.sh       # Server setup script
│   └── 📄 nginx.conf            # Nginx configuration
│
└── 📄 postman_collection.json   # API testing collection
```

---

## 📁 Directory Details

### `/app` - Application Code

Main application directory containing all Python code.

```
app/
├── routers/          # API route handlers
│   ├── auth.py       # Authentication endpoints
│   ├── projects.py   # Project management
│   ├── meta.py       # Meta tag generation
│   ├── links.py      # Broken link detection
│   ├── competitor.py # Competitor analysis
│   └── serp.py       # SERP tracking
│
├── models/           # SQLAlchemy models
│   ├── user.py       # User model
│   ├── project.py    # Project model
│   ├── meta.py       # Meta tag model
│   ├── links.py      # Broken link model
│   ├── competitor.py # Competitor analysis model
│   └── serp.py       # SERP data model
│
├── services/         # Business logic
│   ├── meta_generator.py      # Meta tag generation service
│   ├── competitor_service.py  # Competitor analysis service
│   ├── serp_service.py        # SERP tracking service
│   └── scheduler.py           # Task scheduling
│
├── integrations/     # External API clients
│   ├── gemini_client.py  # Google Gemini AI
│   ├── apify_client.py   # Apify web scraping
│   └── email_client.py   # Email notifications
│
├── workers/          # Celery background tasks
│   ├── celery_app.py     # Celery configuration
│   └── tasks/            # Task definitions
│       ├── meta_tasks.py
│       ├── link_tasks.py
│       ├── competitor_tasks.py
│       └── serp_tasks.py
│
├── nlp/              # NLP & Machine Learning
│   ├── embeddings.py  # Text embeddings
│   └── clustering.py  # Topic clustering
│
├── utils/            # Utility functions
│   ├── validators.py      # Input validation
│   ├── scoring.py         # CTR scoring
│   └── scraper_utils.py   # Web scraping helpers
│
├── main.py           # FastAPI app initialization
├── config.py         # Configuration management
└── dependencies.py   # Dependency injection
```

### `/docs` - Documentation

All project documentation organized by category.

```
docs/
├── README.md                      # 📚 Documentation index
│
├── 🚀 Deployment
│   ├── DEPLOY_NOW.md              # Quick deploy commands
│   ├── QUICK_DEPLOY.md            # 3-command guide
│   ├── DEPLOYMENT_GUIDE.md        # Comprehensive guide
│   ├── DEPLOYMENT_SUMMARY.md      # Overview
│   └── DEPLOYMENT_CHECKLIST.md    # Checklist
│
├── 🔐 Security
│   ├── SECURITY.md                # Security guidelines
│   ├── SECURITY_AUDIT_SUMMARY.md  # Audit report
│   ├── CREDENTIALS_CHECKLIST.md   # Credential management
│   └── QUICK_SECURITY_REFERENCE.md # Quick reference
│
├── 🔌 API
│   ├── API_DOCUMENTATION.md       # Complete API reference
│   ├── API_QUICKSTART.md          # 5-minute start
│   ├── API_SETUP_SUMMARY.md       # Setup overview
│   └── SWAGGER_SETUP.md           # Swagger configuration
│
├── ⚙️ Configuration
│   └── ENVIRONMENT_SETUP.md       # Environment setup
│
└── 📋 Project
    ├── SCHEMA.md                  # Database schema
    ├── FRS.md                     # Requirements
    └── PROGRESS.md                # Development status
```

---

## 🔑 Key Files

### Configuration Files

| File | Purpose | In Git? |
|------|---------|---------|
| `.env` | Your actual credentials | ❌ No |
| `.env.example` | Template with placeholders | ✅ Yes |
| `.env.production` | Production template | ✅ Yes |
| `app/config.py` | Configuration loader | ✅ Yes |

### Docker Files

| File | Purpose |
|------|---------|
| `Dockerfile` | Application container definition |
| `docker-compose.yml` | Development environment |
| `docker-compose.prod.yml` | Production environment |
| `nginx.conf` | Nginx reverse proxy config |

### Deployment Files

| File | Purpose |
|------|---------|
| `deploy.sh` | Automated deployment script |
| `setup-server.sh` | One-time server setup |
| `postman_collection.json` | API testing collection |

### Documentation Files

| File | Purpose |
|------|---------|
| `README.md` | Project overview (root) |
| `docs/README.md` | Documentation index |
| `PROJECT_STRUCTURE.md` | This file |

---

## 🚀 Quick Navigation

### I want to...

#### Deploy the application
→ `docs/DEPLOY_NOW.md` or `docs/QUICK_DEPLOY.md`

#### Configure environment
→ `docs/ENVIRONMENT_SETUP.md` and `.env.example`

#### Use the API
→ `docs/API_QUICKSTART.md` and `docs/API_DOCUMENTATION.md`

#### Understand security
→ `docs/SECURITY.md` and `docs/CREDENTIALS_CHECKLIST.md`

#### Modify the code
→ `app/` directory

#### Run tests
→ `tests/` directory (if exists)

#### Deploy with Docker
→ `docker-compose.yml` or `docker-compose.prod.yml`

---

## 📊 File Count

```
Total Files: ~50+
├── Python files (.py): ~30
├── Documentation (.md): ~18
├── Configuration (.yml, .conf, .env): ~5
├── Scripts (.sh): 2
└── Other (.json, .txt): ~3
```

---

## 🔒 Security Notes

### Files to NEVER commit:

- ❌ `.env` - Contains actual credentials
- ❌ `*.log` - May contain sensitive data
- ❌ `__pycache__/` - Python cache
- ❌ `postgres_data/` - Database files

### Files that SHOULD be committed:

- ✅ `.env.example` - Template only
- ✅ All `.md` documentation
- ✅ All `.py` source code
- ✅ `requirements.txt`
- ✅ Docker files
- ✅ Deployment scripts

---

## 🎯 Development Workflow

### 1. Setup
```bash
git clone <repo>
cd seo-automation-suite
cp .env.example .env
# Edit .env with your credentials
```

### 2. Development
```bash
# Start services
docker-compose up -d

# View logs
docker-compose logs -f api

# Make changes to code in app/
# Changes auto-reload in development mode
```

### 3. Testing
```bash
# Access API docs
open http://localhost:8000/docs

# Test endpoints
# Use Postman collection
```

### 4. Deployment
```bash
# Deploy to server
./deploy.sh
```

---

## 📚 Documentation Organization

All documentation is now in the `docs/` directory for better organization:

- **Before**: Documentation scattered in root directory
- **After**: All docs in `docs/` with clear index

### Benefits:

1. ✅ Cleaner root directory
2. ✅ Easier to find documentation
3. ✅ Better organization by category
4. ✅ Clear documentation index
5. ✅ Professional project structure

---

## 🔄 Updates

When adding new files:

1. **Code files** → Add to `app/` directory
2. **Documentation** → Add to `docs/` directory
3. **Configuration** → Add to root directory
4. **Update this file** if structure changes significantly

---

## 📞 Support

- **Documentation Index**: [docs/README.md](docs/README.md)
- **Project README**: [README.md](README.md)
- **Quick Deploy**: [docs/DEPLOY_NOW.md](docs/DEPLOY_NOW.md)

---

*Last Updated: November 12, 2025*
