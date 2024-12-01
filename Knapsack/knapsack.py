from collections import namedtuple
from typing import List

Item = namedtuple('Item', ['weight', 'value'])


class Knapsack:
    n = 0
    maximum_capacity = 0
    availabe_items: List[Item] = []

    def __init__(self, selected_items):
        self._weight = 0
        self._value = 0
        self.selected_items = selected_items[:]

        self._calculate_weights()

    def _calculate_weights(self):
        """Calculate total weight of selected items in the knapsack"""

        for i, take in enumerate(self.selected_items):
            self._weight += Knapsack.availabe_items[i].weight * take
            self._value += Knapsack.availabe_items[i].value * take

    def flip_item(self, index):
        """Take or drop an item in the knapsack"""

        item = Knapsack.availabe_items[index]
        sign = -1 if self.selected_items[index] else 1

        self._weight += item.weight * sign
        self._value += item.value * sign
        self.selected_items[index] = not self.selected_items[index]

    def change_quantity(self, index, take):
        """Change how much should i take an item"""

        if index < 0 or take < 0 or index >= Knapsack.n:
            return

        item = Knapsack.availabe_items[index]
        quantity = take - self.selected_items[index]

        self._weight += item.weight * quantity
        self._value += item.value * quantity
        self.selected_items[index] = take

    def get_weight(self):
        """Get total weight"""

        return self._weight

    def get_value(self):
        """Get total value"""

        return self._value

    @staticmethod
    def add_item(value: int, weight: int):
        """Add new item to available items"""

        Knapsack.availabe_items.append(Item(weight=weight, value=value))
        Knapsack.n += 1

    def __repr__(self) -> str:
        """How the knapsack object should be printed"""

        result = f"Weight: {self._weight}\nValue: {self._value}\nTaken items: "
        for i, take in enumerate(self.selected_items):
            if take > 1:
                result += f"{i + 1}({self.selected_items[i]}) "
            elif take:
                result += f"{i + 1} "

        return result
