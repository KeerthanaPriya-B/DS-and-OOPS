# Python program for implementation of Insertion Sort
def insertionSort(list):
    for index in range(1, len(list)):
        current_ele = list[index]
        pos = index
        while pos>0 and current_ele < list[pos-1]:
            list[pos] = list[pos-1]
            pos = pos-1
        list[pos] = current_ele

list = list(map(int, input('Enter the list: ').split()))
insertionSort(list)
print(list)

'''output:
Enter the list: 34 56 87 12 98
[12, 34, 56, 87, 98]'''
