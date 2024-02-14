import aioredis
from typing import Callable, Awaitable
from app.helpers.async_redis_decorator import async_redis_connection
from app.configuration.settings import REDIS_HOST


class RedisTools:
    __redis_connect = REDIS_HOST
    __redis_pool = None

    @classmethod
    async def get_redis_pool(cls) -> aioredis.Redis:
        if cls.__redis_pool is None:
            cls.__redis_pool = await aioredis.Redis.from_url(cls.__redis_connect)
        return cls.__redis_pool

    @classmethod
    @async_redis_connection
    async def set_key(cls, con: aioredis.Redis, key: str, value: str | int):
        await con.set(key, value)

    @classmethod
    @async_redis_connection
    async def get_key(cls, con: aioredis.Redis, key: str):
        return await con.get(key)

    @classmethod
    @async_redis_connection
    async def get_keys_pattern(cls, con: aioredis.Redis, pattern: str = '*'):
        return await con.keys(pattern=pattern)

    @classmethod
    @async_redis_connection
    async def delete_key(cls, con: aioredis.Redis, key: str):
        return await con.delete(key)

    @classmethod
    @async_redis_connection
    async def increment_key(cls, con: aioredis.Redis, key: str, amount: int = 1):
        return await con.incrby(key, amount)

    @classmethod
    @async_redis_connection
    async def expire_key(cls, con: aioredis.Redis, key: str, time: int = 60 * 60):
        return await con.expire(key, time)

    @classmethod
    @async_redis_connection
    async def add_to_list(cls, con: aioredis.Redis, list_key: str, value: str | list):
        return await con.rpush(list_key, value)

    @classmethod
    @async_redis_connection
    async def get_elements_from_list(cls, con: aioredis.Redis, list_key: str, start: int = 0, end: int = -1):
        return await con.lrange(list_key, start, end)

    @classmethod
    @async_redis_connection
    async def subscribe_to_channel(cls, con: aioredis.Redis, channel: str, callback: Callable[..., Awaitable]):
        pubsub = con.pubsub()
        await pubsub.subscribe(channel)
        async for message in pubsub.listen():
            callback(message)
