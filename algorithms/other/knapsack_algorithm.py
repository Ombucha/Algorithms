class Item:

    def __init__(self, weight: float, profit: float) -> None:
        self.weight = weight
        self.profit = profit

def maximum_profit_dynamic(capacity: float, items: list[Item]) -> float:
    length = len(items)
    profits = [[None for _ in range(capacity + 1)] for _ in range(length + 1)]
    for index in range(length + 1):
        profits[index][0] = 0
    for index in range(capacity + 1):
        profits[0][index] = 0
    for index in range(1, length + 1):
        weight = items[index - 1].weight
        profit = items[index - 1].profit
        for _index in range(1, capacity + 1):
            if weight <= _index:
                profits[index][_index] = max(profits[index - 1][_index], profits[index - 1][_index - weight] + profit)
            else:
                profits[index][_index] = profits[index - 1][_index]
    return profits[-1][-1]

def maximum_profit_recursive(capacity: float, items: list[Item], index: int = None) -> float:
    if index is None:
        index = len(items)
    if index == 0 or capacity == 0:
        return 0
    if items[index - 1].weight > capacity:
        profit = maximum_profit_recursive(capacity, items, index - 1)
        return profit
    profit = max(items[index - 1].profit + maximum_profit_recursive(capacity - items[index - 1].weight, items, index - 1), maximum_profit_recursive(capacity, items, index - 1))
    return profit

def knapsack_algorithm(capacity: float, items: list[Item]) -> set[Item]:
    selected = set()
    index = len(items) - 1
    value = capacity
    while index > 0 and value > 0:
        if maximum_profit_recursive(value, items, index) > maximum_profit_recursive(value, items, index - 1):
            selected.add(items[index])
            value -= items[index].weight
        index -= 1
    return selected
