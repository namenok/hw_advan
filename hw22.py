from pydantic.v1 import BaseModel, validator, Field, root_validator, EmailStr

class Book(BaseModel):
    b_name: str
    author: str
    pages_amount: int
    year: int

class Library(BaseModel):
    l_name: str
    adress: str
    email: EmailStr
    books: list[Book]
    books_amount: int

    @root_validator(pre=True)
    def root(cls, values: dict) ->dict:
        count_bo = len(values['books'])
        values['books_amount'] = count_bo
        return values


data = {
    'b_name': 'design',
    'author': 'daniel',
    'pages_amount': 80,
    'year': 2024,
    'l_name': 'bigLib',
    'adress': 'MainStr',
    'email': 'afhj@g.com',
    'books':['bo', 'Hints', 'Vo'],
}

res_book_and_lib = Library(**data)
print(res_book_and_lib.json())


#-------------------домашня-----------------
from pydantic.v1 import BaseModel, validator, Field, root_validator, constr, EmailStr
from datetime import date
import re #бібліотека для регулярних виразів ( я для себе це коментую )


class Product(BaseModel):
    prod_id: constr(regex=r'^PRD-\d{4}$')
    pr_name: str
    category: str
    price: int
    quantity_available: int

    @validator('prod_id', pre=True)
    def check_pr_id(cls, val):
        try:
            re.compile(val)
            return val
        except re.error:
            print("Non valid regex pattern")
            exit()

class Customer(BaseModel):
    client_id: constr(regex=r'^CRD-\d{4}$')
    cl_name: str
    email: EmailStr
    list_of_orders: list[Product]

    @validator('email')
    def check(cls, val):
        try:
            re.compile(val)
            return val
        except re.error:
            return f'Non valid regex pattern'


    @validator('client_id', pre=True)
    def check_cl_id(cls, val):
        try:
            re.compile(val)
            return val
        except re.error:
            return f'Non valid regex pattern'


class OrderItem(BaseModel):#містить посилання на продукт та кількість (в наявності)
    product_link: Product
    quantity_available_link: #я не знаю як послатись на квантіті_амаунт в класе продукта


class Order(BaseModel):
    order_id: constr(regex=r'^ORD-\d{4}$')
    order_date: date
    client: Customer
    products_list_in_class_order: list[Product]
    status: str #тут через валідатор буду перевіряти -"нове", "в обробці", "відправлено", "доставлено"

    @validator('order_id', pre=True)
    def check_or_id(cls, val):
        try:
            re.compile(val)
            return val
        except re.error:
            print("Non valid regex pattern")
            exit()

    @validator('status', pre=True)
    def check_status(cls, value)->str:
        if value == 'new':
            value = 'in processing'
            return value
        elif value == 'in processing':
            value = 'sent'
            return value
        elif value == 'sent':
            value = 'delivered'
            return value


    @root_validator(pre=True)
    def check_minimal_symm(cls, values: dict) -> dict:
        total = sum(product.price * product.quantity_available for product in products_list_in_class_order)
        if total < 50:
            raise ValueError('Minimal order is 50')
        return values