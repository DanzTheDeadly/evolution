from array import array
import random

class Cell:
    def __init__ (self, name, x, y, energy=50, genes=array('i', (0,0,0,0,0))):
        self.name = name
        self.energy = energy
        self.genes = genes
        self.x = x
        self.y = y

    def divide (self, CELLS_COUNT, MUTATION_RATE):
        self.energy //= 2
        return Cell(CELLS_COUNT, self.energy//2, self.mutate(MUTATION_RATE), self.x+1, self.y+1))

    def mutate (self, MUTATION_RATE):
        genes = self.genes
        rand = random.random()
        for i in range(len(genes)):
            if rand <= MUTATION_RATE/3:
                genes(i) = random.choice(0,1,2,3)
            elif rand > MUTATION_RATE/3 and rand <= MUTATION_RATE*2/3:
                genes.remove(i)
            elif rand > MUTATION_RATE*2/3 and rand <= MUTATION_RATE:
                genes.insert(random.choice(0,1,2,3))
        return genes
