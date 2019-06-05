def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False
    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    if found:
        print("Element found at index",midpoint)
    else:
        print("Element not found.")

a=[1,3,2,5,8,0]
binarySearch(a,2)
binarySearch(a,10)