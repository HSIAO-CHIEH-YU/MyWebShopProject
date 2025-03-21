from fastapi import APIRouter
from pydantic import BaseModel
import mysqlPython  # type: ignore
from typing import Optional

product_router=APIRouter()

class Product(BaseModel):
    name:str
    price:Optional[float]=None
    have:Optional[int]=None
    new_name:Optional[str]=None

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

@product_router.delete("/delete_product/{product_name}")
async def delete_product(product_name:str):
    result=mysqlPython.delete_product_b(product_name)
    if result=="商品不存在":
        return{"message":f"商品:{product_name}不存在"}
    else:
        return{"message":f"商品:{product_name}已刪除"}
    
@product_router.put("/update_product/{name}")
async def update_product(name: str, product: Product):
    result = mysqlPython.update_product_details_by_name(name,new_name=product.new_name,new_price=product.price,new_have=product.have)
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