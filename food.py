class FoodGenerator:
    def __init__ (self, x, y):
        self.x = x
        self.y = y


    def generate (self, FOOD_RATE, FOOD_LIFE):
        for i in FOOD_RATE:




class Food:
    def __init__ (self, x, y, FOOD_LIFE):
        self.x = x
        self.y = y
        self.lifetime = FOOD_LIFE


    def decay (self):
        self.lifetime -= 1
