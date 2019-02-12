from cell import Cell

class World:
    def __init__ (self, config):
        self.MUTATION_RATE = config['MUTATION_RATE']
        self.CELLS_COUNT = config['START_CELLS']
        self.FOOD_COUNT = config['START_FOOD']
        self.FOOD_RATE = config['FOOD_RATE']
        self.SUN_RATE = config['SUN_RATE']
        self.MAP_SIZE = config['MAP_SIZE']

        self.CELLS = [Cell(cnt, 50, random.randint(0, self.MAP_SIZE['WIDTH']), random.randint(0, self.MAP_SIZE['HEIGHT'])) for cnt in range(self.CELLS_COUNT)]


    def update (self, frames):
        pass
