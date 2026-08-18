class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res, stackP, stackQ = [0], [temperatures[-1]], [1]
        for i in range(len(temperatures)-2, -1, -1):
            while stackP and temperatures[i] >= stackP[-1]:
                    stackP.pop()
                    stackQ.pop()

            stackP.append(temperatures[i])
            res.append(stackQ[-1] if stackQ else 0)
            stackQ = [x+1 for x in stackQ]
            stackQ.append(1)

        return res[::-1]