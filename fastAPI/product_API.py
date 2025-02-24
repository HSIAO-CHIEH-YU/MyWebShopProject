from fastapi import APIRouter
from pydantic import BaseModel
from ..import mysqlPython

product_router=APIRouter

class Product(BaseModel):
    name:str
    price:float

@product_router.post("/add_product")
async def add_product(product:Product):
    mysqlPython.add_product(product.name,product.price)
    return{"message":f"商品:{product.name}以新增,售價為{product.price}元"}

@product_router.get("/show_products")
async def show_product():
    products=mysqlPython.show_products()
    return{"product":products}

