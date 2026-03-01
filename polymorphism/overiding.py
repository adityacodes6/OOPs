class Parent:

    def demo(self):
        print("hello")

class Child(Parent):
    
    def demo(self): # overiding
        print("hi")

obj = Child()
obj.demo()