r = {'G':'C','C':'G','T':'A','A':'U'}
d = input()
if set(d).issubset(set(r.keys())):
    print(''.join(r[i] for i in d if i in r.keys()))
else:
    print("Invalid Input")