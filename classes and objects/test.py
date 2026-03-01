# class DemoClass:

#     a = 10

#     def sumVal(self):
#         print(20 + 30)

# obj = DemoClass()
# obj.sumVal()

class DemoClass:

    a = 10

    def sumVal(self):
        print(20 + self.a)

obj = DemoClass()
obj.sumVal()