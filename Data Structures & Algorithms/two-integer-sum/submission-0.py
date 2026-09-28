class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        for index, num in enumerate(nums):
            numDict[num] = index
        
        for index, num in enumerate(nums):
            diff = target - num
            if diff in numDict and numDict[diff] != index:
                return [index, numDict[diff]]
        return []