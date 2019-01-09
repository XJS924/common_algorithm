from random import randint


def insertsort(arr, n=1, dis=1):
    for i in range(n, len(arr), dis):
        key = arr[i]
        j = i - dis
        while j >= 0 and key < arr[j]:
            arr[j + dis] = arr[j]
            j -= dis
        arr[j + dis] = key
    return arr


if __name__ == '__main__':
    arr = [randint(0, 100) for _ in range(0, 100)]
    print(insertsort(arr) == sorted(arr))
