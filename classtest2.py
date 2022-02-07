class Phone:
    def __init__(self, model, is_touch, size, price):
        self.model = model
        self.is_touch = is_touch
        self.size = size
        self.price = price

    def is_toutchabel(self):
        if self.is_touch:
            return True
        else:
            return False
    def price(self):
        return self.price
    
class Tablet(Phone):
    def __init__(self, model, is_touch, size, color):
        self.model = model
        self.is_touch = is_touch
        self.size = size
        self.color = color
        
    
    