from fastapi import APIRouter

router: APIRouter = APIRouter(
    prefix='/api/v1'
)


@router.get('/test')
def get_test():
    return {
        'test_field': 'test_field'
    }
