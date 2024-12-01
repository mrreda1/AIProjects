import matplotlib.pyplot as plt
from knapsack import Knapsack
import genetic


n, Knapsack.maximum_capacity = map(int, input().split())

for _ in range(n):
    weight, value = map(int, input().split())
    Knapsack.add_item(weight=weight, value=value)

knapsack, y = genetic.evolution()
print(knapsack)

x = list(range(len(y)))
plt.scatter(x, y)
plt.show()
