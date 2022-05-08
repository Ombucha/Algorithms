from __future__ import annotations

import typing

class Activity:

    def __init__(self, start_time: float, finish_time: float, profit: float) -> None:
        self.start_time = start_time
        self.finish_time = finish_time
        self.profit = profit

    def __iter__(self) -> typing.Iterator[float]:
        for item in (self.start_time, self.finish_time):
            yield item

def previous(activities: list[Activity], index: int) -> int:
    activity = activities[index]
    previous_index = 0
    for _index in range(index):
        finish_time = activities[_index].finish_time
        if finish_time < activity.start_time and finish_time > activities[previous_index].finish_time:
            previous_index = _index
    return previous_index

def maximum_profit(activities: list[Activity], index: int = None) -> float:
    if index is None:
        index = len(activities) - 1
    if index == 0:
        return 0
    profit = max(maximum_profit(activities, index - 1), activities[index].profit + maximum_profit(activities, previous(activities, index)))
    return profit

def maximum_profit_memoised(activities: list[Activity], index: int = None) -> float:
    if index is None:
        index = len(activities) - 1
    profits = [None for _ in range(index + 1)]
    if index == 0:
        return 0
    if profits[index]:
        return profits[index]
    profits[index] = max(maximum_profit_memoised(activities, index - 1), activities[index].profit + maximum_profit_memoised(activities, previous(activities, index)))
    return profits[index]

def maximum_profit_dynamic(activities: list[Activity]) -> float:
    profits = [None for _ in range(len(activities))]
    profits[0] = 0
    for index, element in enumerate(activities):
        if index > 0:
            profits[index] = max(profits[index - 1], element.profit + profits[previous(activities, index)])
    return profits[-1]

def weighted_activity_selection(activities: list[Activity]) -> set[Activity]:
    selected = set()
    index = len(activities) - 1
    while index > 0:
        if maximum_profit(activities, index) > maximum_profit(activities, index - 1):
            selected.add(activities[index])
            index = previous(activities, index)
        else:
            index -= 1
    return selected
