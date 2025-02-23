# 引入 FastAPI 應用程式
from fastapi import FastAPI
import uvicorn

# 從 main.py 中導入 app 物件，app 物件在 main.py 中已經設定了路由
from main import app  # 假設 main.py 和 server.py 在同一層目錄

if __name__ == "__main__":
    # 使用 uvicorn 啟動 FastAPI 伺服器，host 設定為 '127.0.0.1'，port 設定為 8000
    uvicorn.run(app, host="127.0.0.1", port=8000)
