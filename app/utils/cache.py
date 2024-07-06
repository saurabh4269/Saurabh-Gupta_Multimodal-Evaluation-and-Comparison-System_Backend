from redis import Redis
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

def init_cache():
    redis = Redis(host='localhost', port=6379)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
