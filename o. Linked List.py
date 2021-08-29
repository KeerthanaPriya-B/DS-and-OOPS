class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LL:
    def __init__(self):
        self.head = None
    def display(self):
        if self.head == None:
            print('Empty LL')
        else:
            temp = self.head
            while temp:
                print(temp.data,'-> ',end='')
                temp = temp.next

Display = LL()
n1 = Node(34)
Display.head = n1

n2 = Node(35)
n1.next = n2

n3 = Node(34)
n2.next = n3

Display.display()

'''output:  34 -> 35 -> 34 -> '''
