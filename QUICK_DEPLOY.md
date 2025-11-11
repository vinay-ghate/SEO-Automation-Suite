# Quick Deploy Guide

## 🚀 Deploy in 3 Commands

### On Your Server

```bash
# 1. Setup server (installs Docker, configures firewall)
curl -fsSL https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/setup-server.sh | bash

# 2. Configure credentials
cd ~/seo-automation-suite
nano .env  # Edit with your API keys

# 3. Deploy
./deploy.sh
```

**Done!** Your API is now running at `http://your-server-ip:8000`

---

## 📋 Step-by-Step Guide

### Step 1: Get a Server

Choose any of these providers:

| Provider | Plan | Cost | Link |
|----------|------|------|------|
| **DigitalOcean** | Basic Droplet | $12/mo | [Sign up](https://digitalocean.com) |
| **Linode** | Nanode | $5/mo | [Sign up](https://linode.com) |
| **Vultr** | Cloud Compute | $6/mo | [Sign up](https://vultr.com) |
| **AWS** | t3.small | ~$15/mo | [Sign up](https://aws.amazon.com) |

**Minimum Requirements:**
- 2GB RAM
- 1 CPU
- 25GB Storage
- Ubuntu 22.04 LTS

### Step 2: Connect to Your Server

```bash
ssh root@your-server-ip
# or
ssh ubuntu@your-server-ip
```

### Step 3: Run Setup Script

```bash
# Download and run setup script
curl -fsSL https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/setup-server.sh -o setup.sh
chmod +x setup.sh
./setup.sh
```

This will:
- ✅ Install Docker
- ✅ Install Docker Compose
- ✅ Configure firewall
- ✅ Clone your repository
- ✅ Create .env file

### Step 4: Configure Environment

```bash
cd ~/seo-automation-suite
nano .env
```

**Required Configuration:**

```bash
# Generate secret key
SECRET_KEY=$(openssl rand -hex 32)

# Add your API keys
APIFY_API_TOKEN=apify_api_YOUR_TOKEN
GEMINI_API_KEY=YOUR_GEMINI_KEY

# Set strong database password
POSTGRES_PASSWORD=$(openssl rand -base64 32)
```

**Save and exit:** `Ctrl+X`, then `Y`, then `Enter`

### Step 5: Deploy

```bash
./deploy.sh
```

Select option `2` for production deployment.

### Step 6: Verify

```bash
# Check if services are running
docker-compose ps

# Test API
curl http://localhost:8000/health

# View logs
docker-compose logs -f api
```

### Step 7: Access Your API

Open in browser:
- **API**: `http://your-server-ip:8000`
- **Docs**: `http://your-server-ip:8000/docs`

---

## 🌐 Add Domain (Optional)

### Step 1: Point Domain to Server

In your domain registrar (Namecheap, GoDaddy, etc.):

```
Type: A
Name: @
Value: your-server-ip
TTL: 3600
```

### Step 2: Install SSL Certificate

```bash
# Install Certbot
sudo apt install certbot python3-certbot-nginx -y

# Get certificate
sudo certbot certonly --standalone -d yourdomain.com
```

### Step 3: Update Nginx Config

```bash
nano nginx.conf
```

Uncomment and update the HTTPS section with your domain.

### Step 4: Restart Services

```bash
docker-compose -f docker-compose.prod.yml restart nginx
```

Now access via: `https://yourdomain.com`

---

## 🔧 Common Tasks

### View Logs

```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f api
docker-compose logs -f celery_worker
```

### Restart Services

```bash
# Restart all
docker-compose restart

# Restart specific service
docker-compose restart api
```

### Update Application

```bash
# Pull latest code
git pull

# Rebuild and restart
docker-compose down
docker-compose build
docker-compose up -d
```

### Backup Database

```bash
# Create backup
docker-compose exec postgres pg_dump -U user seo_automation > backup_$(date +%Y%m%d).sql

# Restore backup
docker-compose exec -T postgres psql -U user seo_automation < backup_20241112.sql
```

### Stop Application

```bash
docker-compose down
```

### Start Application

```bash
docker-compose up -d
```

---

## 🚨 Troubleshooting

### "Cannot connect to Docker daemon"

```bash
# Add user to docker group
sudo usermod -aG docker $USER
newgrp docker
```

### "Port 8000 already in use"

```bash
# Find what's using the port
sudo lsof -i :8000

# Kill the process
sudo kill -9 <PID>
```

### "Database connection failed"

```bash
# Check if PostgreSQL is running
docker-compose ps postgres

# View PostgreSQL logs
docker-compose logs postgres
```

### "API returns 500 error"

```bash
# Check API logs
docker-compose logs api

# Common causes:
# - Missing environment variables
# - Database not ready
# - Invalid API keys
```

---

## 📊 Monitoring

### Check Service Status

```bash
# List all containers
docker-compose ps

# Check resource usage
docker stats
```

### Health Check

```bash
# API health
curl http://localhost:8000/health

# Should return: {"status":"healthy"}
```

### View Metrics

```bash
# Container stats
docker stats --no-stream

# Disk usage
df -h

# Memory usage
free -h
```

---

## 🔒 Security Checklist

After deployment, verify:

- [ ] Changed default passwords in `.env`
- [ ] Generated strong `SECRET_KEY`
- [ ] Firewall is enabled (`sudo ufw status`)
- [ ] Only necessary ports are open (22, 80, 443)
- [ ] SSL certificate installed (for production)
- [ ] Regular backups configured
- [ ] Monitoring set up
- [ ] `.env` file has correct permissions (`chmod 600 .env`)

---

## 💰 Cost Estimate

### Monthly Costs

| Service | Provider | Cost |
|---------|----------|------|
| **Server** | DigitalOcean | $12 |
| **Domain** | Namecheap | $1 |
| **SSL** | Let's Encrypt | Free |
| **Apify** | Pay-as-you-go | ~$10 |
| **Gemini** | Pay-as-you-go | ~$5 |
| **Total** | | **~$28/mo** |

### Free Tier Options

- **Railway**: Free tier available
- **Render**: Free tier for web services
- **Fly.io**: Free tier with limitations
- **Heroku**: Hobby tier $7/mo

---

## 🎯 Next Steps

1. ✅ Test all API endpoints in Swagger UI
2. ✅ Set up automated backups
3. ✅ Configure monitoring/alerts
4. ✅ Add your domain and SSL
5. ✅ Share API docs with your team
6. ✅ Set up CI/CD pipeline (optional)

---

## 📞 Need Help?

- **Documentation**: [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)
- **Security**: [SECURITY.md](SECURITY.md)
- **API Docs**: [API_DOCUMENTATION.md](API_DOCUMENTATION.md)
- **Environment Setup**: [ENVIRONMENT_SETUP.md](ENVIRONMENT_SETUP.md)

---

## 🎉 Success!

Your SEO Automation Suite is now live!

**Share your API:**
- API URL: `http://your-server-ip:8000`
- Documentation: `http://your-server-ip:8000/docs`
- Postman Collection: `postman_collection.json`

**Happy automating!** 🚀
