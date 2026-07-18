val = input()

num = val.split()

new_num = [int(x) for x in num]

sum = 0

for i in new_num:
    sum+=i

avg = sum/len(new_num)

if(avg < 85):
    print("Dark Image")
elif avg <= 170:
    print("Normal Image")
elif avg > 170:
    print("Bright Image")
