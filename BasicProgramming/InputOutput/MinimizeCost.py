def Solve (k, arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] <= 0:
            continue
        while (arr[i]>0) and (j <= i+k):
            if arr[j] >= 0:
                j += 1
                continue
            v = min(arr[i], abs(arr[j]))
            arr[i] -= v
            arr[j] += v
            if arr[j] >= 0:
                j+=1
    return sum([abs(i) for i in arr])



n, k = map(int, input().split(' '))
arr = list(map(int, input().split()))

out_ = Solve(k, arr)
print (out_)