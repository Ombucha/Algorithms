import copy
import typing

class Activity:

    def __init__(self, start_time, finish_time) -> None:
        self.start_time = start_time
        self.finish_time = finish_time

    def __iter__(self) -> typing.Iterator[float]:
        for item in (self.start_time, self.finish_time):
            yield item

def activity_selection(activities: list[Activity]) -> list[Activity]:
    start_times = [activity.start_time for activity in activities]
    finish_times = [activity.finish_time for activity in activities]
    _activities = copy.copy(activities)
    _activities.sort(key = lambda activity: activity.finish_time)
    selected = {_activities[0]}
    index = 1
    length = len(_activities)
    for _index in range(1, length):
        if start_times[_index] >= finish_times[index]:
            selected = selected.union({_activities[_index]})
            index = _index
    return selected
