from collections import namedtuple
from typing import List

Item = namedtuple('Item', ['weight', 'value'])


class Knapsack:
    n = 0
    maximum_capacity = 0
    availabe_items: List[Item] = []

    def __init__(self, selected_items: List[bool]):
        self.__weight = 0
        self.__value = 0
        self.selected_items = selected_items[:]

        self.__calculate_weights()

    def __calculate_weights(self):
        """Calculate total weight of selected items in the knapsack"""

        for i, take in enumerate(self.selected_items):
            if take:
                self.__weight += Knapsack.availabe_items[i].weight
                self.__value += Knapsack.availabe_items[i].value

    def flip_item(self, index):
        """Take or drop an item in the knapsack"""

        item = Knapsack.availabe_items[index]
        sign = -1 if self.selected_items[index] else 1

        self.__weight += item.weight * sign
        self.__value += item.value * sign
        self.selected_items[index] = not self.selected_items[index]

    def get_weight(self):
        """Get total weight"""

        return self.__weight

    def get_value(self):
        """Get total value"""

        return self.__value

    @staticmethod
    def add_item(value: int, weight: int):
        """Add new item to available items"""

        Knapsack.availabe_items.append(Item(weight=weight, value=value))
        Knapsack.n += 1

    def __repr__(self) -> str:
        """How the knapsack object should be printed"""

        result = "Taken items: "
        for i, take in enumerate(self.selected_items):
            if take:
                result += f"{i + 1} "

        result += f"\nWeight: {self.__weight}\nValue: {self.__value}\n"
        return result
