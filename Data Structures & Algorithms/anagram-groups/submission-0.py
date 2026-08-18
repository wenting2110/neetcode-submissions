class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = {}
        for c in strs:
            temp_key = "".join(sorted(c))
            # print(temp_key)
            if temp_key in temp.keys():
                temp[temp_key].append(c)
            else:
                temp[temp_key] = [c]
                
        return list(temp.values())