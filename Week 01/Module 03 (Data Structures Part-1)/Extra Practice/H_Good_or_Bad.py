t = int(input())

for i in range(t):
    num = input()

    if "101" in num or "010" in num:
        print("Good")
    else:
        print("Bad")