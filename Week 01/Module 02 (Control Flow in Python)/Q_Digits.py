# Problem Link: https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/Q


t = int(input())

for i in range(t):

    numbers = int(input())

    if numbers == 0:
        print(0)
        continue
    while numbers > 0:
        print(numbers%10, end=" ")
        numbers//=10
    print()