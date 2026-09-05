class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                '''
                如果直接 res.append(cur)
                放進 res 裡的其實是 cur 的引用 (Reference / 記憶體位址)
                這會導致以下兩個主要問題：
                1. 修改連動：
                後續程式碼執行 cur.append(...) 或 cur.pop() 時，
                res 裡面已經存入的那個 List 內容也會跟著改變。
                
                2. 最終結果全部變空：
                當 DFS 遞迴全部執行完畢時，
                cur 會被一路 pop() 到變成空陣列 []。
                此時你會發現 res 裡面所有的組合全都變成了 []。
                '''
                return
            if i >= len(nums) or total > target:
                return
            
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res
