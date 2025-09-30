t = int(input())
for i in range(t):
    n,m = list(map(int,input().split()))
    startX,startY = list(map(int,input().split()))
    endX,endY = list(map(int,input().split()))
    directionsIntital = []
    directionLast = []
    direction = [[n,m],[-n,m],[n,-m],[-n,-m],[m,n],[-m,-n],[-m,n],[m,-n]]
    for i,j in direction:
        directionsIntital.append((startX+i,startY+j))
    for i,j in direction:
        directionLast.append((endX+i,endY+j))
    print(len(set(directionsIntital) & set(directionLast)))

            
