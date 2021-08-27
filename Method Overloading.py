'''Method Overloading: 
Method Overloading is an example of Compile time polymorphism. In this, more than one method of the same class shares the same method name having different signatures.
 Method overloading is used to add more to the behavior of methods and there is no need of more than one class for method overloading.
Note: Python does not support method overloading. We may overload the methods but can only use the latest defined method.'''

class add:
    def sum(self,a=None,b=None,c=None):
        if c == None:
            s = a+b
            return s
        else:
            s = a+b+c
            return  s

ob = add()
print(ob.sum(2,10,3))

