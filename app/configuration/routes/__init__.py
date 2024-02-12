from app.configuration.routes.register_routes import Routes
from app.internal import routes

__routes__ = Routes(routers=tuple(routes.__all__))
