import random
from traits import traits

class Cell:
    def __init__ (self, name, x, y, energy=50, genes=''):
        self.name = name
        self.energy = energy
        self.genes = genes
        self.traits = []
        self.x = x
        self.y = y
        for trait in traits:
            if trait['genecode'] in self.genes:
                self.traits.append(trait)


    def divide (self, CELLS_COUNT, MUTATION_RATE, x, y):
        self.energy //= 2
        return Cell(CELLS_COUNT, x, y, self.energy//2, self.mutate(MUTATION_RATE))


    def mutate (self, MUTATION_RATE):
        genes = self.genes
        for i in range(len(genes)):
            rand = random.random()
            if rand <= MUTATION_RATE/3:
                genes = genes[:i] + str(random.choice([0,1,2,3])) + genes[i+1:]
            elif rand > MUTATION_RATE/3 and rand <= MUTATION_RATE*2/3:
                genes = genes[:i] + genes[i+1:]
            elif rand > MUTATION_RATE*2/3 and rand <= MUTATION_RATE:
                genes = genes[:i] + str(random.choice([0,1,2,3])) + genes[i:]
        return genes


    def update (self):
        energy_spent = 1
        for trait in self.traits:
            trait['action'](self.__dict__)
            energy_spent += trait['cost']
