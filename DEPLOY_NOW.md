# 🚀 Deploy Now - Quick Reference

## Copy-Paste Commands

### 1️⃣ Setup Server (One-Time)

```bash
# Connect to your server
ssh root@your-server-ip

# Run setup script
curl -fsSL https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/setup-server.sh -o setup.sh
chmod +x setup.sh
./setup.sh
```

### 2️⃣ Configure Environment

```bash
cd ~/seo-automation-suite
nano .env
```

**Copy this template and fill in your values:**

```bash
# Database
DATABASE_URL=postgresql://user:password@postgres:5432/seo_automation
POSTGRES_USER=user
POSTGRES_PASSWORD=CHANGE_ME
POSTGRES_DB=seo_automation

# Security - Generate with: openssl rand -hex 32
SECRET_KEY=PASTE_GENERATED_KEY_HERE

# API Keys
APIFY_API_TOKEN=apify_api_YOUR_TOKEN
GEMINI_API_KEY=YOUR_GEMINI_KEY

# Redis
REDIS_URL=redis://redis:6379
CELERY_BROKER_URL=redis://redis:6379/0
CELERY_RESULT_BACKEND=redis://redis:6379/0

# CORS
ALLOWED_ORIGINS=["http://localhost:3000"]
```

**Generate SECRET_KEY:**
```bash
openssl rand -hex 32
```

**Save:** Press `Ctrl+X`, then `Y`, then `Enter`

### 3️⃣ Deploy

```bash
./deploy.sh
# Select option 2 for production
```

### 4️⃣ Verify

```bash
# Check health
curl http://localhost:8000/health

# Should return: {"status":"healthy"}
```

---

## 🌐 Access Your API

- **API**: `http://your-server-ip:8000`
- **Docs**: `http://your-server-ip:8000/docs`
- **Health**: `http://your-server-ip:8000/health`

---

## 🔑 Get API Keys

| Service | URL |
|---------|-----|
| Apify | https://console.apify.com/account/integrations |
| Gemini | https://makersuite.google.com/app/apikey |

---

## 📊 Useful Commands

```bash
# View logs
docker-compose logs -f api

# Restart
docker-compose restart

# Stop
docker-compose down

# Start
docker-compose up -d

# Status
docker-compose ps
```

---

## 🆘 Troubleshooting

### "Cannot connect to Docker daemon"
```bash
sudo usermod -aG docker $USER
newgrp docker
```

### "Port 8000 already in use"
```bash
sudo lsof -i :8000
sudo kill -9 <PID>
```

### "Database connection failed"
```bash
docker-compose logs postgres
```

---

## 📚 Full Documentation

- **Quick Deploy**: [QUICK_DEPLOY.md](QUICK_DEPLOY.md)
- **Full Guide**: [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)
- **Checklist**: [DEPLOYMENT_CHECKLIST.md](DEPLOYMENT_CHECKLIST.md)
- **Summary**: [DEPLOYMENT_SUMMARY.md](DEPLOYMENT_SUMMARY.md)

---

## ✅ Success!

When you see:
```
✅ Deployment completed successfully!
```

Your API is live! 🎉

Test it: `http://your-server-ip:8000/docs`

---

**Need help?** Check [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)
