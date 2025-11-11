#!/bin/bash

# SEO Automation Suite - Deployment Script
# This script helps deploy the application to a server

set -e  # Exit on error

echo "🚀 SEO Automation Suite - Deployment Script"
echo "============================================"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_info() {
    echo -e "ℹ️  $1"
}

# Check if .env file exists
if [ ! -f .env ]; then
    print_error ".env file not found!"
    print_info "Creating .env from .env.example..."
    cp .env.example .env
    print_warning "Please edit .env file with your actual credentials before continuing!"
    exit 1
fi

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    print_error "Docker is not installed!"
    print_info "Please install Docker: https://docs.docker.com/get-docker/"
    exit 1
fi

print_success "Docker is installed"

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null && ! docker compose version &> /dev/null; then
    print_error "Docker Compose is not installed!"
    print_info "Please install Docker Compose: https://docs.docker.com/compose/install/"
    exit 1
fi

print_success "Docker Compose is installed"

# Determine which docker-compose command to use
if docker compose version &> /dev/null; then
    DOCKER_COMPOSE="docker compose"
else
    DOCKER_COMPOSE="docker-compose"
fi

# Ask for deployment type
echo ""
print_info "Select deployment type:"
echo "1) Development (with hot reload)"
echo "2) Production (optimized)"
read -p "Enter choice [1-2]: " deploy_choice

if [ "$deploy_choice" = "2" ]; then
    COMPOSE_FILE="docker-compose.prod.yml"
    print_info "Using production configuration"
else
    COMPOSE_FILE="docker-compose.yml"
    print_info "Using development configuration"
fi

# Pull latest images
print_info "Pulling latest Docker images..."
$DOCKER_COMPOSE -f $COMPOSE_FILE pull

# Build images
print_info "Building Docker images..."
$DOCKER_COMPOSE -f $COMPOSE_FILE build

# Stop existing containers
print_info "Stopping existing containers..."
$DOCKER_COMPOSE -f $COMPOSE_FILE down

# Start containers
print_info "Starting containers..."
$DOCKER_COMPOSE -f $COMPOSE_FILE up -d

# Wait for services to be healthy
print_info "Waiting for services to be ready..."
sleep 10

# Check if API is running
if curl -f http://localhost:8000/health &> /dev/null; then
    print_success "API is running!"
else
    print_error "API is not responding. Check logs with: $DOCKER_COMPOSE -f $COMPOSE_FILE logs api"
    exit 1
fi

# Run database migrations (if alembic is configured)
if [ -d "alembic" ]; then
    print_info "Running database migrations..."
    $DOCKER_COMPOSE -f $COMPOSE_FILE exec -T api alembic upgrade head || print_warning "Migration failed or not configured"
fi

echo ""
print_success "Deployment completed successfully!"
echo ""
print_info "Access your application:"
echo "  - API: http://localhost:8000"
echo "  - API Docs: http://localhost:8000/docs"
echo "  - Health Check: http://localhost:8000/health"
echo ""
print_info "Useful commands:"
echo "  - View logs: $DOCKER_COMPOSE -f $COMPOSE_FILE logs -f"
echo "  - Stop: $DOCKER_COMPOSE -f $COMPOSE_FILE down"
echo "  - Restart: $DOCKER_COMPOSE -f $COMPOSE_FILE restart"
echo "  - View status: $DOCKER_COMPOSE -f $COMPOSE_FILE ps"
echo ""
