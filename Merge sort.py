# Python program for implementation of MergeSort
def mergesort(list):
    if len(list)>1:
        mid = len(list)//2
        left_list = list[:mid]
        right_list = list[mid:]
        mergesort(left_list)
        mergesort(right_list)
        i, j, k = 0, 0, 0
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                list[k] = left_list[i]
                i+=1
                k+=1
            else:
                list[k] = right_list[j]
                j+=1
                k+=1
        while i < len(left_list):
            list[k] = left_list[i]
            i += 1
            k += 1
        while j < len(right_list):
           list[k] = right_list[j]
           j += 1
           k += 1

list = list(map(int, input('Enter the list: ').split()))
mergesort(list)
print(list)

'''output:
Enter the list: 97 64 7 321 0 
[0, 7, 64, 97, 321]'''
