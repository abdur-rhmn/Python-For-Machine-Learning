input()

a = list(map(int, input().split()))
b = list(map(int, input().split()))

def combine(a,b):
    c = b + a
    return c

c = combine(a, b)

for item in c:
    print(item, end=" ")