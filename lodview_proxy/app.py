from fastapi import FastAPI

from lodview_proxy import settings, routes


def create_app():
    app = FastAPI(title=settings.LODVIEW_PROXY_TITLE)
    app.include_router(routes.api_v1.router, prefix='/api/v1')
    app.include_router(routes.general.router, prefix='')

    return app
