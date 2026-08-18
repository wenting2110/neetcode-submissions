# Hash Table 57ms, 8.7MB
# Time: O(m*n), Space(m*n)
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

        # return temp.values() # error
        return list(temp.values())