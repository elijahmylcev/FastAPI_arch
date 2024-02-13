from fastapi import APIRouter, BackgroundTasks
from app.packages.tools.redis import RedisTools
from fastapi.responses import JSONResponse
from pprint import pprint

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


def callback_function(message):
    pprint(f"Принято сообщение: {message}")


@router.get("/subscribe_to_channel")
async def subscribe_to_channel(background_tasks: BackgroundTasks, channel: str):
    try:
        background_tasks.add_task(RedisTools.subscribe_to_chanel, channel, callback_function)

        return JSONResponse(content={"message": f"Подписались на {channel}"})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
