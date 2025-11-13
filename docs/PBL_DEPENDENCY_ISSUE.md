# Missing PBL Library - Critical Dependency Issue

## Overview

The Smarter Playlists application depends on a custom `pbl` (Playlist Builder Library) that is **not included** in this repository. This is a critical dependency that must be resolved for the application to function.

## Impact

The following files import and depend on `pbl`:
- `server/compiler.py`
- `server/components.py`
- `server/plugs.py`
- `server/mixer.py`
- `server/program_manager.py`
- `server/tests.py`
- `server/flask_server.py` (optional import)
- `server/cherrypy_server.py`

## What is PBL?

Based on code analysis, `pbl` appears to be a custom playlist manipulation library that provides:

1. **Core Components:**
   - `pbl.PushableSource` - Track source management
   - `pbl.Concatenate` - Combining multiple track sources
   - `pbl.Conditional` - Conditional logic for playlists
   - `pbl.AttributeRangeFilter` - Filtering tracks by attributes
   - `pbl.Dumper` - Debug output
   - `pbl.PBLException` - Custom exceptions
   - `pbl.tlib` - Track library functions
   - `pbl.engine` - Execution engine

2. **Spotify Integration:**
   - `pbl.spotify_plugs` - Spotify-specific functionality
   - `pbl.PlaylistSource` - Loading tracks from Spotify playlists

## Resolution Options

### Option 1: Locate the Original Library
Contact the original author (@plamere) or check for:
- Separate repository for `pbl`
- Python package installation
- Vendor directory in older versions of this project

### Option 2: Stub Implementation (Temporary)
Create a minimal stub implementation to allow the app to start:

```python
# server/pbl_stub.py
"""
Minimal stub implementation of pbl library
This is NOT functional - just allows imports to work
"""

class PBLException(Exception):
    pass

class Conditional:
    def __init__(self, func, true_source, false_source):
        pass

class PushableSource:
    def __init__(self, source):
        pass

class Concatenate:
    def __init__(self, sources):
        pass

class AttributeRangeFilter:
    def __init__(self, source, attr, match=None, min_val=None, max_val=None):
        pass

# Add to each affected file:
# try:
#     import pbl
# except ImportError:
#     import pbl_stub as pbl
```

### Option 3: Reimplement from Scratch
Based on the usage patterns, create a new implementation:
- Extract interfaces from current code
- Implement using Spotipy directly
- Focus on core playlist manipulation features

## Recommended Actions

1. **Immediate:** Search for `pbl` in:
   - Author's GitHub repositories
   - PyPI package index
   - Archive.org for old versions of this project
   - Original Smarter Playlists releases

2. **Short-term:** Create stub to allow development on other components

3. **Long-term:** Consider reimplementing as open-source library

## Related Issue: pyen (Echo Nest)

Similarly, `pyen` (Echo Nest Python library) is also missing but less critical:
- Echo Nest API was shut down in 2016
- Already commented out in recent fixes
- Features should be replaced with Spotify Audio Features API

## Contact

If you have access to the original `pbl` library or know where to find it, please:
- Open an issue in this repository
- Contact the maintainers
- Share the library source or installation instructions
