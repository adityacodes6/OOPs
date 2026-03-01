class Parent:
    
    def demo(self):
        print('hi')

class Child1(Parent):

    def test1(self):
        print("this is child1")


class Child2(Parent):

    def test2(self):
        print("this is child2")

obj1 = Child1()
obj2 = Child2()
obj1.demo() # parent
obj1.test1() # child1
obj2.test2() # child2
