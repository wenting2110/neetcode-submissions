class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left_m, right_m = 0, m - 1
        left_n, right_n = 0, n - 1

        while left_m <= right_m:
            mid_m = (left_m + right_m) // 2

            if target > matrix[mid_m][-1]:
                left_m = mid_m + 1

            elif target < matrix[mid_m][0]:
                right_m = mid_m - 1

            else:
                while left_n <= right_n:
                    mid_n = (left_n + right_n) // 2
                    print(matrix[mid_m][mid_n])
                    if target == matrix[mid_m][mid_n]:
                        return True
                    elif target > matrix[mid_m][mid_n]:
                        left_n = mid_n + 1
                    else:
                        right_n = mid_n - 1

                return False

        return False
