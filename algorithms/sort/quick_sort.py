# Helper functions
def choosePivot(array: list[float], left: int, right: int) -> int:
    return int((left + right) / 2)  # Middle index

def elementSwap(arr: list[float], idx1: int, idx2: int) -> None:
    arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

# Worker quick_sort function
def quick_sort_recursive(array: list[float], left: int, right: int) -> None:

    # assert valid left and right parameters
    length = right - left
    assert length >= 0, "Can have non-positively sized subarray"
    assert 0 <= left, "left value must be in the array range"
    assert right <= len(array), "right value must be in the array range"

    # base case: given an array of size 0, 1, or 2
    if length == 2 and array[left] > array[right - 1]:
        elementSwap(array, left, right - 1)
    if length <= 2:
        return

    # partition the array into sections: <, =, and > the pivot
    pivot = array[choosePivot(array, left, right)]
    lessInserter = equalInserter = left
    for toPlace in range(left, right):
        if array[toPlace] < pivot:
            elementSwap(array, lessInserter, equalInserter)
            if equalInserter != toPlace:  # typical case
                elementSwap(array, lessInserter, toPlace)
            equalInserter += 1; lessInserter += 1
        elif array[toPlace] == pivot:
            elementSwap(array, equalInserter, toPlace); equalInserter += 1

    # recursive step: break down array into the elements < or > the pivot
    quick_sort_recursive(array, left, lessInserter)
    quick_sort_recursive(array, equalInserter, right)

# Wrapper function for quick_sort_recursive
def quick_sort(array: list[float]) -> None:
    quick_sort_recursive(array, 0, len(array))
