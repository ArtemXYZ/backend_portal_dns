"""
    Главный исполнительный файл.
"""

# ---------------------------------- Импорт стандартных библиотек
# ---------------------------------- Импорт сторонних библиотек
from fastapi import FastAPI  # , Body
from pydantic import EmailStr, BaseModel
import uvicorn

# from sqlalchemy.types import *
# -------------------------------- Локальные модули
from api import router as api_router
from configs.config_api import settings
# ----------------------------------------------------------------------------------------------------------------------
app = FastAPI()
app.include_router(api_router, prefix=settings.api.prefix)


# ======================================================================================================================
class CreateUsers(BaseModel):
    email: EmailStr


@app.get("/")
async def test():
    return {'0': 'Test good'}


@app.get("/tests/")
async def rest2():
    return ['10', 'Test good 2']


@app.get("/{rr_id}/")
async def rest3(rr_id: int):
    return {'4': rr_id + 2}


@app.post("/user/")
async def create_user(email: CreateUsers):  # EmailStr = Body()
    return {
        'msg': 'success',
        'email': email.email
    }


if __name__ == '__main__':
    uvicorn.run("main:app", host=settings.run.host, port=settings.run.port, reload=True)
