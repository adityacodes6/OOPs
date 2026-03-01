class Student:

    # private var
    __name = "Aditya"

    def __init__(self):
        print(self.__name)
        
    def __displayInfo(self):
        print('hi aditya')

obj = Student()