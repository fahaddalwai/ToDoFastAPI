from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import models, routers
from db import engine
from config import settings

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


origins = [] + settings.cors_origin_whitelist

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """ Root route """
    return {"message": "This is my first FastApi Project! Hope you enjoy it"}

app.include_router(routers.router)