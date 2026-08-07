from pydantic import BaseModel, Field


class Market(BaseModel):
    id: int
    name: str


class Product(BaseModel):
    name: str
    price: float = Field(..., gt=0, description = "Цена должна быть больше 0" )
    market: Market = Field(...)

product_data = {
        "name": "Phone",
        "price": 499.99,
        "tags": ["electronics", "smartphone"],
        "market": {
            "id": 1,
            "name": "Amazon"
        }
    }

product = Product(**product_data)
print(product.market.name)
print(product.price)

new_product = Product(name='Phone',price=499.99,market=Market(id=1,name="Amazon"))
print(new_product)