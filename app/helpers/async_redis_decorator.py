from typing import Callable, TypeVar, Awaitable
import functools

T = TypeVar('T')


def async_redis_connection(method: Callable[..., Awaitable[T]]) -> Callable[..., Awaitable[T]]:
    """
       Декоратор для обеспечения асинхронного подключения к Redis перед выполнением метода.

       Параметры:
       - method: Асинхронный метод, который требует подключения к Redis.

       Возвращает обертку вокруг переданного метода, которая обеспечивает подключение к Redis
       из пула и передает подключение в качестве первого аргумента методу.
       """

    @functools.wraps(method)
    async def wrapper(cls, *args, **kwargs):
        redis_pool = await cls.get_redis_pool()
        async with redis_pool as con:
            return await method(cls, con, *args, **kwargs)

    return wrapper
