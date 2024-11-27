from time import sleep
from board import GeneticBoard
import random
import math
from typing import List, Callable

Genome = GeneticBoard
Population = List[Genome]
FitnessFunc = Callable[[Genome], float]


def fitness(genome: Genome) -> float:
    """Determine the fitness of the genome"""

    if genome.threatens == 0:
        return math.inf

    return 1/genome.threatens


def generate_genome(k: int) -> Genome:
    """Generate genome with random values"""

    return Genome(random.choices(population=list(range(k)), k=k))


def generate_population(length: int, board_size: int) -> Population:
    """Generate random population with custom length"""

    return [generate_genome(k=board_size) for _ in range(length)]


def natural_selection(population: Population, k: int,
                      fitness_func: FitnessFunc) -> Population:
    """Select most suitable top k genomes"""

    population.sort(key=fitness_func, reverse=True)
    return population[:k]


def select_parents(population: Population) -> List[Genome]:
    """Select two parents for the new genomes"""

    return random.choices(population=population, k=2)


def crossover(parents: List[Genome]) -> List[Genome]:
    """Generate new genomes using two parents"""

    crossover_point = random.randrange(parents[0].size)

    return [GeneticBoard(parents[0].queens[:crossover_point]
                         + parents[1].queens[crossover_point:]),
            GeneticBoard(parents[1].queens[:crossover_point]
            + parents[0].queens[crossover_point:])]


def mutation(genome: Genome, k: int = 1) -> Genome:
    """Mutate a genome to make it unique"""

    indexes = random.choices(population=list(range(genome.size)), k=k)
    for index in indexes:
        choice = 0
        match genome.queens[index] + 1:
            case genome.size:
                choice = -1
            case 1:
                choice = 1
            case _:
                choice = random.choice([-1, 1])

        genome.queens[index] = genome.queens[index] + choice

    return Genome(genome.queens)


def make_generation(population: Population, k: int) -> Population:
    """Make new generation from current generation"""

    generation = []
    for _ in range(k//2):
        parents = select_parents(population=population)
        generation += crossover(parents=parents)

    for i, _ in enumerate(generation):
        generation[i] = mutation(generation[i], k=random.randrange(
            0, math.ceil(population[0].size / 1.8)))

    return generation


def is_good_enough(solution: Genome) -> bool:
    """Determine if a solution is good enough"""

    if fitness(solution) == math.inf:
        return True

    return False


def run(n: int):
    """Driver function"""

    gen_size = 10000
    population = generate_population(length=gen_size, board_size=n)
    best_solution = 0
    last = 0
    identical = 0
    for i in range(1000):
        population = natural_selection(
            population=population, k=gen_size//10, fitness_func=fitness)

        best_solution = population[0]

        print("\033[H\033[2J")
        print(f"Generation {i}'s best solution is {
              fitness(best_solution)}")
        print(best_solution)

        if is_good_enough(best_solution):
            return

        if last != fitness(best_solution):
            identical = 0
            last = fitness(best_solution)

        identical += 1

        if identical > 60:
            print("\033[H\033[2J")
            print("Add new population to next Generation")
            population = generate_population(1999 * gen_size // 2000, n) \
                + make_generation(population=population,
                                  k=math.ceil(gen_size/2000))
            identical = 1
            sleep(3)
        else:
            population = make_generation(population=population, k=gen_size)
    print(best_solution)
