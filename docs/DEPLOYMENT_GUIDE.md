# Deployment Guide

## 🚀 Quick Deployment (5 Minutes)

### Prerequisites

- Server with Docker and Docker Compose installed
- Domain name (optional, for production)
- SSH access to your server

### One-Command Deployment

```bash
# 1. Clone repository
git clone <your-repo-url>
cd seo-automation-suite

# 2. Configure environment
cp .env.example .env
nano .env  # Edit with your credentials

# 3. Deploy
chmod +x deploy.sh
./deploy.sh
```

That's it! Your application will be running at `http://your-server-ip:8000`

---

## 📋 Detailed Deployment Options

### Option 1: VPS/Cloud Server (Recommended)

Perfect for: DigitalOcean, Linode, AWS EC2, Google Cloud, Azure

#### Step 1: Prepare Your Server

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Install Docker Compose
sudo apt install docker-compose-plugin -y

# Add your user to docker group
sudo usermod -aG docker $USER
newgrp docker
```

#### Step 2: Clone and Configure

```bash
# Clone repository
git clone <your-repo-url>
cd seo-automation-suite

# Configure environment
cp .env.example .env
nano .env
```

**Edit `.env` with your credentials:**
```bash
DATABASE_URL=postgresql://user:password@postgres:5432/seo_automation
SECRET_KEY=$(openssl rand -hex 32)
APIFY_API_TOKEN=your_apify_token
GEMINI_API_KEY=your_gemini_key
```

#### Step 3: Deploy

```bash
# Make deploy script executable
chmod +x deploy.sh

# Run deployment
./deploy.sh

# Select option 2 for production
```

#### Step 4: Configure Firewall

```bash
# Allow HTTP and HTTPS
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw allow 22/tcp  # SSH
sudo ufw enable
```

#### Step 5: Access Your Application

- API: `http://your-server-ip:8000`
- Docs: `http://your-server-ip:8000/docs`

---

### Option 2: Docker Compose (Manual)

#### Development Deployment

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

#### Production Deployment

```bash
# Start with production config
docker-compose -f docker-compose.prod.yml up -d

# View logs
docker-compose -f docker-compose.prod.yml logs -f

# Stop services
docker-compose -f docker-compose.prod.yml down
```

---

### Option 3: Individual Services

If you prefer to run services separately:

#### 1. PostgreSQL

```bash
docker run -d \
  --name postgres \
  -e POSTGRES_USER=user \
  -e POSTGRES_PASSWORD=password \
  -e POSTGRES_DB=seo_automation \
  -p 5432:5432 \
  -v postgres_data:/var/lib/postgresql/data \
  postgres:15-alpine
```

#### 2. Redis

```bash
docker run -d \
  --name redis \
  -p 6379:6379 \
  redis:7-alpine
```

#### 3. API

```bash
docker build -t seo-api .

docker run -d \
  --name seo-api \
  -p 8000:8000 \
  --env-file .env \
  -e DATABASE_URL=postgresql://user:password@host.docker.internal:5432/seo_automation \
  -e REDIS_URL=redis://host.docker.internal:6379 \
  seo-api
```

#### 4. Celery Worker

```bash
docker run -d \
  --name celery-worker \
  --env-file .env \
  -e DATABASE_URL=postgresql://user:password@host.docker.internal:5432/seo_automation \
  -e CELERY_BROKER_URL=redis://host.docker.internal:6379/0 \
  seo-api \
  celery -A app.workers.celery_app worker --loglevel=info
```

---

## 🌐 Domain and SSL Setup

### Step 1: Point Domain to Server

Add an A record in your DNS:
```
Type: A
Name: @
Value: your-server-ip
TTL: 3600
```

For subdomain:
```
Type: A
Name: api
Value: your-server-ip
TTL: 3600
```

### Step 2: Install Certbot (Let's Encrypt)

```bash
# Install Certbot
sudo apt install certbot python3-certbot-nginx -y

# Get SSL certificate
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
```

### Step 3: Update Nginx Configuration

Edit `nginx.conf` and uncomment the HTTPS section:

```nginx
server {
    listen 443 ssl http2;
    server_name yourdomain.com;
    
    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;
    
    # ... rest of configuration
}
```

### Step 4: Restart Nginx

```bash
docker-compose -f docker-compose.prod.yml restart nginx
```

---

## 🔧 Configuration

### Environment Variables

Create `.env` file with these required variables:

```bash
# Database
DATABASE_URL=postgresql://user:password@postgres:5432/seo_automation
POSTGRES_USER=user
POSTGRES_PASSWORD=strong_password_here
POSTGRES_DB=seo_automation

# Security
SECRET_KEY=your-secret-key-generate-with-openssl
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60

# API Keys
APIFY_API_TOKEN=apify_api_YOUR_TOKEN
APIFY_API_URL=https://api.apify.com/v2
GEMINI_API_KEY=YOUR_GEMINI_KEY

# Redis
REDIS_URL=redis://redis:6379
CELERY_BROKER_URL=redis://redis:6379/0
CELERY_RESULT_BACKEND=redis://redis:6379/0

# Email (Optional)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-app-password

# CORS
ALLOWED_ORIGINS=["https://yourdomain.com","https://www.yourdomain.com"]
```

### Generate Secure Keys

```bash
# Generate SECRET_KEY
openssl rand -hex 32

# Generate strong password
openssl rand -base64 32
```

---

## 📊 Monitoring and Maintenance

### View Logs

```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f api
docker-compose logs -f celery_worker

# Last 100 lines
docker-compose logs --tail=100 api
```

### Check Service Status

```bash
# List running containers
docker-compose ps

# Check health
curl http://localhost:8000/health
```

### Database Backup

```bash
# Backup database
docker-compose exec postgres pg_dump -U user seo_automation > backup.sql

# Restore database
docker-compose exec -T postgres psql -U user seo_automation < backup.sql
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

---

## 🔒 Security Checklist

- [ ] Change default passwords in `.env`
- [ ] Generate strong `SECRET_KEY`
- [ ] Configure firewall (UFW)
- [ ] Set up SSL/HTTPS
- [ ] Enable automatic security updates
- [ ] Configure backup strategy
- [ ] Set up monitoring/alerts
- [ ] Review and restrict CORS origins
- [ ] Disable debug mode in production
- [ ] Use strong database passwords

---

## 🚨 Troubleshooting

### API Not Starting

```bash
# Check logs
docker-compose logs api

# Common issues:
# 1. Missing environment variables
# 2. Database connection failed
# 3. Port already in use
```

### Database Connection Error

```bash
# Check if PostgreSQL is running
docker-compose ps postgres

# Test connection
docker-compose exec postgres psql -U user -d seo_automation
```

### Redis Connection Error

```bash
# Check if Redis is running
docker-compose ps redis

# Test connection
docker-compose exec redis redis-cli ping
```

### Port Already in Use

```bash
# Find process using port 8000
sudo lsof -i :8000

# Kill process
sudo kill -9 <PID>

# Or change port in docker-compose.yml
ports:
  - "8001:8000"  # Use port 8001 instead
```

### Out of Memory

```bash
# Check memory usage
docker stats

# Increase swap space
sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

---

## 📈 Performance Optimization

### Increase Workers

Edit `docker-compose.prod.yml`:

```yaml
api:
  command: uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4

celery_worker:
  command: celery -A app.workers.celery_app worker --concurrency=4
```

### Enable Caching

Add Redis caching for API responses (implement in code).

### Database Optimization

```sql
-- Create indexes for better performance
CREATE INDEX idx_projects_owner ON projects(owner_id);
CREATE INDEX idx_meta_project ON meta_tags(project_id);
```

---

## 🌍 Popular Hosting Providers

### DigitalOcean

1. Create Droplet (Ubuntu 22.04)
2. Choose size: $12/month (2GB RAM) minimum
3. Follow VPS deployment steps above

**One-Click Deploy**: Use DigitalOcean App Platform

### AWS EC2

1. Launch EC2 instance (t3.small minimum)
2. Configure security group (ports 80, 443, 22)
3. Follow VPS deployment steps

### Google Cloud Run

```bash
# Build and push image
gcloud builds submit --tag gcr.io/PROJECT_ID/seo-api

# Deploy
gcloud run deploy seo-api \
  --image gcr.io/PROJECT_ID/seo-api \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

### Heroku

```bash
# Login
heroku login

# Create app
heroku create your-app-name

# Add PostgreSQL
heroku addons:create heroku-postgresql:hobby-dev

# Add Redis
heroku addons:create heroku-redis:hobby-dev

# Deploy
git push heroku main
```

### Railway

1. Connect GitHub repository
2. Add PostgreSQL and Redis services
3. Configure environment variables
4. Deploy automatically

---

## 📞 Support

- **Documentation**: See all `*.md` files in repository
- **Issues**: Create GitHub issue
- **Security**: See [SECURITY.md](SECURITY.md)

---

## 🎉 Success!

Your SEO Automation Suite is now deployed and running!

Access your application:
- **API**: http://your-domain.com
- **Documentation**: http://your-domain.com/docs
- **Health Check**: http://your-domain.com/health

Next steps:
1. Test all endpoints in Swagger UI
2. Set up monitoring and alerts
3. Configure automated backups
4. Review security settings
5. Share API documentation with your team
