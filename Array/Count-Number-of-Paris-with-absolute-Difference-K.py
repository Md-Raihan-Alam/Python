# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        output=0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if(abs(nums[i]-nums[j]))==k:
                    output+=1
        return output

#    class Solution:
#     def countKDifference(self, nums: List[int], k: int) -> int:
#         output=0
#         cnt=Counter(nums)
#         for i in nums:
#             if i+k in cnt:
#                 output+=cnt[i+k]
#         return output