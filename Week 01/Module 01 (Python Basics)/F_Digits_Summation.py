# Problem Link: https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/F

val = input()

numbers = val.split()

x  = int(numbers[0]); y= int(numbers[1])

x = x % 10; y = y % 10

print(x+y)