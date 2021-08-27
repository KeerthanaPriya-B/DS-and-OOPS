#Linear search

list = [1,2,3,9,6]
for i in range(len(list)):
    if(list[i] == 9):
        print('index:',i)
        
'''ouput -> index: 3'''



#Binary search

def binary(list,ele):
    lower = 0
    upper = len(list)-1

    while lower <= upper:
        mid = (lower+upper) // 2
        if list[mid] == ele:
            print('index:',mid)
            break
        elif list[mid] < ele:
            lower = mid + 1
        else:
            upper = mid - 1

list = [1,2,3,9,16]
binary(list,16)

'''output -> index: 4'''
