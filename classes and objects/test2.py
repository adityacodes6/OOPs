class DemoClass:

    a = 10
    b = 30

    def __init__(self):
        print("hello")
    
    def showValue(self):
        self.c = self.a * self.b
        print(self.c)

    def showValue1(self, a, b):
        print(a + b)

obj = DemoClass()
obj.showValue()
obj.showValue1(20, 30)