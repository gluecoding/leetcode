class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, x in enumerate(nums):
            j = d.get(target - x, None)
            if j is not None:
                return [j, i]
            else:
                d[x] = i

