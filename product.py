from pydantic import BaseModel
class Product(BaseModel):
    name:str
    price:float
    instock:bool
raw={'name':"Shtmana PukhtoKhwa",'price':200,'instock':"True"}
p=Product(**raw)
print(p)