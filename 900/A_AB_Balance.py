t = int(input())
for i in range(t):
    s = input()
    if s[0] == s[-1]:
        print(s)
    else:
        if s[0] == "b":
            print("a"+s[1:])
        else:
            print("b"+s[1:])