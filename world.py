from cell import Cell
from food import FoodGenerator
import random

class World:
    def __init__ (self, config):
        self.MUTATION_RATE = config['MUTATION_RATE']
        self.CELLS_COUNT = config['START_CELLS']
        self.FOOD_COUNT = config['START_FOOD']
        self.FOOD_LIFE = config['FOOD_LIFE']
        self.FOOD_RATE = config['FOOD_RATE']
        self.SUN_RATE = config['SUN_RATE']
        self.MAP_SIZE = config['MAP_SIZE']

        self.time = 0
        self.cells = [Cell(cnt, random.randint(0, self.MAP_SIZE['WIDTH']-1), random.randint(0, self.MAP_SIZE['HEIGHT']-1), genes='00011') for cnt in range(self.CELLS_COUNT)]
        self.map = [['.' for i in range(self.MAP_SIZE['WIDTH'])] for i in range(self.MAP_SIZE['HEIGHT'])]
        self.food = [FoodGenerator(random.randint(0, self.MAP_SIZE['WIDTH']-1), random.randint(0, self.MAP_SIZE['HEIGHT']-1)) for i in range(self.FOOD_COUNT)]
        for cell in self.cells:
            self.map[cell.y][cell.x] = '0'
        for foodgen in self.food:
            self.map[foodgen.y][foodgen.x] = 'F'


    def update (self, frames):
        for i in range(frames):
            for cell in self.cells:
                cell.update()
                if cell.energy <= 0:
                    self.cells.remove(cell)
                elif cell.energy >= 50:
                    free_space = [
                        (cell.y-1, cell.x-1),
                        (cell.y-1,   cell.x),
                        (cell.y-1, cell.x+1),
                        (cell.y,   cell.x-1),
                        (cell.y,   cell.x+1),
                        (cell.y+1, cell.x-1),
                        (cell.y+1,   cell.x),
                        (cell.y+1, cell.x+1)
                    ]
                    while free_space:
                        new_loc = random.choice(free_space)
                        try:
                            free_space.remove(new_loc)
                            if self.map[new_loc[0]][new_loc[1]] == '.':
                                self.cells.append(cell.divide(self.CELLS_COUNT+1, self.MUTATION_RATE, x=new_loc[1], y=new_loc[0]))
                                self.CELLS_COUNT += 1
                                self.map[new_loc[0]][new_loc[1]] = '0'
                                break
                        except:
                            continue
            self.time += 1


    def show (self):
        for line in self.map:
            print(''.join(line))
