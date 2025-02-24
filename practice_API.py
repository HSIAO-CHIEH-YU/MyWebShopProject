from fastapi import APIRouter
import practice_SQL  # 引入 practice_SQL.py，操作 MySQL 資料庫
from practice_models import User # type: ignore

router = APIRouter()

# 註冊用戶 API
@router.post("/register")
async def register(user: User):
    practice_SQL.add_user(user.username, user.password)
    return {"message": "註冊成功"}

# 登入用戶 API
@router.post("/login")
async def login(user: User):
    if practice_SQL.check_user(user.username, user.password):
        return {"message": "登入成功"}
    else:
        return {"message": "登入失敗"}
