# Smarter Playlists v3.0 (2025-11-13)

This release completes the Python 3 modernization and hardens deployment.

Highlights

- Python 3.11+ runtime, updated dependencies
- Flask backend health endpoint: GET /healthz
- Environment-driven configuration via .env (python-dotenv)
- Redis 5 client usage in Scheduler and services
- Optional Nginx for static hosting + proxy to backend
- Docker Compose stack with health checks
- Frontend now reads web/config.json for API base URL and OAuth redirect URIs
- Test runner updated for Python 3 (test/run.py)

Notes

- Echo Nest-era libraries (pyen) remain optional; some features may be limited
- Legacy “v2” frontend files have been removed. Primary UI is under web/*.html + main.js. Old bookmarks to go2.html and v2 scripts are redirected at the web server.

Upgrade steps

1) Copy .env.example to .env and set Spotify credentials
2) Copy web/config.example.json to web/config.json and adjust API paths/redirect URIs
3) Use Docker Compose (recommended): `docker-compose up -d` and visit <http://localhost:8000>

Thanks to all contributors and users who kept Smarter Playlists going!
