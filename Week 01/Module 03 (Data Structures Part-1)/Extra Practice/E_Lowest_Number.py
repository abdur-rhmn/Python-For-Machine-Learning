n = int(input())

values = input()

numbers = values.split()

new_num = [int(num) for num in numbers]

min = new_num[0]
pos = 1

for i in range(1, n):
    if min > new_num[i]:
        min = new_num[i]
        pos = i+1

print(min, pos)