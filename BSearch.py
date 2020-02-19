def findElement(arr, l, r, k):
    #print(l,r)
    if (l <= r):
        mid = int((l + (r)) / 2)
        if (arr[mid]==k):
            print(mid)
            print("yes")
        elif (k < arr[mid]):
            findElement(arr, l, mid - 1, k)
        else:
            findElement(arr, mid + 1, r, k)
    else:

        print("no")


n,k=map(int,input().split())
arr=list(map(int,input().split()[:n]))
findElement(arr,0,len(arr)-1,k)