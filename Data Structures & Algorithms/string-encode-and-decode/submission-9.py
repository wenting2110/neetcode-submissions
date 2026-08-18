# 參考 gemini
class Solution:

    def encode(self, strs: List[str]) -> str:
        # ["we", "say", ":", "yes"]
        encoded_str = ""
    
        for s in strs:
            # 格式：字串長度 + "#" + 字串本身
            encoded_str += str(len(s)) + '#' + s

        return encoded_str # "2#we3#say1#:3#yes"
    
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])

            start_idx = j + 1
            end_idx = start_idx + length
            res.append(s[start_idx : end_idx])

            i = end_idx

        return res
        
       
