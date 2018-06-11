# Learng fast input/output technique. 
# Instead of reading element and then doing sum of sublist, keep on doing sum and then diff the elements to get the actual sum
N, Q = map(int, input().split(' '))
A = list(map(int, input().split(' ')))
s = [0]
for i,a in enumerate(A):
    if i == 0:
        continue
    s.append(s[i]+a)
for _ in range(Q):
    L, R = map(int, input().split(' '))
    print((s[R-1]- s[L-1]) // (R-L+1))
    