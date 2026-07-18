n = int(input())

target = float(input())

sum = 0

for i in range(n):
    val = float(input())
    sum+=val
    
if (sum/n) <= target:
    print("PASS")
else:
    print("RETRY")