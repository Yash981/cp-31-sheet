t = int(input())
ans = []
for _ in range(t):
    s = input()
    pos = int(input())
    n = len(s)
    length = n
    stack = []
    for i in range(n):
        while stack and stack[-1] > s[i] and pos > length:
            stack.pop()
            pos -= length
            length -= 1
        stack.append(s[i])
    while pos > length:
        stack.pop()
        pos -= length
        length -= 1
    ans.append(stack[pos-1])
print("".join(ans))
