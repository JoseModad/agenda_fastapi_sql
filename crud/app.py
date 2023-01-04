# Fastapi

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Starlette

from starlette.responses import RedirectResponse 


from .routes.routes import agenda

from .config.config import engine

from .models import models

models.Base.metadata.create_all(bind = engine)


description = """
Practice Schedule
Jose Anibal Modad
"""

app = FastAPI(
    title = "Schedule",
    description = description,
    version = 1
)

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_methods = ["*"],
    allow_headers = ["*"],
    allow_credentials = True,    
)

app.include_router(agenda)

@app.get("/")
def main():
    return RedirectResponse(url = "/docs/")
    