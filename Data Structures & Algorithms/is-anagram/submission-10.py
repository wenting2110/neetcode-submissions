# Hash Map
# Time: O(n+m), Space: O(1) for 26 alphabet
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            # eg: s = 'apple'
            # eg:count[s[1]=a] = 1 + count[a].values()
            countS[s[i]] = 1 + countS.get(s[i], 0) 
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
        