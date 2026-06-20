class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has={}

        for i in nums:
            if i not in has:
                has[i]=1
            else:
                has[i]+=1    
                return True
        return False        