class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        cur = []
        res = False
        
        def dfs(i, j, k):
            print(i, j, k)
            nonlocal res
            if k == len(word):
                res = True
                return
            for l in range(-1, 2):
                if  -1 < i + l < len(board):
                    if word[k] == board[i + l][j] and (i + l, j) not in cur:
                        cur.append((i + l, j))
                        dfs(i + l, j, k + 1)
                        cur.pop()
                    
                if  -1 < j + l < len(board[0]):
                    if word[k] == board[i][j + l] and (i, j + l) not in cur:
                        cur.append((i, j + l))
                        dfs(i, j + l, k + 1)
                        cur.pop()
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j]:
                    cur.append((i, j))
                    dfs(i, j, 1)
                    cur.pop()
                    print(res)
                    if res == True:
                        break
        return res
        