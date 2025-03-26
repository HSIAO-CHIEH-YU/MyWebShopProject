from fastapi import APIRouter
from pydantic import BaseModel
import mysqlPython  # type: ignore
from typing import Optional

product_router=APIRouter()

class Product(BaseModel):
    new_name:Optional[str]=None
    name:Optional[str]=None
    price:Optional[float]=None
    have:Optional[int]=None
    
@product_router.post("/add_product")
async def add_product(product:Product):
    result=mysqlPython.add_product(product.name,product.price,product.have)
    if result=="商品已存在":
        return{"message":f"商品:{product.name}已存在"}
    else:
        return{"message":f"商品:{product.name}以新增,售價為{product.price}元,庫存數量有{product.have}個"}

@product_router.get("/show_products")
async def show_product():
    products=mysqlPython.show_products()
    return{"products":products}

@product_router.delete("/delete_product/{product_id}")
async def delete_product(product_id: int):
    result = mysqlPython.delete_product_by_id(product_id)  # 修改為根據 ID 刪除
    if "不不存在" in result:  # 根據錯誤訊息判斷商品是否不存在
        return {"message": f"商品 ID: {product_id} 不存在"}
    else:
        return {"message": f"商品 ID: {product_id} 已刪除"}

@product_router.put("/update_product_name/{product_id}")
async def update_product_name(product_id: int, product: Product):
    result = mysqlPython.update_product_name_by_id(product_id, product.new_name)  # 修改為根據 ID 更新名稱
    return {"message": result}

@product_router.get("/show_cart")
async def show_cart(user_id:int):
    result=mysqlPython.show_cart(user_id)
    return result

@product_router.delete("/delete_cart")
async def delete_cart(user_id:int,product_id:int):
    result=mysqlPython.delete_from_cart(user_id,product_id)
    return result

@product_router.post("/buy_cart")
async def buy_cart(user_id:int):
    result=mysqlPython.buy(user_id)
    return {"message":result}