from fastapi_limiter import FastAPILimiter
from redis import Redis

def init_rate_limiter(app):
    redis = Redis(host='localhost', port=6379)
    FastAPILimiter.init(redis, app=app)
