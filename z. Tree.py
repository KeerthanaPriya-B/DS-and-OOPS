class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent =self
        self.children.append(child)

    def print_tree(self):
        print(self.data)                                        
        if self.children:
            for child in self.children:
                child.print_tree()

def build_Vehicle():
    root = TreeNode('Vehicle')
    car = TreeNode('car')
    root.add_child(car)
    car.add_child(TreeNode('Audi'))
    
    bike = TreeNode('Bike')
    root.add_child(bike)
    bike.add_child(TreeNode('Honda'))
    
    root.print_tree()

if __name__ =='__main__':
    build_Vehicle()

'''output:
Vehicle
car
Audi
Bike
Honda'''    
-----------------------------------------------------------------------------------------------------------------------------------------   
#STANDARD WAY

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent =self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level+=1
            p = p.parent
        return level

    def print_tree(self):
        spaces = ' '*self.get_level()*4
        prefix = spaces +'* ' if self.parent else ''
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

def build_Vehicle():
    root = TreeNode('Vehicle')

    car = TreeNode('car')
    root.add_child(car)
    car.add_child(TreeNode('Audi'))
    car.add_child(TreeNode('BMW'))

    bike = TreeNode('Bike')
    root.add_child(bike)
    bike.add_child(TreeNode('Honda'))
    bike.add_child(TreeNode('TVS'))

    root.print_tree()

if __name__ =='__main__':
    build_Vehicle()

'''output:
Vehicle
    * car
        * Audi
        * BMW
    * Bike
        * Honda
        * TVS'''
-----------------------------------------------------------------------------------------------------------------------------------------  
# SIMPLE IMPLEMENTATION

class BinaryTreeNode:
  def __init__(self, data):
    self.data = data
    self.leftChild = None
    self.rightChild = None
     
a1=BinaryTreeNode(10)
a2=BinaryTreeNode(15)
a3=BinaryTreeNode(20)

a1.leftChild=a2
a1.rightChild=a3

print("Root Node is:")
print(a1.data)
print("left child of node is:")
print(a1.leftChild.data)
print("right child of node is:")
print(a1.rightChild.data)

'''output
Root Node is:
10
left child of node is:
15
right child of node is:
20'''
