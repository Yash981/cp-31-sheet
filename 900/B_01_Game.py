t = int(input())
for i in range(t):
    n = input()
    x = min(n.count('0'),n.count('1'))
    if x % 2:
        print("DA")
    else:
        print("NET")