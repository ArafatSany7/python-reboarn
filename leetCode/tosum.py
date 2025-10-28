class Solution(object):
    def twosum(self, nums, target):
        numMap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in numMap:
                return [numMap[complement], i]
            numMap[num] = i


nums = [2, 7, 11, 133]
target = 18
sol = Solution()
print(sol.twosum(nums, target))
