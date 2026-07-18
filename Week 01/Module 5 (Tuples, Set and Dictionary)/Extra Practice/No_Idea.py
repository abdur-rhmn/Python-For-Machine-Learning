size = input().split()

n = size[0]
m = size[1]

arr = input().split()

a = set(input().split())

b = set(input().split())

happiness = 0

for x in arr:
    if x in a:
        happiness += 1
    elif x in b:
        happiness -= 1

print(happiness)







