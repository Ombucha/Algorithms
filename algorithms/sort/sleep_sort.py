import time
import threading

def sleep_sort(array: list[float]) ->list[float]:
    result = []
    def add(element: float) -> None:
        result.append(element)
    first = array[0]
    for element in array:
        first = max(first, element)
        threading.Timer(element, add, [element]).start()
    time.sleep(first + 1)
    return result
