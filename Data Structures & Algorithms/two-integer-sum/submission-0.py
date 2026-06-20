class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        has={}
        com=0
        for i in range(len(nums)):
            com=target-nums[i]
            if com not in has:
                has[nums[i]]=i
            else:
                return [has[com],i] 
                  