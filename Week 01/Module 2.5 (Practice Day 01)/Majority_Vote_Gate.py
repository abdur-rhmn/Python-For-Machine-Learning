n = int(input())

yes = 0
no = 0

for i in range(n):
    vote = input()
    if vote == "YES":
        yes+=1
    else:
        no+=1

if yes >= no:
    print("ACCEPT")
else:
    print("REJECT")