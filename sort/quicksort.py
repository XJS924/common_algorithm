from random import randint


def partion(arr, low, high):
    key = arr[low]
    while low < high:
        while low < high and key <= arr[high]: high -= 1
        if low < high: arr[low] = arr[high]
        while low < high and key > arr[low]: low += 1
        if low < high: arr[high] = arr[low]
    arr[low] = key
    return low


def quicksort(arr, low, high):
    if low < high:
        pos = partion(arr, low, high)
        quicksort(arr, low, pos)
        quicksort(arr, pos + 1, high)


if __name__ == '__main__':
    arr = [randint(0, 100) for _ in range(14)]
    print(sorted(arr))
    print(arr)
    quicksort(arr, 0, len(arr) - 1)
    print(arr == sorted(arr))
