inp = input()

str = inp.split()

keyword = ["ai", "data", "model", "learn", "train", "neural"]

cnt = 0

for val in keyword:
    if val in str:
        cnt+=1

if cnt >= 2:
    print("AI Detected")
else:
    print("Not AI Related")