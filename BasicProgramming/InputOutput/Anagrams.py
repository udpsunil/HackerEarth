# Given two strings, a and b , that may or may not be of the same length, determine the minimum number of character
# deletions required to make a and b anagrams. Any characters can be deleted from either of the strings.

# my idea is to create dictionary of each letter appearing in string a and b. get common letters and find the difference
# between unique letter counts, add them up.
# find unique letters, directly add the count of unique letters
N = int(input())
for _ in range(N):
    a = input()
    b = input()
    a_dict = {}
    b_dict = {}
    count = 0
    for letter in a:
        if letter not in a_dict.keys(): a_dict[letter] = 1
        else: a_dict[letter] += 1
    for letter in b:
        if letter not in b_dict.keys(): b_dict[letter] = 1
        else: b_dict[letter] += 1
    letters_to_go_through = set(a_dict.keys()).intersection(set(b_dict.keys()))
    letters_to_ignore = set(a_dict.keys()).union(set(b_dict.keys())) - letters_to_go_through
    for letter in letters_to_ignore:
        if letter in a_dict.keys(): count += a_dict[letter]
        if letter in b_dict.keys(): count += b_dict[letter]
    for letter in letters_to_go_through:
        count += abs(a_dict[letter] - b_dict[letter])
    print(count)

# Best solution
