# Security Guidelines

## Environment Variables and Credentials

### ⚠️ IMPORTANT: Never Commit Credentials

All API keys, passwords, and sensitive configuration must be stored in the `.env` file, which is excluded from version control.

### Configuration Files

- **`.env`** - Your actual credentials (NEVER commit this)
- **`.env.example`** - Template with placeholder values (safe to commit)
- **`app/config.py`** - Configuration loader (no hardcoded credentials)

### Required Environment Variables

All credentials are loaded from `.env` file:

```bash
# Database
DATABASE_URL=postgresql://user:password@host:port/database

# Security
SECRET_KEY=your-secret-key-here

# API Keys
APIFY_API_TOKEN=apify_api_YOUR_TOKEN
GEMINI_API_KEY=YOUR_GEMINI_KEY

# Email
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-app-password
```

## Setting Up Your Environment

### 1. Copy the Example File

```bash
cp .env.example .env
```

### 2. Generate a Secure Secret Key

```bash
# Using OpenSSL
openssl rand -hex 32

# Using Python
python -c "import secrets; print(secrets.token_hex(32))"
```

### 3. Get Your API Keys

#### Apify API Token
1. Go to https://console.apify.com/account/integrations
2. Copy your API token
3. Add to `.env`: `APIFY_API_TOKEN=apify_api_YOUR_TOKEN`

#### Google Gemini API Key
1. Go to https://makersuite.google.com/app/apikey
2. Create a new API key
3. Add to `.env`: `GEMINI_API_KEY=YOUR_KEY`

#### Gmail App Password (for SMTP)
1. Go to https://myaccount.google.com/apppasswords
2. Generate an app password
3. Add to `.env`: `SMTP_PASSWORD=your-app-password`

### 4. Configure Database

For PostgreSQL:
```bash
DATABASE_URL=postgresql://username:password@localhost:5432/database_name
```

For SQLite (development only):
```bash
DATABASE_URL=sqlite:///./seo_automation.db
```

## Verifying Configuration

### Check if .env is Loaded

```python
from app.config import settings

# This should NOT show actual credentials in logs
print(f"Database configured: {bool(settings.DATABASE_URL)}")
print(f"Apify configured: {bool(settings.APIFY_API_TOKEN)}")
print(f"Gemini configured: {bool(settings.GEMINI_API_KEY)}")
```

### Test Configuration

```bash
# Start Python shell
python

# Import settings
from app.config import settings

# Verify (don't print actual values!)
assert settings.DATABASE_URL, "DATABASE_URL not set"
assert settings.SECRET_KEY, "SECRET_KEY not set"
assert settings.APIFY_API_TOKEN, "APIFY_API_TOKEN not set"
assert settings.GEMINI_API_KEY, "GEMINI_API_KEY not set"

print("✅ All required environment variables are set!")
```

## Security Best Practices

### 1. Never Hardcode Credentials

❌ **BAD:**
```python
api_key = "AIzaSyAw5MkMYHhx32QoRwM-oaTdkD8XlO3MDHg"
```

✅ **GOOD:**
```python
from app.config import settings
api_key = settings.GEMINI_API_KEY
```

### 2. Use Strong Secret Keys

```bash
# Generate a strong key
openssl rand -hex 32
```

### 3. Rotate Keys Regularly

- Change `SECRET_KEY` every 90 days
- Rotate API keys if compromised
- Update passwords quarterly

### 4. Use Different Keys per Environment

- Development: `.env.development`
- Staging: `.env.staging`
- Production: `.env.production`

### 5. Restrict Database Access

```bash
# Create a dedicated database user with limited permissions
CREATE USER seo_app WITH PASSWORD 'strong_password';
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO seo_app;
```

### 6. Use Environment-Specific Settings

```python
# app/config.py
class Settings(BaseSettings):
    ENVIRONMENT: str = "development"  # development, staging, production
    DEBUG: bool = False
    
    @property
    def is_production(self) -> bool:
        return self.ENVIRONMENT == "production"
```

## Production Deployment

### Environment Variables in Production

**Never use `.env` files in production.** Instead, use:

#### Docker
```bash
docker run -e DATABASE_URL="..." -e SECRET_KEY="..." myapp
```

#### Docker Compose
```yaml
services:
  app:
    environment:
      - DATABASE_URL=${DATABASE_URL}
      - SECRET_KEY=${SECRET_KEY}
```

#### Kubernetes
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: app-secrets
type: Opaque
data:
  database-url: <base64-encoded>
  secret-key: <base64-encoded>
```

#### Cloud Platforms

- **AWS**: Use AWS Secrets Manager or Parameter Store
- **Google Cloud**: Use Secret Manager
- **Azure**: Use Key Vault
- **Heroku**: Use Config Vars
- **Vercel/Netlify**: Use Environment Variables in dashboard

### Production Checklist

- [ ] All credentials stored in secure secret management
- [ ] `.env` file not deployed to production
- [ ] Strong, unique `SECRET_KEY` generated
- [ ] Database credentials use least privilege
- [ ] API keys are production-specific
- [ ] HTTPS enabled for all endpoints
- [ ] CORS configured for production domains only
- [ ] Debug mode disabled
- [ ] Error messages don't leak sensitive info

## Handling Credential Leaks

### If Credentials Are Compromised

1. **Immediately rotate all affected credentials**
   - Generate new API keys
   - Change database passwords
   - Update SECRET_KEY

2. **Revoke compromised keys**
   - Apify: Delete token in console
   - Gemini: Restrict or delete API key
   - Database: Change password

3. **Check for unauthorized access**
   - Review API usage logs
   - Check database access logs
   - Monitor for unusual activity

4. **Update all environments**
   - Development
   - Staging
   - Production

### If .env Was Committed to Git

```bash
# Remove from history (use with caution!)
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch .env" \
  --prune-empty --tag-name-filter cat -- --all

# Force push (coordinate with team!)
git push origin --force --all

# Rotate ALL credentials immediately
```

## Monitoring and Auditing

### Log Security Events

```python
import logging

logger = logging.getLogger(__name__)

# Log authentication attempts
logger.info(f"Login attempt for user: {email}")

# Log API key usage
logger.info(f"API call to Gemini: {endpoint}")

# Never log credentials!
# ❌ logger.info(f"Using key: {api_key}")
```

### Regular Security Audits

- Review who has access to credentials
- Check for unused API keys
- Audit database access logs
- Monitor API usage patterns

## Additional Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [12-Factor App Config](https://12factor.net/config)
- [Pydantic Settings Documentation](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)

## Questions?

If you discover a security vulnerability, please email security@example.com instead of creating a public issue.

---

**Remember: Security is everyone's responsibility!** 🔒
