n = int(input())

values = input()

numbers = values.split()

new_num = [int(num) for num in numbers]

min = new_num[0]; max = new_num[0]

for val in new_num:
    if(min > val):
        min = val
    if max < val:
        max = val

min_pos = new_num.index(min)
max_pos = new_num.index(max)

new_num[min_pos], new_num[max_pos] = max, min

for val in new_num:
    print(val, end=" ")
