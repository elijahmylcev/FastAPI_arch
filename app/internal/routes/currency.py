from fastapi import APIRouter
from app.packages.tools.redis import RedisTools
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix='/api/v1/currency'
)


@router.get('/{currency_pair}')
async def get_currency_pair(currency_pair: str):
    if currency_pair not in [key.decode('utf-8') for key in await RedisTools.get_keys_pattern()]:
        return JSONResponse(content={
            'error': 'This currency pair does not exists'
        }, status_code=500)

    return {
        'currency_pair': currency_pair,
        'price': await RedisTools.get_key(str(currency_pair))
    }
