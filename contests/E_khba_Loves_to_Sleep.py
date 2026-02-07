def can_place(friends, n, k, x, D):
    """Check if we can place k teleports with min distance D from all friends."""
    count = 0
    pos = 0 
    i = 0

    while pos <= x and count < k:
        while i < n and friends[i] - D <= pos <= friends[i] + D:
            pos = friends[i] + D + 1
            i += 1
        if pos > x:
            break
        count += 1
        pos += D + 1

    return count >= k


def solve():
    t = int(input())
    for _ in range(t):
        n, k, x = map(int, input().split())
        friends = sorted(map(int, input().split()))
        
        if n == k == x+1:
            print(*list(range(n)))
            continue
        low, high, best = 0, x, 0
        while low <= high:
            mid = (low + high) // 2
            if can_place(friends, n, k, x, mid):
                best = mid
                low = mid + 1
            else:
                high = mid - 1
        print(friends,"friends",best)
        teleports = []
        pos = 0
        i = 0
        while pos <= x and len(teleports) < k:
            while i < n and friends[i] - best <= pos <= friends[i] + best:
                pos = friends[i] + best + 1
                i += 1
            if pos > x:
                break
            teleports.append(pos)
            pos += best + 1

        print(*teleports)
solve()