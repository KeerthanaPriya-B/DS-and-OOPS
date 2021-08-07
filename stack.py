# Python program for stack implementation using list

stack = []
# append() function to push element in the stack
stack.append('a')
stack.append('b')
stack.append('c')

print('Initial stack')
print(stack)

# pop() fucntion to pop element from stack in LIFO order
print('\nElements poped from stack:')
print(stack.pop(0))
print(stack.pop(0))
print(stack.pop(0))

print('\nStack after elements are poped:')
print(stack)

'''output
Initial stack
['a', 'b', 'c']
Elements poped from stack:
c
b
a
Stack after elements are poped:
[]'''