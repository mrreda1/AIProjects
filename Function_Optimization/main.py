import random
from math import inf
from typing import List, Callable
import matplotlib.pyplot as plt

Genome = List[float]
Population = List[Genome]
Fitness = Callable[[Genome], float]


def equation(x: float, y: float, z: float) -> float:
    """The function that we want
    to optimize a solution for"""

    return 9 * x**3 + 12 * y**2 + z - 25


def fitness(genome: Genome) -> float:
    """Determine how much a solution
    is good for our problem"""

    x, y, z = genome
    ans = equation(x, y, z)
    if ans == 0:
        return inf
    return abs(1/ans)


def generate_genome() -> Genome:
    """Generate a genome with random values"""

    genome = [random.uniform(0, 10000) for _ in range(3)]
    return genome


def generate_population(k: int) -> Population:
    """Make generation 0 with k genomes"""

    generation = [generate_genome() for _ in range(k)]
    return generation


def natural_selection(population: Population, k: int,
                      fitness_func: Fitness) -> Population:
    """Select best k solution from a
       generation based on genomes' fitness"""

    population.sort(key=fitness_func, reverse=True)

    if k > len(population) or k <= 0:
        return population

    return population[:k]


def select_parents(population: Population) -> List[Genome]:
    """Select two parents from a population"""

    parents = random.choices(population=population, k=2)
    return parents


def crossover(parents: List[Genome], k: int) -> List[Genome]:
    """Generate k genomes from two parents
    with random portion from each parent's dna"""

    genomes = []
    for _ in range(k):
        genome = [parents[random.choice([0, 1])][i] for i in range(3)]
        genomes.append(genome)

    return genomes


def mutation(genome: Genome) -> Genome:
    """Change point(s) is genome's dna to achieve variety"""

    genome = [value * random.uniform(0.99, 1.01) for value in genome]
    return genome


def make_generation(population: Population, k: int) -> Population:
    """Make new generation based on current generation with k genomes"""

    generation = []
    genomes_from_parents = 3
    for _ in range(k // genomes_from_parents):
        parents = select_parents(population=population)
        genomes = crossover(parents=parents, k=genomes_from_parents)
        generation += genomes

    generation = [mutation(genome) for genome in generation]
    return generation


def is_good_enough(genome: Genome, goal: int,
                   fitness_func: Fitness) -> bool:
    """Check if generation's best genome
    is good enough for our problem"""

    if fitness_func(genome) >= goal:
        return True

    return False


def evolution(fitness_func: Fitness, goal: int) -> List[float]:
    """Evolution function"""

    gen = 0
    generation = generate_population(k=1200)
    gen_fitness = []
    while True:
        top_genomes = natural_selection(population=generation,
                                        k=100, fitness_func=fitness)
        best_genome = top_genomes[0]
        gen_fitness.append(fitness_func(best_genome))

        print(f"Generation {gen}'s best solution is {
              fitness_func(best_genome)}, {best_genome}")

        if is_good_enough(genome=best_genome, goal=goal,
                          fitness_func=fitness):
            return gen_fitness

        gen += 1
        generation = make_generation(population=top_genomes, k=1200)


def main():
    """Driver function"""

    y = evolution(fitness_func=fitness, goal=200000)
    x = list(range(len(y)))
    plt.scatter(x, y)
    plt.show()


if __name__ == '__main__':
    main()
