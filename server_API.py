from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastAPI.user_API import user_router# 從 fastAPI 資料夾中引入用戶相關的 API 路由
from fastAPI.product_API import product_router# 從 fastAPI 資料夾中引入商品相關的 API 路由
#user_router--->user_API裡面的user_router=APIRouter()
#product_router--->product_API裡面的product_router=APIRouter()
# 創建 FastAPI 應用實例
app = FastAPI()

# 設定 CORS 策略，允許特定來源的請求
#不然google不允許不同來源的請求
# CORSMiddleware 是 FastAPI 提供的中間件，用來處理跨來源請求（CORS）的問題
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 設置為 "*" 代表允許來自所有域的請求
    allow_credentials=True,
    allow_methods=["*"],  # 允許所有的 HTTP 方法（GET, POST, PUT, DELETE 等）
    allow_headers=["*"],  # 允許所有的請求標頭
)

# 註冊用戶相關的路由到 FastAPI 應用中
# 這樣將 user_router 中的所有路由都加入到應用中
app.include_router(user_router)

# 註冊商品相關的路由到 FastAPI 應用中
# 這樣將 product_router 中的所有路由都加入到應用中
app.include_router(product_router)