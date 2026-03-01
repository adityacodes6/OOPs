# selects elements based on condition

numbers = [1, 2, 3, 4, 5, 6]
                # function            iterable
result = filter(lambda x: x % 2 == 0, numbers)
print(list(result))