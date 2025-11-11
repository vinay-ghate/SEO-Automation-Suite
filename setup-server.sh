#!/bin/bash

# SEO Automation Suite - Server Setup Script
# This script sets up everything needed on a fresh Ubuntu server

set -e

echo "🚀 SEO Automation Suite - Server Setup"
echo "======================================"
echo ""

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

print_success() { echo -e "${GREEN}✅ $1${NC}"; }
print_error() { echo -e "${RED}❌ $1${NC}"; }
print_warning() { echo -e "${YELLOW}⚠️  $1${NC}"; }
print_info() { echo -e "${BLUE}ℹ️  $1${NC}"; }

# Check if running as root
if [ "$EUID" -eq 0 ]; then 
    print_error "Please do not run as root. Run as a regular user with sudo privileges."
    exit 1
fi

print_info "This script will install:"
echo "  - Docker"
echo "  - Docker Compose"
echo "  - Configure firewall"
echo "  - Set up the application"
echo ""
read -p "Continue? (y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    exit 1
fi

# Update system
print_info "Updating system packages..."
sudo apt update && sudo apt upgrade -y
print_success "System updated"

# Install dependencies
print_info "Installing dependencies..."
sudo apt install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release \
    git \
    ufw
print_success "Dependencies installed"

# Install Docker
if ! command -v docker &> /dev/null; then
    print_info "Installing Docker..."
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    sudo usermod -aG docker $USER
    rm get-docker.sh
    print_success "Docker installed"
else
    print_success "Docker already installed"
fi

# Install Docker Compose
if ! docker compose version &> /dev/null; then
    print_info "Installing Docker Compose..."
    sudo apt install -y docker-compose-plugin
    print_success "Docker Compose installed"
else
    print_success "Docker Compose already installed"
fi

# Configure firewall
print_info "Configuring firewall..."
sudo ufw --force enable
sudo ufw allow 22/tcp comment 'SSH'
sudo ufw allow 80/tcp comment 'HTTP'
sudo ufw allow 443/tcp comment 'HTTPS'
sudo ufw allow 8000/tcp comment 'API'
print_success "Firewall configured"

# Create application directory
APP_DIR="$HOME/seo-automation-suite"
if [ ! -d "$APP_DIR" ]; then
    print_info "Application directory will be created at: $APP_DIR"
    read -p "Enter your Git repository URL (or press Enter to skip): " REPO_URL
    
    if [ -n "$REPO_URL" ]; then
        print_info "Cloning repository..."
        git clone "$REPO_URL" "$APP_DIR"
        cd "$APP_DIR"
        print_success "Repository cloned"
    else
        print_warning "Skipping repository clone. Please manually copy your files to $APP_DIR"
        mkdir -p "$APP_DIR"
    fi
else
    print_warning "Directory $APP_DIR already exists"
    cd "$APP_DIR"
fi

# Setup environment file
if [ ! -f .env ]; then
    print_info "Setting up environment configuration..."
    
    if [ -f .env.example ]; then
        cp .env.example .env
        print_success "Created .env from .env.example"
    else
        print_warning ".env.example not found, creating basic .env"
        cat > .env << 'EOF'
DATABASE_URL=postgresql://user:password@postgres:5432/seo_automation
POSTGRES_USER=user
POSTGRES_PASSWORD=changeme
POSTGRES_DB=seo_automation
SECRET_KEY=changeme
APIFY_API_TOKEN=your_token
GEMINI_API_KEY=your_key
REDIS_URL=redis://redis:6379
CELERY_BROKER_URL=redis://redis:6379/0
CELERY_RESULT_BACKEND=redis://redis:6379/0
ALLOWED_ORIGINS=["http://localhost:3000"]
EOF
    fi
    
    print_warning "⚠️  IMPORTANT: Edit .env file with your actual credentials!"
    print_info "Run: nano .env"
else
    print_success ".env file already exists"
fi

# Make scripts executable
if [ -f deploy.sh ]; then
    chmod +x deploy.sh
    print_success "Made deploy.sh executable"
fi

echo ""
print_success "Server setup completed!"
echo ""
print_info "Next steps:"
echo "  1. Edit .env file with your credentials:"
echo "     nano $APP_DIR/.env"
echo ""
echo "  2. Generate a secure SECRET_KEY:"
echo "     openssl rand -hex 32"
echo ""
echo "  3. Deploy the application:"
echo "     cd $APP_DIR"
echo "     ./deploy.sh"
echo ""
echo "  4. Access your application:"
echo "     http://$(curl -s ifconfig.me):8000"
echo ""
print_warning "Note: You may need to log out and back in for Docker permissions to take effect"
print_info "Or run: newgrp docker"
echo ""
