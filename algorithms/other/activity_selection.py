from __future__ import annotations

import copy
import typing

class Activity:

    def __init__(self, start_time: float, finish_time: float) -> None:
        self.start_time = start_time
        self.finish_time = finish_time

    def __iter__(self) -> typing.Iterator[float]:
        for item in (self.start_time, self.finish_time):
            yield item

def activity_selection(activities: list[Activity]) -> set[Activity]:
    _activities = copy.deepcopy(activities)
    _activities.sort(key = lambda activity: activity.finish_time)
    selected = {_activities[0]}
    latest = _activities[0].finish_time
    length = len(_activities)
    for index in range(1, length):
        if _activities[index].start_time >= latest:
            selected.add(_activities[index])
            latest = _activities[index].finish_time
    return selected
