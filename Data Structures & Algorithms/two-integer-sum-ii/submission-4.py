# Two Pointers, time：O(n), space：O(1)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # index = 0
        # if target <= numbers[index]:
        #     while target <= numbers[index]:
        #         index +=1
        # numbers = [-1, 0] -> error

        # i, j = index, len(numbers)-1
        i, j = 0, len(numbers)-1
        while i<j:
            current = numbers[i] + numbers[j]
            if current == target:
                return [i+1, j+1]
            elif current > target:
                j -=1
            else:
                i +=1