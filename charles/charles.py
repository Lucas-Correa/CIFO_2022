from scipy.spatial.distance import hamming
from statistics import mean
import numpy as np


class Individual:
    def __init__(self, grid):
        self.grid = grid
        self.sharing_fitness = 0
        self.solution = Individual.get_neighbours(self.grid)
        self.fitness = Individual.fitness(self.solution)
        # self.sf = Individual.shared_fitness(self.solution)  # sharing fitness pontuation

    def fitness(self, prob_sol):
        raise Exception("You need to monkey patch the fitness path.")

    def get_neighbours(self, **kwargs):
        raise Exception("You need to monkey patch the neighbourhood function.")

    # def shared_fitness(self, **kwargs):
    #     raise Exception("You need to monkey patch the shared fitness function.")

    def __repr__(self):
        return f"Individual: (matrix={self.solution}); Fitness: {self.fitness}"


class Population:
    def __init__(self, size, optim, grid, **kwargs):
        self.individuals = []
        self.size = size #tamanho da população
        self.optim = optim #tipo de problema
        self.grid = grid
        for i in range(size):
            self.individuals.append(
                Individual(grid = self.grid)
            )
    
    # def add_individuals(self,inds):

    #     self.individuals.extend(inds)

    #     var = self.variance()

    #     if self.optim == 'max':
    #         for i in self.individuals:
    #             i.fitness = i.fitness / (1-var)
    #     else:
    #         for i in self.individuals:
    #             #print(i.fitness)
    #             i.fitness = i.fitness / var

        
    #     return 1

    def variance(self):
        distances = []
        pop = self.individuals
        
        for i in range(len(pop)):
            distances.append(hamming(pop[0].solution.flatten(),pop[i].solution.flatten()))
        
        n = len(distances)
        x = mean(distances)

        dmax = max(distances)
        dmin = min(distances)

        normalized_distances = np.array([(x - dmin) / (dmax - dmin) for x in distances])
        normalized_distances = np.nan_to_num(normalized_distances)

        return round(1/(n-1) * (sum(normalized_distances-x))**2)

    
    def __len__(self):
        return len(self.individuals)

    def __getitem__(self, position):
        return self.individuals[position]

    def __repr__(self):
        return f"Population(size={len(self.individuals)})"


