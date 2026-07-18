inp = input()

count = [0] * 26

for val in inp:
    count[ord(val)-ord('a')]+=1

for i in range(26):
    if count[i] != 0:
        print(f"{chr(ord('a')+i)} : {count[i]}")