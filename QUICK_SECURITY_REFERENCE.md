# Quick Security Reference Card

## 🚀 Quick Setup (2 Minutes)

```bash
# 1. Copy template
cp .env.example .env

# 2. Generate secret key
openssl rand -hex 32

# 3. Edit .env with your credentials
nano .env  # or use your favorite editor

# 4. Start application
docker-compose up -d
```

## 📋 Required Variables

```bash
DATABASE_URL=postgresql://user:pass@host:port/db
SECRET_KEY=<generate-with-openssl-rand-hex-32>
APIFY_API_TOKEN=apify_api_YOUR_TOKEN
GEMINI_API_KEY=YOUR_GEMINI_KEY
```

## 🔑 Get API Keys

| Service | URL |
|---------|-----|
| **Apify** | https://console.apify.com/account/integrations |
| **Gemini** | https://makersuite.google.com/app/apikey |
| **Gmail App Password** | https://myaccount.google.com/apppasswords |

## ✅ Verify Setup

```python
from app.config import settings
assert settings.DATABASE_URL
assert settings.SECRET_KEY
assert settings.APIFY_API_TOKEN
assert settings.GEMINI_API_KEY
print("✅ All configured!")
```

## ❌ Common Mistakes

| ❌ Wrong | ✅ Right |
|---------|---------|
| Hardcode API keys in code | Use `settings.API_KEY` |
| Commit `.env` file | Keep `.env` in `.gitignore` |
| Use same keys everywhere | Different keys per environment |
| Share keys in chat/email | Use secure secret sharing |
| Empty `.env` file | Fill all required variables |

## 🔒 Security Rules

1. ✅ `.env` is in `.gitignore`
2. ✅ Never commit credentials
3. ✅ Use strong secret keys
4. ✅ Rotate keys every 90 days
5. ✅ Different keys per environment
6. ✅ Enable 2FA on all accounts

## 📚 Documentation

- **Setup Guide**: [ENVIRONMENT_SETUP.md](ENVIRONMENT_SETUP.md)
- **Security Guide**: [SECURITY.md](SECURITY.md)
- **Audit Report**: [SECURITY_AUDIT_SUMMARY.md](SECURITY_AUDIT_SUMMARY.md)
- **Checklist**: [CREDENTIALS_CHECKLIST.md](CREDENTIALS_CHECKLIST.md)

## 🆘 Troubleshooting

### "Config validation error"
→ Missing variables in `.env` file

### "Database connection failed"
→ Check `DATABASE_URL` format

### "Invalid API key"
→ Verify key in respective dashboard

### "SMTP authentication failed"
→ Use Gmail App Password, not regular password

## 🚨 If Credentials Leaked

1. **Immediately revoke** all affected keys
2. **Generate new keys** from dashboards
3. **Update `.env` file**
4. **Restart application**
5. **Check access logs**

## 📞 Support

- **Apify**: https://apify.com/contact
- **Google Cloud**: https://cloud.google.com/support
- **Documentation**: See files above

---

**Remember**: Keep `.env` secure and never commit it! 🔒
