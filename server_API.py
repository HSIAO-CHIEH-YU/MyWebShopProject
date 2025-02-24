from fastapi import FastAPI
from fastAPI.user_API import user_router# 從 fastAPI 資料夾中引入用戶相關的 API 路由
from fastAPI.product_API import product_router# 從 fastAPI 資料夾中引入商品相關的 API 路由

# 創建 FastAPI 應用實例
app = FastAPI()

# 註冊用戶相關的路由到 FastAPI 應用中
# 這樣將 user_router 中的所有路由都加入到應用中
app.include_router(user_router)

# 註冊商品相關的路由到 FastAPI 應用中
# 這樣將 product_router 中的所有路由都加入到應用中
app.include_router(product_router)