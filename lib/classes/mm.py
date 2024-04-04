class Customer:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self._name 
    
    def set_name(self, value):
        if type(value) == str and 1 < len(value) < 16:
            self._name = value
    
    name = property(get_name,set_name)
        
    def orders(self):
        pass
    
    def coffees(self):
        pass
    
    def create_order(self, coffee, price):
        pass


class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

    
class Coffee:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self._name

    def set_name(self, value):
        if hasattr(self, "_name"):
            raise AttributeError()
        elif type(value) == str and len(value)>= 3:
            self._name = value
            
    name = property(get_name, set_name)   

    def orders(self):
        pass
    
    def customers(self):
        pass
    
    def num_orders(self):
        pass
    
    def average_price(self):
        pass