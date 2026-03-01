


try:
    num = int(input("Enter a num: "))
    print(10 / num)
except ZeroDivisionError:
    print("cant div")
else: 
    print("no err")
finally:
    print("exec complete")
