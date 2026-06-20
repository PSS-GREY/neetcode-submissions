class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        has={}
        s=''
        for i in strs:
            s=''.join(sorted(i))
            if s not in has:
                has[s]=[i]
            else:
                has[s].append(i)
        return list(has.values())