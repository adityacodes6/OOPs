# zip function is use to comebine two or more iterrable (like list, tuples) element by element

name = ["aditya", "baby", "driver"]
age = [19, 26, 26]

res = list(zip(name, age))
print(res)


# if list have diff len it stops at shortest len
l1 = [1,2,3]
l2 = [7,8]

print(list(zip(l1, l2)))
