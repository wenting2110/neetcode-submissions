# Reverse string 28ms, 7.7MB
# Time: O(n), Space: O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''
        for i in s:
            if i.isalnum():
                new_s += i.lower()
        # print(new_s[::-1])
        return new_s == new_s[::-1]