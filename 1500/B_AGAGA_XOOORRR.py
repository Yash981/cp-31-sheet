from functools import reduce
import operator
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    if len(set(arr))==1:
        print("YES")
        continue
    xorr = reduce(operator.xor, arr)
    if xorr == 0:
        print("YES")
    else:
        prefixXor = [0]
        for num in arr:
            prefixXor.append(prefixXor[-1] ^ num)
        suffixXor = [0]
        for num in reversed(arr):
            suffixXor.append(suffixXor[-1] ^ num)
        suffixXor.reverse()
        found = False
        for i in range(1, n-1):
            if prefixXor[i] == xorr:
                middlexor = 0
                for j in range(i+1, n):
                    middlexor ^= arr[j-1]
                    if suffixXor[j] == xorr and middlexor == xorr:
                        found = True
                        print("YES")
                        break
            if found:
                break
        if not found:
            print("NO")
        
        
