from random import randint


def merge(a, b):
    h, j, c = 0, 0, []
    while h < len(a) and j < len(b):
        if a[h] < b[j]:
            c.append(a[h])
            h += 1
        else:
            c.append(b[j])
            j += 1
    c += a[h:] + b[j:]
    return c


def mergesort(arr):

    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    a = mergesort(arr[:mid])
    b = mergesort(arr[mid:])
    return merge(a, b)


if __name__ == '__main__':
    arr = [randint(0, 100) for i in range(14)]
    print(mergesort(arr)==sorted(arr))
