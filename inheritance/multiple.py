class A:

    def displayA(self):
        print("hello aditya A")

class B:
    
    def displayB(self):
        print("hello aditya B")

class C(A, B):
    
    def displayC(self):
        print("hello aditya C")    

obj = C()
obj.displayA()
obj.displayB()
obj.displayC()

