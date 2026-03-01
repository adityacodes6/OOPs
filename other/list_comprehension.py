# list comprehension is an short and clean way of creating new list form an existing iterable (list, tuple, range)

l = [l for l in range(5)]
print(l)

r = [x ** 2 for x in range(5)]
print(r)

# for even nums
r = [x ** 2 for x in range(5) if x % 2 == 0]
print(r)

