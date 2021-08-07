'''Method Overloading: 
Method Overloading is an example of Compile time polymorphism. In this, more than one method of the same class shares the same method name having different signatures.
 Method overloading is used to add more to the behavior of methods and there is no need of more than one class for method overloading.
Note: Python does not support method overloading. We may overload the methods but can only use the latest defined method.'''

# Function to take multiple arguments
def add(datatype, *args):
	# if datatype is int
	# initialize answer as 0
	if datatype =='int':
		answer = 0
		
	# if datatype is str
	# initialize answer as ''
	if datatype =='str':
		answer =''

	# Traverse through the arguments
	for x in args:

		# This will do addition if the
		# arguments are int. Or concatenation
		# if the arguments are str
		answer = answer + x

	print(answer)

# Integer
add('int', 5, 6)

# String
add('str', 'Hi ', 'Geeks')

'''Output: 
11
Hi Geeks'''