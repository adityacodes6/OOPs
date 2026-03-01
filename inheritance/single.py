class A:

    def displayA(self):
        print("hello aditya A")

class B(A):
    
    def displayB(self):
        print("hello aditya B")

obj = B()
obj.displayA()
obj.displayB()