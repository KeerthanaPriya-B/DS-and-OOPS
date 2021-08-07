'''Method Overriding: 
Method overriding is an example of run time polymorphism. In this, the specific implementation of the method that is already provided by the parent class is provided by the child class.
 It is used to change the behavior of existing methods and there is a need for at least two classes for method overriding.
 In method overriding, inheritance always required as it is done between parent class(superclass) and child class(child class) methods.'''

class A:
	def fun1(self):
		print('feature_1 of class A')
		
	def fun2(self):
		print('feature_2 of class A')
	

class B(A):
	# Modified function that is
	# already exist in class A
	def fun1(self):
		print('Modified feature_1 of class A by class B')
		
	def fun3(self):
		print('feature_3 of class B')
		

# Create instance
obj = B()
	
# Call the override function
obj.fun1()

'''Output: 
Modified feature_1 of class A by class B'''