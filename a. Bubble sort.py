# Python program for implementation of Bubble Sort
def bubbleSort(list):
    for i in range(len(list)-1, 0, -1):
        for j in range(i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

list = list(map(int, input('Enter the list: ').split()))
bubbleSort(list)
print(list)

'''output:
Enter the list: 43 67 12 89 23 90 34 7
[7, 12, 23, 34, 43, 67, 89, 90]'''
