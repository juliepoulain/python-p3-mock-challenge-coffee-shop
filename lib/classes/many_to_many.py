class Coffee:
    def __init__(self, name):
        self.name = name
        
    def orders(self):
        return [order for order in Order.all if order.coffee is self]
    
    def customers(self):
        return list({order.customer for order in Order.all if order.coffee is self})
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        prices = [order.price for order in Order.all if order.coffee is self]
        return sum(prices)/len(prices)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if hasattr(self, "_name"):
            raise Exception("Coffee name cannot be changed.")
        if not isinstance(name, str):
            raise Exception("Coffee name must be a string.")
        if len(name) < 3:
            raise Exception("Coffen name must be greater than 2 characters.")
        else:
            self._name = name
    

class Customer:

    all = []

    def __init__(self, name):
        self.name = name
        self.__class__.all.append(self)
        
    def orders(self):
        return [order for order in Order.all if order.customer is self]
    
    def coffees(self):
        return list({order.coffee for order in Order.all if order.customer is self})
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
    def spent_on(self, coffee):
        return sum([order.price for order in Order.all if (order.customer is self and order.coffee is coffee)])

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        if not 1 <= len(name) <= 15:
            raise Exception("Name must be between 1 and 15 characters")
        else:
            self._name = name

    @classmethod
    def most_aficionado(cls, coffee):
       return max(cls.all, key=lambda customer: customer.spent_on(coffee))
    
class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        self.__class__.all.append(self)
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if hasattr(self, "_price"):
            raise Exception("Price cannot be changed")
        if not isinstance(price, float):
            raise Exception("Price must be a float")
        if not 1 <= price <= 10:
            raise Exception("Price must be between 1 and 10")
        else:
            self._price = price 


# Tests exceptions
# coffee = Coffee(name="blah")
# try:
#     coffee.name = "test"
# except Exception as e:
#     print(e.__str__())