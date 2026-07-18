n = int(input())

num = input().strip().split()

t = tuple(int(x) for x in num)

print(hash(t))