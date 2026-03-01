class Parent:

    def demo(self):
        print("hello")

class Child(Parent):
    
    def demo(self): 
        super().demo() # overload using super key word
        print("hi")

obj = Child()
obj.demo()