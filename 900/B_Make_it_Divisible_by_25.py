for _ in range(int(input())):
    nStr = input()
    n = int(nStr)
    def check(num,digit1,digit2):
        nonMatch = 0
        dg1 = "-1"
        dg2 = "-1"
        for i in range(len(num)-1,-1,-1):
            if num[i] != digit1 and num[i] != digit2:
                nonMatch += 1
            else:
                if (dg2=="-1" and num[i] == digit2):
                    dg2 = num[i]
                elif (dg2 != "-1" and num[i] == digit1):
                    dg1 = num[i]
                else:
                    nonMatch += 1
            if dg1 != "-1" and dg2 != "-1":
                return nonMatch
        return 10**20
    print(min(check(nStr,'0','0'),
    check(nStr,'2','5'),
    check(nStr,'5','0'),
    check(nStr,'7','5')))
