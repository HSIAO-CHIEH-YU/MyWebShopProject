from fastapi import APIRouter
from pydantic import BaseModel
import mysqlPython # type: ignore

user_router=APIRouter()

class User(BaseModel):# 定義一個 Pydantic 數據模型類別，用來驗證傳入的請求數據
    username:str  # 定義用戶名欄位，並且指定為字串類型
    password:str  # 定義密碼欄位，並且指定為字串類型
    
@user_router.post("/register")#定義一個POST請求，用來處理用戶註冊
# 定義註冊函數，使用 async 是為了支持異步操作，這樣可以處理更多請求
async def register(user:User):# 路由接收來自請求的 user 資料（必須是符合 User 類別的格式）
    result=mysqlPython.add_user(user.username,user.password)
    if result=="註冊成功":
        return{"message":"註冊成功"}
    else:
        return{"message":result}

@user_router.post("/login")
async def login(user:User):
    result=mysqlPython.check_user(user.username,user.password)
    if result=="登入成功":
        return {"message":"登入成功"}
    else:
        return{"message":result}
    
# HTTP方法	作用	        適用場景
# GET	  取得資料	   查詢用戶、查詢商品清單
# POST	  新增資料	     註冊帳號、新增商品
# PUT	  更新整筆資料	修改帳號資料、更新商品資訊
# PATCH	  更新部分資料	部分修改密碼、改變商品價格
# DELETE  刪除資料	     刪除帳號、刪除商品

# GET 是無狀態的（stateless），它只用來查詢資料，不應該改變伺服器的狀態。
# POST 是有狀態的（stateful），它通常用來提交數據、觸發變更。


# from pydantic import BaseModel 是引入Pydantic庫中的BaseModel類別
# Pydantic 是一個Python庫，主要用來進行數據驗證和數據解析，尤其適用於與API請求和
# 回應的數據交互
# BaseModel是Pydantic中的一個基類，當你創建一個繼承自BaseModel的類時，它會自動
# 提供以下功能：

# 數據驗證：確保傳入的數據符合定義的類型（例如，str, int 等）。
# 如果數據不符合預期類型，Pydantic 會自動引發錯誤。

# 數據轉換：當數據傳遞進來時，Pydantic可以將數據轉換為所需的類型
# 例如，將字符串 "123" 轉換為整數 123。

# 數據序列化：當你需要將模型轉換為JSON格式時，Pydantic 
# 會自動處理序列化過程，生成適合JSON的結構。