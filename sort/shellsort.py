from random import randint
from insertsort import insertsort

def shellsort(arr):
    mid=len(arr)//2
    while mid>0:
        for i in range(mid):
            insertsort(arr,i,mid)
        mid=mid//2
    return arr

if __name__=='__main__':
    arr=[randint(0,100) for _ in range(14)]
    print(shellsort(arr)==sorted(arr))