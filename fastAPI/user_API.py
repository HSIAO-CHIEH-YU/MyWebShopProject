# 引入 FastAPI 的 APIRouter 用來定義 API 路由
from fastapi import APIRouter
from ..import mysqlPython#從父目錄導入用來處理資料庫操作

# 創建一個 APIRouter 實例，用來組織我們的API端點
router = APIRouter()

# 註冊用戶的 API 路由
@router.post("/register")
async def register_user(username: str, password: str):# async def 可以讓函式變成非同步執行，避免等待，提高執行效率！
    # 調用 sql 模組中的 add_user 方法來新增用戶
    message = mysqlPython.add_user(username, password)  # 使用 sql 中的 add_user 方法處理資料庫邏輯
    return {"message": message}  # 直接將 sql 回傳的訊息回傳給使用者

# 登入用戶的 API 路由
@router.post("/login")
async def login_user(username: str, password: str):
    # 調用 sql 模組中的 check_user 方法來驗證用戶的帳號密碼
    message = mysqlPython.check_user(username, password)  # 使用 sql 中的 check_user 方法處理資料庫邏輯
    return {"message": message}  # 直接將 sql 回傳的訊息回傳給使用者


# HTTP方法	作用	        適用場景
# GET	  取得資料	   查詢用戶、查詢商品清單
# POST	  新增資料	     註冊帳號、新增商品
# PUT	  更新整筆資料	修改帳號資料、更新商品資訊
# PATCH	  更新部分資料	部分修改密碼、改變商品價格
# DELETE  刪除資料	     刪除帳號、刪除商品

# GET 是無狀態的（stateless），它只用來查詢資料，不應該改變伺服器的狀態。
# POST 是有狀態的（stateful），它通常用來提交數據、觸發變更。