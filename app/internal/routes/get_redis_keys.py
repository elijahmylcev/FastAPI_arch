from fastapi import APIRouter
from app.packages.tools.redis import RedisTools

router = APIRouter(
    prefix='/api/v1/redis'
)


@router.get('/get_all')
async def get_all():
    return await RedisTools.get_keys_pattern()


@router.get('/set_keys')
async def set_key(key, value=None):
    if key:
        return await RedisTools.set_key(key, value)


@router.get('/get_key')
async def get_key(key):
    return await RedisTools.get_key(key)
