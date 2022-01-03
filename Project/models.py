from abc import ABC
import datetime as dt


class DBModel(ABC):  # abstract base Database model
    TABLE: str  # table name
    PK: str  # primary key column of the table

    def __str__(self) -> str:
        return f"<{self.__class__.__name__} {vars(self)}>"


class MenuItems(DBModel):  # Menu items model
    TABLE = 'menu_items'  # TABLE NAME
    PK = 'id'  # PRIMARY KEY FOR TABLE

    def __init__(self, name: str, price: int, serving_time_period: str, estimated_cooking_time: int, id: int = None):
        self.name = name
        self.price = price
        self.serving_time_period = serving_time_period
        self.estimated_cooking_time = estimated_cooking_time
        if id:
            self.id = id

    def __repr__(self):
        return f"<menuItem_class {self.id}:{self.name}>"


class Status(DBModel):
    TABLE = 'status'
    PK = 'id'

    def __init__(self, status: str, id: int = None):
        self.status = status

        if id:
            self.id = id

    def __repr__(self):
        return f"<Status_class {self.id}:{self.status}>"





























class Order:
    TABLE = 'orders'
    PK = 'id'

    def __init__(self, table_id: int, menu_item: int, count: int = 1, id: int = None):
        self.table_id = table_id
        self.menu_item = menu_item
        self.count = count

        if id:
            self.id = id

    def __repr__(self):
        return f'<Order_Class {self.id}:{self.menu_item}>'


class Receipt:
    TABLE = 'receipts'
    PK = 'id'

    def __init__(self, orders: list, total_price: int, id: int = None):
        self.orders = orders
        self.total_price = total_price
        if id:
            self.id = id

    def __repr__(self):
        return f"<Class_Receipt id_{self.id}:{self.orders}||Price: {self.total_price}>"
