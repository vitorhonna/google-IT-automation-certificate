fruit = {"oranges": 3, "apples": 5, "bananas": 7, "pears": 2, 'ab': {'c':1, 'd':2}}

print(sorted(fruit.items(),reverse=True, key = lambda x:x[1]))