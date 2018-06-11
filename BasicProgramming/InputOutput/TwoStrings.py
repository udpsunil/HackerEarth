# Learnt how to use for... else. whenever you break out of for loop, else is not executed.
# if the loop executes without any break, then only else clause is executed.
for _ in range(int(input())):
    a, b = input().split(' ')
    a_dict = {}
    b_dict = {}
    for letter in a:
        if letter not in a_dict.keys(): a_dict[letter] = 1
        else: a_dict[letter] += 1
    for letter in b:
        if letter not in b_dict.keys(): b_dict[letter] = 1
        else: b_dict[letter] += 1
    if a_dict.keys() != b_dict.keys():
        print("NO")
    else:
        for key in a_dict.keys():
            if a_dict[key] != b_dict[key]: 
                print("NO")
                break
        else:
            print("YES")