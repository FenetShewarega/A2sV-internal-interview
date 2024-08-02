class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.isValidArray(row):
                return False
        
        for col in range(9):
            if not self.isValidArray([board[row][col] for row in range(9)]):
                return False
        
        for i in range(3):
            for j in range(3):
                sub_box = [board[row][col]for row in range(i*3, (i+1)*3) for col in range(j*3, (j+1)*3)]
                if not self.isValidArray(sub_box):
                    return False
        
        return True
    
    def isValidArray(self, arr: List[str]) -> bool:
        seen = set()
        for val in arr:
            if val != '.' and val in seen:
                return False
            seen.add(val)
        return True