from Sudoku.data_sudoku import grid
from Sudoku.functions import get_neighbour, fitness_max, fitness_min
from charles.charles import Population, Individual
from charles.GA import GA
from operator import attrgetter
import numpy as np
import timeit
from charles.mutation import mutation,swap_mutation
from charles.selection import tournament, roulette, rank

sudoku_grid = grid

# define monkey patch of the charles functions
Individual.fitness = fitness_min
Individual.get_neighbours = get_neighbour

pop_size = 1000
optim_problem = 'min'


#initial population
pop = Population(
            size=pop_size,
            optim=optim_problem,
            grid=sudoku_grid
        )

#valida se nenhum dos individuos inicializados já é a solução final
solution = 0
flag_sucesso = False
if min(pop, key=attrgetter("fitness")).fitness == 0:
    flag_sucesso = True
    solution = min(pop, key=attrgetter("fitness"))

#fazer o loop para conseguir chegar a fitness igual a zero
count = 0
start = timeit.default_timer()
while flag_sucesso == False:
    
    #inicializa a nova população de offspring
    off_pop = Population(0,optim_problem,grid)
    
    #loop até a off_pop tiver o tamanho da parent pop
    while len(off_pop) < pop_size:
        off_pop.individuals.extend(GA(pop, 0.1, 0.5, selection_choice=tournament,mutation_choice=swap_mutation))
    
    #a população de offspring vira a nova parent population
    pop = off_pop

    #pega o indivíduo com o menor valor de fitness
    best_fit = min(pop, key=attrgetter("fitness"))

    print('count:', count,', Fitness ',best_fit.fitness)

    if pop.optim =='min' and best_fit.fitness==0:
        print(np.abs(best_fit.solution))
        print('count:', count)
        flag_sucesso = True
    elif pop.optim =='max' and best_fit.fitness==243:
        print(np.abs(best_fit.solution))
        print('count:', count)
        flag_sucesso = True

    count += 1

stop = timeit.default_timer()

print('Time: ', stop - start,'s')  