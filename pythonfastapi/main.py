from fastapi import HTTPException

from fastapi import FastAPI

from database import User, Product, Category, database as connection

from schemas import UserRequestModel, ProductRequestModel, CategoryRequestModel
from schemas import ProductResponseModel






app = FastAPI(
    tittle='ApiBsale',
    description='Api de productos tipo "Tienda Virutal" en FastApi',
    version='1.0.1'
)

posts = []


#events
@app.on_event('startup')
def startup():
    if connection.is_closed():
        connection.connect()

@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()



#pathoperation
@app.get('/product/{product_name}')
def get_product(product_name):
    print('=============================')
    product = Product.select().where(Product.name == product_name)
    if product:
        return ProductResponseModel(
            id = product.id,
            name = product.name,
            url_image=product.url_image,
            price=product.price,
            discount=product.discount,
            category=product.category
)
    else:
        return HTTPException(404, 'No se encuentra el producto')
   


# @app.get('/posts')
# async def get_posts():
#     return posts

# @app.get('/about')
# async def get_about():
#     return {"About":"test"}


# @app.post('/')
# async def create_user(user: UserRequestModel):
#     user = models.User.create(
#         username=user.username,
#         email=user.email
#     )
#     return 'Nuevo Usuario creado 😎'