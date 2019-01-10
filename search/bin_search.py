from random import randint

def bin_search(arr,target):
    low,high,mid=0,len(arr)-1,len(arr)//2
    while target!=arr[mid]:
        if target<arr[mid]:high=mid-1
        else:low=mid+1
        if low>high:return -1
        mid=(low+high)//2
    return mid

if __name__=='__main__':
    arr=sorted([randint(0,100) for _ in range(14)])
    print(arr)
    print(bin_search([1, 1, 6, 17, 23, 30, 47, 56, 65, 69, 77, 81, 84, 93],1))