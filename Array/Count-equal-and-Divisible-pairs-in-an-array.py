# https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        pairs=0
        i=0
        while i < len(nums):
            j=i+1
            while j < len(nums):
                if nums[i]==nums[j] and i!=j:
                    if (i*j)%k==0:
                        pairs=pairs+1
                j=j+1
            i=i+1
        return pairs

# class Solution:
#     def countPairs(self, nums: List[int], k: int) -> int:
#         c=0
#         for i in range(len(nums)-1):
#             for j in range(i+1,len(nums)):
#                 if nums[i]==nums[j]:
#                     if (i*j)%k==0:
#                         c+=1
#         return c
# class Solution:
#     def countPairs(self, nums: List[int], k: int) -> int:
#         d={}
#         cnt=0
#         for i in range(len(nums)):
#             if nums[i] in d:
#                 for x in d[nums[i]]:
#                     if (x*i)%k==0:
#                         cnt+=1
#                 d[nums[i]].append(i)
#             else:
#                 d[nums[i]]=[i]
                
#         return cnt