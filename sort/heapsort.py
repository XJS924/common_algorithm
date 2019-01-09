from random import randint


def heapify(arr, root, size):
    left = root * 2
    right = left + 1
    larger = root
    if left < size and arr[larger] < arr[left]: larger = left
    if right < size and arr[larger] < arr[right]: larger = right
    if larger != root:
        arr[larger], arr[root] = arr[root], arr[larger]
        heapify(arr, larger, size)


def build_max_heap(arr):
    size = len(arr)
    for i in range(size // 2 - 1, -1, -1):
        heapify(arr, i, size)


def heapsort(arr):
    build_max_heap(arr)
    for i in range(len(arr) - 1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, 0, i)
    return arr


if __name__ == '__main__':
    arr = [randint(0, 100) for _ in range(14)]
    # print(sorted(arr))
    # print(arr)
    print(heapsort(arr) == sorted(arr))
