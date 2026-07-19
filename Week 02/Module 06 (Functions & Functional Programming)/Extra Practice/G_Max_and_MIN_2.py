from functools import reduce

input()

numbers = list(map(int, input().split()))

min = reduce(lambda cur, x : x if  x < cur else cur, numbers)
max = reduce(lambda cur, x : x if  x > cur else cur, numbers)

print(min, max)