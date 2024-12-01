import random
from typing import List, Callable
from knapsack import Knapsack

Genome = Knapsack
Population = List[Genome]
Fitness = Callable[[Genome], float]


def fitness(genome: Genome) -> int:
    """Determine how much a solution
    is good for our problem"""

    if genome.get_weight() > Knapsack.maximum_capacity:
        return 0

    return genome.get_value()


def generate_genome() -> Genome:
    """Generate a genome with random values"""

    genome = Genome(random.choices(
        population=[False, True], weights=[0.9, 0.1], k=Knapsack.n))

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


def crossover(parents: List[Genome]) -> List[Genome]:
    """Generate k genomes from two parents
    with random portion from each parent's dna"""

    cross_point = random.randrange(Knapsack.n)
    genomes = [Genome(parents[0].selected_items[:cross_point] +
                      parents[1].selected_items[cross_point:]),
               Genome(parents[1].selected_items[:cross_point] +
                      parents[0].selected_items[cross_point:])]

    return genomes


def mutation(genome: Genome) -> Genome:
    """Change point(s) is genome's dna to achieve variety"""

    points = random.randrange(5) if Knapsack.n > 5 else 1
    new_genome = Genome(genome.selected_items)

    for _ in range(points):
        index = random.randrange(Knapsack.n)
        new_genome.flip_item(index)

    return new_genome


def make_generation(population: Population, k: int) -> Population:
    """Make new generation based on current generation with k genomes"""

    generation = []
    for _ in range(k):
        parents = select_parents(population=population)
        genomes = crossover(parents=parents)
        generation += genomes

    generation = [mutation(genome) for genome in generation]
    return generation


def evolution() -> tuple[Knapsack, List[int]]:
    """Evolution function"""

    generation = generate_population(k=1200)
    result = generation[0]
    gen_fitness = []

    for gen in range(50):
        top_genomes = natural_selection(population=generation,
                                        k=100, fitness_func=fitness)
        best_genome = top_genomes[0]
        gen_fitness.append(fitness(best_genome))

        if fitness(best_genome) > fitness(result):
            result = best_genome

        print(f"Generation {gen}'s best solution is {fitness(best_genome)}")

        generation = make_generation(population=top_genomes, k=1200)

    return result, gen_fitness
