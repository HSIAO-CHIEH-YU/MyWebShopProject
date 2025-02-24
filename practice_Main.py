from fastapi import FastAPI
from pydantic import BaseModel
import practice_API  # 引入 practice_API.py
from practice_models import User # type: ignore

app = FastAPI()

# 註冊請求資料格式
class User(BaseModel):
    username: str
    password: str

# 註冊端點
@app.post("/register")
async def register(user: User):
    practice_API.register(user)  # 呼叫 practice_API.py 中的註冊函式
    return {"message": "註冊成功"}

# 可以在這裡添加更多的 API 路由
