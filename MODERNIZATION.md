# Modernization Checklist

## ✅ Completed

- [x] Created `requirements.txt` with Python 3.11+ dependencies
- [x] Created `package.json` for Node.js dependency management
- [x] Created `.env.example` for environment configuration
- [x] Fixed Flask-CORS deprecated import (`flask.ext.cors` → `flask_cors`)
- [x] Fixed werkzeug deprecated import (`werkzeug.contrib.fixers` → `werkzeug.middleware.proxy_fix`)
- [x] Fixed ConfigParser import (Python 3: `configparser`)
- [x] Converted Python 2 print statements to Python 3 across all files
- [x] Updated `.gitignore` with modern Python and Node.js patterns
- [x] Created `Dockerfile` for containerized deployment
- [x] Created `docker-compose.yml` for orchestration
- [x] Created comprehensive new README with modern setup instructions

## 🚧 In Progress / Next Steps

### High Priority

- [ ] **Test all Python files** - Verify print statement conversions work correctly
- [ ] **Update simplejson → json** - Replace `import simplejson as json` with `import json`
- [ ] **Add environment variable loading** - Use `python-dotenv` in Flask server
- [ ] **Update Redis connection** - Add proper error handling and connection pooling
- [ ] **Fix any remaining Python 2/3 compatibility issues**
  - Check for `unicode()` usage
  - Check for `.iteritems()` (should be `.items()`)
  - Check for `xrange()` (should be `range()`)
  - Check for division operator issues

### Medium Priority

- [ ] **Frontend Modernization**
  - [ ] Update jQuery 1.11.1 → 3.7+
  - [ ] Update Bootstrap 3 → Bootstrap 5
  - [ ] Replace Underscore.js with native ES6 or Lodash
  - [ ] Add build process (Vite configuration)
  - [ ] Convert to ES6 modules
  - [ ] Add proper error handling

- [ ] **Security Improvements**
  - [ ] Remove hardcoded client IDs from JavaScript
  - [ ] Add CSRF protection
  - [ ] Implement rate limiting
  - [ ] Add Content Security Policy headers
  - [ ] Update all HTTP URLs to HTTPS
  - [ ] Add Subresource Integrity (SRI) for CDN resources

- [ ] **Code Quality**
  - [ ] Add type hints to Python code
  - [ ] Configure Black, isort, flake8
  - [ ] Add ESLint configuration
  - [ ] Add Prettier configuration
  - [ ] Set up pre-commit hooks

### Lower Priority

- [ ] **Testing Infrastructure**
  - [ ] Set up pytest
  - [ ] Write unit tests for core functionality
  - [ ] Add integration tests
  - [ ] Set up code coverage reporting
  - [ ] Add CI/CD pipeline (GitHub Actions)

- [ ] **Documentation**
  - [ ] Add API documentation (OpenAPI/Swagger)
  - [ ] Create architecture diagrams
  - [ ] Add inline code documentation
  - [ ] Create troubleshooting guide
  - [ ] Add deployment guide

- [ ] **Features & Improvements**
  - [ ] Add WebSocket support for real-time updates
  - [ ] Implement proper JWT authentication
  - [ ] Add logging infrastructure
  - [ ] Add monitoring/observability
  - [ ] Performance optimization

## 🔍 Files That Need Review

### Python Files (Check for Python 2 patterns)
- [ ] `server/components.py` - Large file, check for dict.iteritems(), unicode()
- [ ] `server/compiler.py` - Check for encoding issues
- [ ] `server/mixer.py` - Verify conversion
- [ ] `server/plugs.py` - Verify conversion
- [ ] `server/program_manager.py` - Check Redis usage patterns

### JavaScript Files (Modernization needed)
- [ ] `web/main.js` - Convert to ES6
- [ ] `web/editor.js` - Convert to ES6, update Raphael.js usage
- [ ] `web/program.js` - Modernize
- [ ] `web/playlist.js` - Modernize

### Configuration Files
- [ ] `nginx/smarterplaylists` - Add HTTPS redirect, update proxy settings
- [ ] `redis/redis.conf` - Review for security best practices
- [ ] Create `nginx/nginx.conf` for Docker setup

## 🐛 Potential Issues to Address

1. **Echo Nest API** - API was shut down, need to find alternatives or remove functionality
2. **Spotipy version** - May need to update API calls for latest Spotipy version
3. **Custom libraries** - `pbl` and `pyen` may need Python 3 updates
4. **Database/Storage** - `kvstore.py` uses simple file system, consider upgrading
5. **Authentication flow** - May need updates for current Spotify OAuth requirements

## 📋 Testing Checklist

After making changes, test:

- [ ] Flask server starts without errors
- [ ] Redis connection works
- [ ] Spotify authentication flow works
- [ ] Can create a simple playlist
- [ ] Can save a program
- [ ] Can load a saved program
- [ ] Scheduled playlists work
- [ ] All example playlists work
- [ ] Docker compose setup works

## 📝 Notes

- The conversion script modified 14 Python files successfully
- Some complex print statements may need manual review
- All deprecated imports have been fixed
- Docker setup is ready but needs testing with actual Spotify credentials
- Frontend still uses legacy libraries - complete modernization is a larger effort

## 🎯 Quick Wins (Can Do Now)

1. Test the current setup with `docker-compose up`
2. Replace simplejson with standard json library
3. Add python-dotenv loading to flask_server.py
4. Update client IDs to be loaded from environment
5. Test one simple playlist creation end-to-end
