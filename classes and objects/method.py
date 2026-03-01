class Person:
    def greet(self):
        self.name = "Aditya"
        print("hello " + self.name)

obj = Person()
obj.greet()