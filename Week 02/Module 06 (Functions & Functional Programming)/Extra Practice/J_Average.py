from functools import reduce

input()

nums = list(map(float, input().split()))

avg = (reduce(lambda x,y : x+y, nums))/len(nums)

print(f"{avg:.7f}")
# print(f"{"%.7f" % avg}")