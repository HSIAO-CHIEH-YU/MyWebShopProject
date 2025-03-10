from fastapi import APIRouter
from pydantic import BaseModel
import mysqlPython  # type: ignore

product_router=APIRouter()

class Product(BaseModel):
    name:str
    price:float
    have:int

class updateProduct(BaseModel):
    old_name:str
    new_name:str

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

@product_router.delete("/delete_product")
async def delete_product(product_name:str):
    result=mysqlPython.delete_product(product_name)
    if result=="商品不存在":
        return{"message":f"商品:{product_name}不存在"}
    else:
        return{"message":f"商品:{product_name}已刪除"}
    
@product_router.put("/update_product")
async def update_product(product:Product):
    result=mysqlPython.update_product(product.name,product.have,product.price)
    if "不存在" in result:
        return{"message":result}
    else:
        return{"message":f"商品:{product.name}已更新,單價為{product.price}元,庫存為{product.have}"}
    
@product_router.put("/update_product_name")
async def update_product_name(updateproduct:updateProduct):
    result=mysqlPython.update_product_name(updateproduct.old_name,updateproduct.new_name)
    if "不存在" in result:
        return{"message":result}
    else:
        return{"message":f"商品:{updateproduct.old_name}已更新為{updateproduct.new_name}"}