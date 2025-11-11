# Deployment Checklist

## Pre-Deployment

### Server Setup
- [ ] Server provisioned (2GB RAM minimum)
- [ ] Ubuntu 22.04 LTS installed
- [ ] SSH access configured
- [ ] Domain name purchased (optional)
- [ ] DNS configured to point to server

### Local Preparation
- [ ] Code committed to Git repository
- [ ] `.env.example` file updated
- [ ] Documentation reviewed
- [ ] API keys obtained:
  - [ ] Apify API token
  - [ ] Google Gemini API key
  - [ ] SMTP credentials (if using email)

## Deployment Steps

### 1. Server Configuration
- [ ] Run `setup-server.sh` script
- [ ] Docker installed and running
- [ ] Docker Compose installed
- [ ] Firewall configured (ports 22, 80, 443, 8000)
- [ ] User added to docker group

### 2. Application Setup
- [ ] Repository cloned to server
- [ ] `.env` file created from `.env.example`
- [ ] All environment variables configured:
  - [ ] `DATABASE_URL`
  - [ ] `SECRET_KEY` (generated with `openssl rand -hex 32`)
  - [ ] `POSTGRES_PASSWORD` (strong password)
  - [ ] `APIFY_API_TOKEN`
  - [ ] `GEMINI_API_KEY`
  - [ ] `ALLOWED_ORIGINS` (production domains)

### 3. Deployment
- [ ] Run `./deploy.sh`
- [ ] Select production mode (option 2)
- [ ] All containers started successfully
- [ ] Health check passes: `curl http://localhost:8000/health`

### 4. Verification
- [ ] API accessible at `http://server-ip:8000`
- [ ] Swagger docs accessible at `http://server-ip:8000/docs`
- [ ] Can register a new user
- [ ] Can login and receive token
- [ ] Can create a project
- [ ] Database persists data after restart
- [ ] Celery worker processing tasks

## Post-Deployment

### Security
- [ ] Changed all default passwords
- [ ] `.env` file permissions set to 600
- [ ] Firewall rules verified
- [ ] SSL certificate installed (production)
- [ ] HTTPS redirect configured (production)
- [ ] Security headers configured in Nginx
- [ ] Rate limiting enabled

### Domain & SSL (Production)
- [ ] Domain DNS propagated
- [ ] SSL certificate obtained (Let's Encrypt)
- [ ] Nginx configured for HTTPS
- [ ] HTTP to HTTPS redirect working
- [ ] Certificate auto-renewal configured

### Monitoring
- [ ] Health check endpoint working
- [ ] Log rotation configured
- [ ] Disk space monitoring set up
- [ ] Memory usage monitoring set up
- [ ] Uptime monitoring configured
- [ ] Error alerting configured

### Backup
- [ ] Database backup script created
- [ ] Automated daily backups scheduled
- [ ] Backup restoration tested
- [ ] Backup storage location configured
- [ ] Backup retention policy defined

### Documentation
- [ ] API documentation accessible
- [ ] Team members have access credentials
- [ ] Deployment process documented
- [ ] Rollback procedure documented
- [ ] Emergency contacts listed

## Testing

### Functional Tests
- [ ] User registration works
- [ ] User login works
- [ ] JWT authentication works
- [ ] Project creation works
- [ ] Meta tag generation works
- [ ] Link scanning works
- [ ] Competitor analysis works
- [ ] SERP comparison works

### Performance Tests
- [ ] API responds within acceptable time
- [ ] Can handle concurrent requests
- [ ] Database queries optimized
- [ ] No memory leaks detected
- [ ] CPU usage acceptable

### Security Tests
- [ ] SQL injection protection verified
- [ ] XSS protection verified
- [ ] CSRF protection verified
- [ ] Rate limiting working
- [ ] Authentication required for protected endpoints
- [ ] CORS configured correctly

## Maintenance

### Daily
- [ ] Check service status
- [ ] Review error logs
- [ ] Monitor disk space
- [ ] Verify backups completed

### Weekly
- [ ] Review API usage metrics
- [ ] Check for security updates
- [ ] Review and rotate logs
- [ ] Test backup restoration

### Monthly
- [ ] Update dependencies
- [ ] Review and optimize database
- [ ] Audit user access
- [ ] Review and update documentation
- [ ] Test disaster recovery plan

### Quarterly
- [ ] Rotate API keys
- [ ] Update SSL certificates (if not auto-renewed)
- [ ] Security audit
- [ ] Performance optimization review
- [ ] Cost optimization review

## Rollback Plan

### If Deployment Fails
1. [ ] Stop new containers: `docker-compose down`
2. [ ] Restore previous version from Git
3. [ ] Rebuild: `docker-compose build`
4. [ ] Start: `docker-compose up -d`
5. [ ] Verify health check
6. [ ] Restore database backup if needed

### Emergency Contacts
- **Server Provider Support**: _________________
- **Database Admin**: _________________
- **DevOps Lead**: _________________
- **Security Team**: _________________

## Sign-Off

### Deployment Team
- [ ] Developer: _________________ Date: _______
- [ ] DevOps: _________________ Date: _______
- [ ] Security: _________________ Date: _______
- [ ] QA: _________________ Date: _______

### Approval
- [ ] Technical Lead: _________________ Date: _______
- [ ] Project Manager: _________________ Date: _______

## Notes

_Add any deployment-specific notes, issues encountered, or special configurations here:_

---

**Deployment Status**: ⬜ Not Started | 🟡 In Progress | ✅ Complete

**Last Updated**: _________________

**Next Review Date**: _________________
