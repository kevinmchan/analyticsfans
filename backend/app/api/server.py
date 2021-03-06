from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ..core import config, predictions

from .routes import router as api_router


def get_application():
    app = FastAPI(
        title=config.PROJECT_NAME,
        version=config.VERSION,
        openapi_url="/api/openapi.json",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.add_event_handler("startup", predictions.create_start_app_handler(app))
    app.add_event_handler("shutdown", predictions.create_stop_app_handler(app))

    app.include_router(api_router, prefix="/api")

    return app


app = get_application()
