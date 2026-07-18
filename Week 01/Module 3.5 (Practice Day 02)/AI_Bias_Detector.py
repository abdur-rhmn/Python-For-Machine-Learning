inp = input()

str = inp.split()

a = str.count('A')
b = str.count('B')

a_par = (100*a)/len(str)
b_par = (100*b)/len(str)

if(a_par > 70 or b_par > 70):
    print("Biased Model")
else:
    print("Fair Model")