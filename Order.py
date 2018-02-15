class Order:
    def __init__(self):
        self.__order_number = ""
        self.__price = 0
        self.__date = ""
        self.cart = []

    def get_grand_total(self):
        for item in self.cart:
            # add each item in list together


class Product(Order):
    def __init__(self, pc, pd, pp, co, si, ge):
        Order.__init__(self)
        self.__product_code = pc
        self.__product_desc = pd
        self.__product_price = pp
        self.__color = co
        self.__size = si
        self.__gender = ge

    def get_product_code(self):
        return self.__product_code

    def get_product_desc(self):
        return self.__product_desc

    def get_product_price(self):
        return self.__product_price

    def get_product_color(self):
        return self.__color

    def get_product_size(self):
        return self.__size

    def get_gender(self):
        return self.__gender


class Hat(Product):
    pass


class Garment(Product):
    pass


class Shoes(Product):
    pass


class OrderLine(Order):
    def __init__(self):
        Order.cart = []
        self.quantity = 0
        self.tax = 0.0875

    def get_total(self, total_price):
        return total_price + total_price * self.tax


class Customer(Order):
    def __init__(self):
        Order.__init__(self)
        self.__firstname = ""
        self.__lastname  = ""
        self.__customer_id = ""
        self.__customer_email = ""

    def set_first_name(self, fn):
        self.__firstname = fn

    def set_last_name(self, ln):
        self.__lastname = ln

    def get_name(self):
        return self.__firstname + " " + self.__lastname

    def get_customer_id(self):
        return self.__customer_id

    def set_customer_id(self, custid):
        self.__customer_id = custid

    def get_customer_email(self):
        return self.__customer_email

    def set_customer_email(self, email):
        self.__customer_email = email

    def get_customer_info(self):
        return self.get_name() + "\n" + self.get_customer_email()


class Address(Customer):
    def __init__(self):
        Customer.__init__(self)
        self.__unit_street = ""
        self.__city = ""
        self.__zip_code = ""
        self.__country = ""

    def get_unit_street(self):
        return self.__unit_street

    def set_unit_street(self, street):
        self.__unit_street = street

    def get_city(self):
        return self.__city

    def set_city(self, city):
        self.__city = city

    def get_zip_code(self):
        return self.__zip_code

    def set_zip_code(self, z_code):
        self.__zip_code = z_code

    def get_country(self):
        return self.__country

    def set_country(self, country):
        self.__country = country

    def get_address(self):
        return "\n" + self.get_name() + "\n" + self.get_unit_street() + "\n" + self.get_city() + " " + self.get_zip_code() + "\n" + self.get_country()
