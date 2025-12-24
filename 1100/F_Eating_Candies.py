import sys

# Using fast I/O for efficiency (optional, but good for large inputs)
input = sys.stdin.readline

t_str = input().strip()
if not t_str:
    exit()
t = int(t_str)

for _ in range(t):
    try:
        n_str = input().strip()
        if not n_str:
            break
        n = int(n_str)
        arr = list(map(int, input().split()))
    except ValueError:
        break

    # Handle edge case for empty or single-element array
    if n <= 1:
        print(0)
        continue

    l = 0
    r = n - 1
    
    # Initialize sums with the first and last elements
    left_sum = arr[l]
    right_sum = arr[r]
    
    ans = 0

    while l < r:
        if left_sum == right_sum:
            ans = (l + 1) + (n - r)
            # Move both pointers inward
            l += 1
            r -= 1
            # Only update sums if pointers haven't crossed/met
            if l < r:
                left_sum += arr[l]
                right_sum += arr[r]
        elif left_sum < right_sum:
            # Left sum is smaller, add more from left
            l += 1
            left_sum += arr[l]
        else:
            # Right sum is smaller, add more from right
            r -= 1
            right_sum += arr[r]

    print(ans)