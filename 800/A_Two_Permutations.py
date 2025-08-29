# from itertools import permutations
# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.isEnd = False
#     def insert(self, word):
#         node = self
#         for char in word:
#             if char not in node.children:
#                 node.children[char] = TrieNode()
#             node = node.children[char]
#         node.isEnd = True
#     def longest_common_prefix(self, word, word2, prefixCheck):

#         node = self
#         length = 0
#         i = 0
#         for char in word:
#             if char in node.children and char == word2[i]:
#                 node = node.children[char]
#                 length += 1
#                 i += 1
#             else:
#                 break
#         return length == prefixCheck
        
#     def longest_common_suffix(self, word,word2 ,suffixCheck):
#         word2 = word2[::-1]
#         node = self
#         length = 0
#         j = 0
#         for char in word[::-1]:
#             if char in node.children and char == word2[j]:
#                 node = node.children[char]
#                 length += 1
#                 j += 1
#             else:
#                 break
#         return length == suffixCheck

t = int(input())
for _ in range(t):
    n,a,b = list(map(int,input().split()))
    # perm = list(permutations(range(1,n+1),n))
    # root = TrieNode()
    # for num in perm:
    #     root.insert(num)
    # if len(perm) == 1:
    #     print("Yes")
    #     continue
    # flag = False
    # for i in range(len(perm)):
    #     for j in range(i+1,len(perm)):
    #         if (root.longest_common_prefix(perm[i],perm[j],a) == root.longest_common_suffix(perm[i],perm[j],b) == True):
    #             print("Yes")
    #             flag = True
    #             break
    #     if flag == True:
    #         break
    # else:
    #     print("No")
    if a == b == n:
        print("Yes")
    elif a+b+2 <= n:
        print("Yes")
    else:
        print("No")

