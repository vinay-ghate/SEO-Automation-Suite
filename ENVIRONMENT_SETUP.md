# Environment Setup Guide

## Quick Start

### 1. Copy Environment Template

```bash
cp .env.example .env
```

### 2. Edit `.env` File

Open `.env` in your text editor and replace all placeholder values with your actual credentials.

## Required Configuration

### Database Configuration

#### Option A: PostgreSQL (Recommended for Production)

```bash
DATABASE_URL=postgresql://username:password@host:port/database_name
```

**Example:**
```bash
DATABASE_URL=postgresql://myuser:mypassword@localhost:5432/seo_automation
```

**Using Docker:**
```bash
# The docker-compose.yml will create a PostgreSQL instance
# Use this connection string:
DATABASE_URL=postgresql://user:password@localhost:5432/seo_automation
```

#### Option B: SQLite (Development Only)

```bash
DATABASE_URL=sqlite:///./seo_automation.db
```

### Security Configuration

#### Generate a Secure Secret Key

**Using OpenSSL:**
```bash
openssl rand -hex 32
```

**Using Python:**
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

**Add to `.env`:**
```bash
SECRET_KEY=your_generated_key_here
```

### API Keys Configuration

#### 1. Apify API Token

**Get Your Token:**
1. Sign up at https://apify.com
2. Go to https://console.apify.com/account/integrations
3. Copy your API token

**Add to `.env`:**
```bash
APIFY_API_TOKEN=apify_api_YOUR_ACTUAL_TOKEN_HERE
```

#### 2. Google Gemini API Key

**Get Your Key:**
1. Go to https://makersuite.google.com/app/apikey
2. Click "Create API Key"
3. Copy the generated key

**Add to `.env`:**
```bash
GEMINI_API_KEY=YOUR_ACTUAL_GEMINI_KEY_HERE
```

### Email Configuration (Optional)

#### Gmail SMTP Setup

**Get App Password:**
1. Enable 2-Factor Authentication on your Google account
2. Go to https://myaccount.google.com/apppasswords
3. Generate an app password for "Mail"

**Add to `.env`:**
```bash
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-16-char-app-password
```

#### Other Email Providers

**SendGrid:**
```bash
SMTP_HOST=smtp.sendgrid.net
SMTP_PORT=587
SMTP_USER=apikey
SMTP_PASSWORD=your-sendgrid-api-key
```

**Mailgun:**
```bash
SMTP_HOST=smtp.mailgun.org
SMTP_PORT=587
SMTP_USER=postmaster@your-domain.mailgun.org
SMTP_PASSWORD=your-mailgun-password
```

### Redis Configuration

**Default (Local):**
```bash
REDIS_URL=redis://localhost:6379
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0
```

**With Password:**
```bash
REDIS_URL=redis://:password@localhost:6379
```

**Remote Redis:**
```bash
REDIS_URL=redis://username:password@redis-host:6379
```

### CORS Configuration

**Add your frontend URLs:**
```bash
ALLOWED_ORIGINS=["http://localhost:3000","http://localhost:5173","https://yourdomain.com"]
```

## Complete `.env` Example

```bash
# Database Configuration
DATABASE_URL=postgresql://myuser:mypassword@localhost:5432/seo_automation

# Security Configuration
SECRET_KEY=a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60

# Apify Configuration
APIFY_API_TOKEN=apify_api_waYf2
APIFY_API_URL=https://api.apify.com/v2

# Google Gemini AI Configuration
GEMINI_API_KEY=AIzaSyAw5MkMYHhx32QoRwM-oaTdkD8XlO3MDHg

# Redis Configuration
REDIS_URL=redis://localhost:6379
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0

# Email Configuration
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=myemail@gmail.com
SMTP_PASSWORD=abcd efgh ijkl mnop

# CORS Configuration
ALLOWED_ORIGINS=["http://localhost:3000"]
```

## Verification

### Check Configuration Loading

```bash
python -c "from app.config import settings; print('✅ Config loaded successfully')"
```

### Verify Required Variables

```python
from app.config import settings

# Check all required variables are set
required_vars = [
    'DATABASE_URL',
    'SECRET_KEY',
    'APIFY_API_TOKEN',
    'GEMINI_API_KEY'
]

for var in required_vars:
    value = getattr(settings, var)
    if value:
        print(f"✅ {var} is set")
    else:
        print(f"❌ {var} is NOT set")
```

### Test Database Connection

```python
from sqlalchemy import create_engine
from app.config import settings

try:
    engine = create_engine(settings.DATABASE_URL)
    with engine.connect() as conn:
        print("✅ Database connection successful")
except Exception as e:
    print(f"❌ Database connection failed: {e}")
```

### Test Redis Connection

```python
import redis
from app.config import settings

try:
    r = redis.from_url(settings.REDIS_URL)
    r.ping()
    print("✅ Redis connection successful")
except Exception as e:
    print(f"❌ Redis connection failed: {e}")
```

## Docker Setup

### Using Docker Compose

**1. Create `.env` file** (as described above)

**2. Start services:**
```bash
docker-compose up -d
```

**3. Check logs:**
```bash
docker-compose logs -f api
```

**4. Stop services:**
```bash
docker-compose down
```

### Environment Variables in Docker

Docker Compose automatically loads `.env` file. You can also override:

```bash
# Override specific variables
DATABASE_URL=postgresql://user:pass@host/db docker-compose up
```

## Different Environments

### Development

Create `.env.development`:
```bash
DATABASE_URL=sqlite:///./dev.db
DEBUG=true
```

### Staging

Create `.env.staging`:
```bash
DATABASE_URL=postgresql://user:pass@staging-db/seo
DEBUG=false
```

### Production

**Never use `.env` files in production!**

Use environment variables directly:
```bash
export DATABASE_URL="postgresql://..."
export SECRET_KEY="..."
```

Or use secret management services:
- AWS Secrets Manager
- Google Cloud Secret Manager
- Azure Key Vault
- HashiCorp Vault

## Troubleshooting

### "Config validation error"

**Problem:** Missing required environment variables

**Solution:**
```bash
# Check which variables are missing
python -c "from app.config import settings"
```

### "Database connection failed"

**Problem:** Incorrect DATABASE_URL or database not running

**Solution:**
```bash
# Check if PostgreSQL is running
pg_isready -h localhost -p 5432

# Or start with Docker
docker-compose up postgres
```

### "Redis connection refused"

**Problem:** Redis not running

**Solution:**
```bash
# Start Redis with Docker
docker-compose up redis

# Or install locally
# macOS: brew install redis && brew services start redis
# Ubuntu: sudo apt install redis-server && sudo systemctl start redis
```

### "Invalid API key"

**Problem:** Incorrect or expired API keys

**Solution:**
1. Verify keys in respective dashboards
2. Regenerate if necessary
3. Update `.env` file
4. Restart application

### "SMTP authentication failed"

**Problem:** Incorrect email credentials or 2FA not enabled

**Solution:**
1. Enable 2-Factor Authentication on Google
2. Generate App Password
3. Use the 16-character app password (not your regular password)

## Security Reminders

- ✅ `.env` is in `.gitignore`
- ✅ Never commit `.env` to version control
- ✅ Use strong, unique passwords
- ✅ Rotate keys regularly
- ✅ Use different keys for each environment
- ✅ Never share credentials in chat/email
- ✅ Use secret management in production

## Additional Resources

- [Pydantic Settings Documentation](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)
- [12-Factor App Config](https://12factor.net/config)
- [PostgreSQL Connection Strings](https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING)
- [Redis Configuration](https://redis.io/docs/management/config/)

## Need Help?

Check the [SECURITY.md](SECURITY.md) file for security best practices and credential management guidelines.

---

**Remember: Keep your `.env` file secure and never commit it to version control!** 🔒
