class FoodGenerator:
    def __init__ (self, x, y):
        self.x = x
        self.y = y


    def generate (self, x, y, lifetime):
        return Food(x, y, lifetime)


class Food:
    def __init__ (self, x, y, lifetime):
        self.x = x
        self.y = y
        self.lifetime = lifetime


    def decay (self):
        self.lifetime -= 1
