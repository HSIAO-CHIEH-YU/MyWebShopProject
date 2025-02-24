# 引入 FastAPI 的 APIRouter，來建立路由
from fastapi import APIRouter
# 引入 sql.py，處理資料庫操作
from ..import mysqlPython  

# 創建一個 APIRouter 實例，用來組織我們的API端點
router = APIRouter()

# 註冊一個 POST 路由，當用戶呼叫 "/add" 時，執行此函數
@router.post("/add")#post提交資料
async def add_product(product_name: str, price: float):
    # 呼叫 sql.py 中的 add_product 函數來新增商品，處理成功與失敗的顯示訊息
    message = mysqlPython.add_product(product_name, price)
    return {"message": message}

# 註冊一個 GET 路由，當用戶呼叫 "/list" 時，執行此函數
@router.get("/list")#get獲取資料
async def list_products():
    # 呼叫 show_products() 獲取商品列表
    products = mysqlPython.show_products()
    return {"products": products}

