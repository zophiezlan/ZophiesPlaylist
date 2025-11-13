# Smarter Playlists 🎵

A web application for creating complex, automated Spotify playlists with a visual graph-based interface.

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## ⚡ Quickstart (TL;DR)

```bash
# 1) Clone
git clone https://github.com/zophiezlan/ZophiesPlaylist.git
cd ZophiesPlaylist

# 2) Configure
cp .env.example .env
cp web/config.example.json web/config.json
# Edit both files with your values (Spotify client ID/secret, redirect URIs)

# 3) Run with Docker (recommended)
docker-compose up -d

# 4) Open the app
# Visit http://localhost:8000 (frontend), API at http://localhost:5000
```

## ✨ Features

- **Visual Playlist Builder**: Create complex playlists using a graph-based UI
- **Multiple Sources**: Combine music from artists, albums, genres, and existing playlists
- **Smart Filtering**: Filter tracks by audio features, popularity, release date, and more
- **Automation**: Schedule playlists to update automatically
- **Spotify Integration**: Seamless connection to your Spotify account

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher
- Node.js 18+ (for frontend development)
- Redis server
- Spotify Developer Account ([Create one here](https://developer.spotify.com/dashboard))

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/zophiezlan/ZophiesPlaylist.git
   cd ZophiesPlaylist
   ```

2. **Set up Python environment**

   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # Windows:
   venv\Scripts\activate
   # Linux/Mac:
   source venv/bin/activate
   
   # Install dependencies
   pip install -r requirements.txt
   ```

3. **Configure environment variables**

   ```bash
   # Copy the example environment file
   cp .env.example .env
   
   # Edit .env and add your Spotify credentials
   # Get these from https://developer.spotify.com/dashboard
   ```

4. **Start Redis**

   ```bash
   # Windows (if installed via MSI):
   redis-server
   
   # Linux/Mac:
   redis-server
   
   # Or use the provided script:
   cd redis
   ./start-redis
   ```

5. **Run the development server**

   ```bash
   cd server
   python flask_server.py
   ```

6. **Frontend configuration (optional but recommended)**
    - Copy the example config and adjust values as needed:

       ```bash
       cp web/config.example.json web/config.json
       ```

    - This file lets you override the frontend API base path and OAuth redirect URIs without editing JS files.

7. **Access the application**
   - Open your browser to `http://localhost:8000`
   - The API runs on `http://localhost:5000`

### 🐳 Docker Setup (Recommended)

The easiest way to run the application is using Docker:

```bash
# Copy environment file (Linux/macOS)
cp .env.example .env
# Windows PowerShell equivalent:
Copy-Item .env.example .env

# Optional: Frontend config (Linux/macOS)
cp web/config.example.json web/config.json
# Windows PowerShell equivalent:
Copy-Item web/config.example.json web/config.json

# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

Access the application at `http://localhost:8000`

If you need to change the frontend API base URL or redirect URIs in Docker, edit `web/config.json` before starting the stack.

## 📁 Project Structure

```text
├── server/              # Python backend (Flask)
│   ├── flask_server.py  # Main Flask application
│   ├── components.py    # Playlist component definitions
│   ├── compiler.py      # Playlist program compiler
│   ├── spotify_auth.py  # Spotify authentication
│   └── ...
├── web/                 # Frontend (HTML/CSS/JavaScript)
│   ├── index.html       # Main application page
│   ├── main.js          # Application logic
│   ├── editor.js        # Visual editor
│   └── examples/        # Example playlists
├── redis/               # Redis configuration
├── nginx/               # Nginx configuration
├── requirements.txt     # Python dependencies
├── package.json         # Node.js dependencies
└── docker-compose.yml   # Docker orchestration
```

## 🔧 Development

### Backend Development

```bash
# Activate virtual environment
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Run with debug mode
cd server
FLASK_DEBUG=True python flask_server.py

# Run tests
python tests.py
```

### Frontend Development

```bash
# Install Node dependencies
npm install

# Start development server with hot reload
npm run dev

# Build for production
npm run build

# Lint code
npm run lint
```

### Code Quality

```bash
# Format Python code
black server/

# Lint Python code
flake8 server/

# Format JavaScript
npm run format

# Type checking (if using TypeScript)
npm run type-check
```

## 🔐 Environment Variables

Key environment variables (see `.env.example` for full list):

```bash
# Spotify API Credentials
SPOTIPY_CLIENT_ID=your_client_id
SPOTIPY_CLIENT_SECRET=your_client_secret
SPOTIPY_REDIRECT_URI=http://localhost:8000/callback.html

# Redis Configuration
REDIS_HOST=localhost
REDIS_PORT=6379

# Flask Configuration
FLASK_ENV=development
FLASK_DEBUG=True
```

### Frontend Config (web/config.json)

The frontend reads `web/config.json` at startup to set API paths and OAuth redirect URIs. Copy `web/config.example.json` to `web/config.json` and adjust as needed.

```json
{
   "apiLocalPath": "http://localhost:5000/SmarterPlaylists/",
   "apiRemotePath": "https://smarterplaylists.playlistmachinery.com/SmarterPlaylists/",
   "localRedirectUri": "http://localhost:8000/callback.html",
   "remoteRedirectUri": "https://smarterplaylists.playlistmachinery.com/callback.html",
   "localAuthRedirectUri": "http://localhost:8000/auth.html",
   "remoteAuthRedirectUri": "https://smarterplaylists.playlistmachinery.com/auth.html",
   "clientId": ""
}
```

## 📚 API Documentation

The application exposes several API endpoints:

- `GET /SmarterPlaylists/inventory` - Get available components
- `POST /SmarterPlaylists/save` - Save a playlist program
- `POST /SmarterPlaylists/run` - Execute a playlist program
- `POST /SmarterPlaylists/delete` - Delete a saved program
- `GET /healthz` - Lightweight health endpoint for liveness checks

See also: [MIGRATION_SUMMARY.md](./MIGRATION_SUMMARY.md) and [MODERNIZATION.md](./MODERNIZATION.md) for full context of changes.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Migration Notes (2021 → 2025)

This project has been updated from Python 2 to Python 3.11+ with the following major changes:

- ✅ Python 2 → Python 3 syntax migration
- ✅ Updated all dependencies to latest versions
- ✅ Added Docker support for easy deployment
- ✅ Modern Flask-CORS integration
- ✅ Environment-based configuration
- ✅ Updated .gitignore for Python 3 and Node.js
- 🚧 Frontend modernization (in progress)
- 🚧 TypeScript migration (planned)
- 🚧 Testing infrastructure (planned)

See [RELEASE_NOTES.md](./RELEASE_NOTES.md) for the latest release highlights and upgrade steps.

## 🛠️ Troubleshooting

- Health checks: `GET /healthz` returns 200 when the backend is healthy.
- Docker logs: `docker-compose logs -f backend` and `docker-compose logs -f nginx` help diagnose startup issues.
- OAuth redirect mismatch: Ensure `SPOTIPY_REDIRECT_URI` in `.env` matches the URIs in `web/config.json` and in your Spotify Dashboard.

## 🐛 Known Issues

- Some Echo Nest features may no longer work (API was deprecated)
- Frontend uses older JavaScript libraries (jQuery, Bootstrap 3)
- Custom `pbl` and `pyen` libraries may need updates

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

Created by [@plamere](http://twitter.com/plamere)

## 🙏 Support

For support, visit the [SmarterPlaylists Google Group](https://groups.google.com/forum/#!forum/smarterplaylists)

## 🔗 Links

- [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
- [Spotify Web API Documentation](https://developer.spotify.com/documentation/web-api/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Redis Documentation](https://redis.io/documentation)

---

**Note**: This is an updated version (v3.0) of the original Smarter Playlists application, migrated to Python 3 and modernized for 2025 standards.
