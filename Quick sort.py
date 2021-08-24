def pivot_place(list, first, last):
    pivot = list[first]
    left = first+1
    right = last
    while True:
        while left <= right and list[left] <= pivot:
            left+=1
        while left <= right and list[right] >= pivot:
            right-=1
        if right < left:
            break
        else:
            list[left], list[right] = list[right], list[left]
    list[first], list[right] = list[right], list[first]
    return right

def quickSort(list, first, last):
    if first < last:
        p = pivot_place(list, first, last)
        quickSort(list, first, p-1)
        quickSort(list, p+1, last)

list = list(map(int, input('Enter the list: ').split()))
n= len(list)
quickSort(list, 0, n-1)
print(list)

'''output:
Enter the list:  2 56 23 78 43 76
[2, 23, 43, 56, 76, 78]
'''
