from pydantic import BaseModel


class UserRequestModel(BaseModel):
    username: str
    email: str

# class UserResponseModel(BaseModel):
#     username: str
#     email: str

class ProductRequestModel(BaseModel):
    name: str 
    url_image: str
    price: float
    discount: float
    category: int

class ProductResponseModel(ProductRequestModel):
    id: int
    name: str 
    url_image: str
    price: float
    discount: float
    category: int


class CategoryRequestModel(BaseModel):
    id: int
    name: str 

# class CategoryResponseModel(BaseModel):
#     id: int
#     name: str 