import array
import random
import numpy as np
import pandas as pd
from deap import algorithms, base, creator, tools

pesos="promedios_educacion_sexual.csv"

df_pesos=pd.read_csv(pesos)

fuentes={"promedios_discriminacion_padres.csv",
"promedios_discriminacion_genero.csv",
"promedios_discriminacion_infancia.csv",
"promedios_discriminacion_adolecencia.csv",
"promedios_discriminacion_12_meses.csv",
}

for f in fuentes:
    df_datos = pd.read_csv(f)
    valores=df_datos.to_numpy
    pd_pesos=df_pesos.to_numpy

    IND_SIZE = len(df_datos.columns)

    pesos=np.dot(pd_pesos,-1.0)

    creator.create("FitnessMin", base.Fitness, weights=np.array(pesos))
    creator.create("Individual", array.array, typecode='i', fitness=creator.FitnessMin)

    toolbox = base.Toolbox()

    toolbox.register("indices", random.sample, range(IND_SIZE), IND_SIZE)

    toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    def eval(individual):
        distance = valores[individual[-1]][individual[0]]
        for gene1, gene2 in zip(individual[0:-1], individual[1:]):
            distance += valores[gene1][gene2]
        return distance,

    toolbox.register("mate", tools.cxPartialyMatched)
    toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
    toolbox.register("select", tools.selTournament, tournsize=3)
    toolbox.register("evaluate", eval)

    def salida():
        random.seed(169)

        pop = toolbox.population(n=300)

        hof = tools.HallOfFame(1)
        stats = tools.Statistics(lambda ind: ind.fitness.values)
        stats.register("avg", np.mean)
        stats.register("std", np.std)
        stats.register("min", np.min)
        stats.register("max", np.max)
    
        GEN=50

        algorithms.eaSimple(pop, toolbox, 0.7, 0.2, GEN, stats=stats, 
                        halloffame=hof)
    
        return pop, stats, hof

    salida()
