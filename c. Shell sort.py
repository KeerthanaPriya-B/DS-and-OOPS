# Python program for implementation of Shell Sort
def shellsort(list):
    gap = len(list) // 2
    while gap>0:
        for index in range(gap ,len(list)):
            current_ele = list[index]
            pos = index
            while pos >= gap and current_ele < list[pos-gap]:
                list[pos] = list[pos-gap]
                pos = pos-gap
            list[pos] = current_ele
        gap = gap//2

num = int(input('List Length:'))
list = [int(input()) for i in range(num)]
shellsort(list)
print('sorted list: ',list)

'''output:
list length:3
5
9
1
sorted list: [1, 5, 9]'''
