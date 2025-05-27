if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    a=max(arr)
    max2=None
    for i in range (0,n,1):
        if(arr[i]<a):
            if (max2 is None or arr[i]>max2):
                max2=arr[i]
    print(max2)
