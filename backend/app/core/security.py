import redis.asyncio as redis
from app.core.config import settings

redis_client = redis.from_url(settings.REDIS_URL, decode_responses=True)

async def check_rate_limit(ip: str) -> bool:
    """Simple IP-based rate limiting"""
    key = f"rate_limit:{ip}"
    current = await redis_client.get(key)
    
    if current and int(current) >= settings.RATE_LIMIT_PER_HOUR:
        return False
    
    if current:
        await redis_client.incr(key)
    else:
        await redis_client.setex(key, 3600, 1)  # 1 hour TTL
    
    return True
