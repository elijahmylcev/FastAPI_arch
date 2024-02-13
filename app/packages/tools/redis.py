import aioredis
from typing import Callable, TypeVar, Awaitable
import functools

T = TypeVar('T')


def async_redis_connection(method: Callable[..., Awaitable[T]]) -> Callable[..., Awaitable[T]]:
    @functools.wraps(method)
    async def wrapper(cls, *args, **kwargs):
        redis_pool = await cls.get_redis_pool()
        async with redis_pool as con:
            return await method(cls, con, *args, **kwargs)

    return wrapper


class RedisTools:
    __redis_connect = 'redis://localhost:6379'
    __redis_pool = None

    @classmethod
    async def get_redis_pool(cls) -> aioredis.Redis:
        if cls.__redis_pool is None:
            cls.__redis_pool = await aioredis.Redis.from_url(cls.__redis_connect)
        return cls.__redis_pool

    @classmethod
    @async_redis_connection
    async def set_key(cls, con: aioredis.Redis, pair: str, value: str | int):
        print(con)
        await con.set(pair, value)

    @classmethod
    @async_redis_connection
    async def get_key(cls, con: aioredis.Redis, pair: str):
        return await con.get(pair)

    @classmethod
    @async_redis_connection
    async def get_keys_pattern(cls, con: aioredis.Redis, pattern: str = '*'):
        return await con.keys(pattern=pattern)
