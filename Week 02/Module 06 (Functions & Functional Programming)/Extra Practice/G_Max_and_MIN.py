input()

numbers = list(map(int, input().split()))

min = numbers[0]
max = numbers[0]

l_min = lambda cur, x : x if  x < cur else cur
l_max = lambda cur, x : x if  x > cur else cur

for num in numbers:
    min = l_min(min, num)
    max = l_max(max, num)

print(min, max)