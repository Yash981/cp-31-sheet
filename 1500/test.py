# Problem had some story, providing a simplified version

# Given an array of n elements where some elements are -1 and others are some integer between 1 and 200, find the number of ways to replace -1 with some value b/w 1 to 200 such that these constraints are satisfied

# arr[0] <= arr[1]
# arr[n - 2] >= arr[n - 1]
# arr[i] <= max(arr[i - 1], arr[i + 1]) for all i between [1, n - 2]
# n <= 1e4
arr = [1, -1, 2, -1, -1]
n = len(arr)
def dp(i):
    if i >= n:
        return 0
    if arr[i] != -1:
        return 0
    
    