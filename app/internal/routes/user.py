from fastapi import APIRouter

router: APIRouter = APIRouter(
    prefix='/api/v1'
)


@router.get('/user')
def get_user():
    return {
        'user': 'hello user'
    }
