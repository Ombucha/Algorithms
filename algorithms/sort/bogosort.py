import random

def is_sorted(data: list[float]) -> bool:
    boolean = all(index <= _index for index, _index in zip(data, data[1:]))
    return boolean

def bogosort(data: list[float]) -> list[float]:
    while not is_sorted(data):
        random.shuffle(data)
    return data
