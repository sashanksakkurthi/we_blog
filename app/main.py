from fastapi import FastAPI
from .authentication import auth_router
from .router import create_user
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(create_user.router)
app.include_router(auth_router.router)


@app.get("/")
async def index():
    return {"Working"}
