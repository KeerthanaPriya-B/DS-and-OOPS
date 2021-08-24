# Python program for implementation of Selection

list = list(map(int, input('Enter the list: ').split()))

for i in range(len(list)):
    min_val = min(list[i:])
    min_ind = list.index(min_val)
    list[i], list[min_ind] = list[min_ind], list[i]

print(list)

'''output:
Enter the list: 9 6 23 8 23 67
[6, 8, 9, 23, 23, 67]'''
