from app.internal.schemas.currency import Symbols
from app.packages.tools.redis import RedisTools
from app.configuration.settings import CURRENCY_PAIR_KEY, ALL_CURRENCY_PAIRS_KEYS

import aiohttp


async def on_startup():
    async with aiohttp.ClientSession() as session:
        async with session.get(ALL_CURRENCY_PAIRS_KEYS) as response:
            symbols = [symbol.symbol for symbol in Symbols(**await response.json()).symbols]
            for symbol in symbols[:20]: await RedisTools.set_key(symbol, 0)


async def on_loop_startup():
    for symbol in await RedisTools.get_keys_pattern():
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{CURRENCY_PAIR_KEY}{symbol.decode("utf-8")}') as response:
                response_json = await response.json()
                await RedisTools.set_key(symbol, response_json['price'])
