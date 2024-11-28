import random
import math
from typing import List, Callable

Genome = List[float]
Population = List[Genome]
FitnessFunc = Callable[[Genome], float]


def foo(x, y, z) -> float:
    """The function that we want to optimize"""

    return 9 * x**3 + 3 * y**2 + 12 * z


def fitness(genome: Genome) -> float:
    """Determine the fitness of the genome"""

    ans = foo(genome[0], genome[1], genome[2])
    if ans == 0:
        return math.inf

    return abs(1/ans)


def generate_genome() -> Genome:
    """Generate genome with random values"""

    return [random.uniform(0, 10000) for _ in range(3)]


def generate_population(length: int) -> Population:
    """Generate random population with custom length"""

    return [generate_genome() for _ in range(length)]


def natural_selection(population: Population, k: int,
                      fitness_func: FitnessFunc) -> Population:
    """Select most suitable top k genomes"""

    population.sort(key=fitness_func, reverse=True)
    return population[:k]


def select_parents(population: Population) -> List[Genome]:
    """Select two parents for the new genomes"""

    return random.choices(population=population, k=2)


def crossover(parents: List[Genome], k: int) -> List[Genome]:
    """Generate new genomes using two parents"""

    children = []
    for _ in range(k):
        genome = [parents[random.choice([0, 1])][i] for i in range(3)]
        children.append(genome)

    return children


def mutation(genome: Genome) -> Genome:
    """Mutate a genome to make it unique"""

    for i, _ in enumerate(genome):
        genome[i] = genome[i] * random.uniform(0.99, 1.01)

    return genome


def make_generation(population: Population) -> Population:
    """Make new generation from current generation"""

    generation = []
    for _ in range(400):
        parents = select_parents(population=population)
        generation += crossover(parents=parents, k=3)

    for i, _ in enumerate(generation):
        generation[i] = mutation(generation[i])

    return generation


def is_good_enough(solution: Genome) -> bool:
    """Determine if a solution is good enough"""

    if fitness(solution) > 20000:
        return True

    return False


def main():
    """Driver function"""

    gen = 0
    population = generate_population(length=1200)
    while True:
        population = natural_selection(
            population=population, k=100, fitness_func=fitness)

        best_solution = population[0]

        print(f"Generation {gen}'s best solution is {
              fitness(best_solution)}, {best_solution}")

        if is_good_enough(best_solution):
            return

        gen += 1
        population = make_generation(population=population)


if __name__ == "__main__":
    main()
