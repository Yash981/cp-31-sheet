t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    i = 0
    j = n-1
    firstMisMatchVals = []
    while i < j:
        if arr[i] != arr[j]:
            firstMisMatchVals = [arr[i],arr[j]]
            break
        else:
            i += 1
            j -= 1
    if not firstMisMatchVals:
        print("YES")
        continue
    array1 = []
    array2 = []
    for i in arr:
        if i != firstMisMatchVals[0]:
            array1.append(i)
        if i != firstMisMatchVals[1]:
            array2.append(i)
    if array1 == array1[::-1] or array2 == array2[::-1]:
        print("YES")
    else:
        print("NO")