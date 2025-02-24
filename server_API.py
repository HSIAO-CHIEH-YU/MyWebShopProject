from fastapi import FastAPI
from fastAPI.user_API import router as user_router  # 用戶 API
from fastAPI.product_API import router as product_router  # 商品 API

# 創建 FastAPI 應用實例
app = FastAPI()

# 註冊用戶相關的 API 路由，並設定路徑前綴為 "/user"
app.include_router(user_router, prefix="/user", tags=["User"])

# 註冊商品相關的 API 路由，並設定路徑前綴為 "/product"
app.include_router(product_router, prefix="/product", tags=["Product"])

# 啟動應用程式的條件判斷
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
