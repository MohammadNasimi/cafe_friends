from abc import ABC
from manager import DBManager

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


class Cashier(DBModel):
    TABLE = 'cashier'

    def __ini__(self, id, password, phone_number, email, first_name, last_name):
        self.id = id
        self.password = password
        self.phone_number = phone_number
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def login(cls, login_email, login_password):
        db = DBManager()
        all_cashier_object = db.read_all(Cashier)
        for i in all_cashier_object:
            if i.username == login_email and i.password == login_password:
                return True
        else:
            return False


    @classmethod
    def return_object_login(cls, cashier_id):
        db = DBManager()
        all_cashier_object = db.read_all(Cashier)
        for i in all_cashier_object:
            if i.id == cashier_id :
                return i
        else:
            return None

    def register(self):
        db = self.dm
        db.create(self)
