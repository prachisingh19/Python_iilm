class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap ={}
        for i in range(len(nums)):
            needed = target-nums[i]
            if needed in hashmap:
                return[i,hashmap[needed]]
            hashmap[nums[i]]=i
        return[]

        