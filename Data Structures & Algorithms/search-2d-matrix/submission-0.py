class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_cnt = len(matrix)
        col_cnt = len(matrix[0])
        l = 0
        r = row_cnt*col_cnt-1
        while(l <= r):
            mid = l+(r-l)//2
            row = mid//col_cnt
            col = mid%col_cnt
            if(matrix[row][col] < target):
                l = mid+1
            elif(matrix[row][col] > target):
                r = mid-1
            elif(matrix[row][col] == target):
                return True
        return False
                
