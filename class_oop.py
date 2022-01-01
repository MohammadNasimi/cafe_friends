import psycopg2
import psycopg2.extras
from psycopg2._psycopg import connection, cursor

class food:
    def __init__(self, _id, name, category, price, count):
        self._id = _id
        self.name = name
        self.category = category
        self.price = price
        self.count = count

    @classmethod
    def show_food(cls):
        pass

    @classmethod
    def food_price(cls):
        pass

    @classmethod
    def add_food(cls):
        pass

    @classmethod
    def change_food(cls):
        pass

    @classmethod
    def remove_food(cls):
        pass

    @classmethod
    def change_count_food(cls):
        pass

    @classmethod
    def price_food(cls):
        pass

    @classmethod
    def is_available_food(cls):
        pass


class desk():
    def __init__(self, _id, status, order, customer):
        self._id = _id
        self.status = status
        self.order = order
        self.customer = customer

    @classmethod
    def status_desk(cls):
        pass

    @classmethod
    def order_desk(cls):
        pass

    @classmethod
    def customer_desk(cls):
        pass


class order():
    def __init__(self, _id, foods_counts, status, total_price, final_price, paid):
        self._id = _id
        self.foods_counts = foods_counts
        self.status = status
        self.total_price = total_price
        self.final_price = final_price
        self.paid = paid

    @classmethod
    def define_order(cls):
        pass

    @classmethod
    def change_order(cls):
        pass

    @classmethod
    def calculate_total_price_order(cls):
        pass

    @classmethod
    def calculate_final_price_order(cls):
        pass

    @classmethod
    def get_status_order(cls):
        pass

    @classmethod
    def change_status_price_order(cls):
        pass

    @classmethod
    def get_paid_order(cls):
        pass

    @classmethod
    def is_paid_order(cls):
        pass


# need progress
class Status():
    def __init__(self, _id, name):
        self._id = _id
        self.name = name

    @classmethod
    def get_name(cls):
        pass


class Customer():
    def __init__(self, cookie, count):
        self.cookie = cookie
        self.count = count

    @classmethod
    def get_cookie_customer(cls):
        pass

    @classmethod
    def get_count_customer(cls):
        pass

#progess !!!!!
class Cashier():
    def __init__(self, _id, user_name, password, phone_number, email, first_name, last_name):
        self._id = _id
        self.user_name = user_name
        self.password = password
        self.phone_number = phone_number
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def login(cls, login_user_name, login_password):
        con = psycopg2.connect(
            host="http://castor.db.elephantsql.com",
            database="emuobeum",
            user="emuobeum",
            password="sPxAPxjlHoFajruESmVmv7UN8x0-a4ST"
        )
        cur = con.cursor()
        cur.execute("select id, user_name, password from cashier")
        rows = cur.fetchall()
        con.close
        for i in rows:
            if i[1] == login_user_name:
                if i[2] == login_password:
                    return Cashier.make_object_login(i[0])
            else:
                return False

    @classmethod
    def make_object_login(cls, cashier_id):
        con = psycopg2.connect(
            host="http://castor.db.elephantsql.com",
            database="emuobeum",
            user="emuobeum",
            password="sPxAPxjlHoFajruESmVmv7UN8x0-a4ST"
        )
        cur = con.cursor()
        cur.execute(f'select id, user_name, password , phone_number, email, first_name, last_name from cashier '
                    f'where id == {cashier_id}')
        row = cur.fetchall()
        con.close
        return Cashier(row[0][0], row[0][1], row[0][2], row[0][3], row[0][4], row[0][5], row[0][6])

    @classmethod
    def register(cls, id, user_name, password, phone_number, email, first_name, last_name):
        con = psycopg2.connect(
            host="http://castor.db.elephantsql.com",
            database="emuobeum",
            user="emuobeum",
            password="sPxAPxjlHoFajruESmVmv7UN8x0-a4ST"
        )
        cur = con.cursor()
        cur.execute(f'INSERT INTO cashire(id, user_name, password, phone_number, email, first_name, last_name)'
                    f'VALUES ({id}, {user_name}, {password}, {phone_number}, {email}, {first_name}, {last_name})')


