import os


# def get_cache(cache_type="NONE"):
def get_cache(cache_type=None):
    if cache_type == None:
        cache_type = os.environ.get("PBL_CACHE")
    if cache_type == "REDIS":
        from . import redis_cache as cache
    elif cache_type == "LEVELDB":
        from . import leveldb_cache as cache
    else:
        from . import nocache as cache

    print("cache", cache.name)
    return cache
