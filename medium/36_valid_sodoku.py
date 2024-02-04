class Solution:
    
    def __init__(self):
        pass
    
    # [] = set
    # validate_sub_boxes = [[], [], [], [] , []] # To keep numbers of each sub-boxes
    # validate_columns = [[], [], []] # To keep numbers in each column
    # validate_rows = [[], [], []] # To keep numbers in each rows
    
    # iterate each column and store number to correlate cell and then we can validate at the end
    
    def get_sub_box(self, i: int, j: int) -> int:
        if i < 3 and j < 3:
            return 0
        elif i < 3 and j < 6:
            return 1
        elif i < 3 and j < 9:
            return 2
        elif i < 6 and j < 3:
            return 3
        elif i < 6 and j < 6:
            return 4
        elif i < 6 and j < 9:
            return 5
        elif i < 9 and j < 3:
            return 6
        elif i < 9 and j < 6:
            return 7
        else:
            return 8
    
    def is_valid_sudoku(self, board: list[list[str]]) -> bool:
        i, j = 0, 0
        
        len_row = len(board)
        len_col = len(board[i])
        
        # validate_rows = [set()] * 9 ---- Why it does not work ????
        # when I set one set, it apply to all set in the array ???
        validate_sub_boxes = [set(), set(), set(), set(), set(), set(), set(), set(), set()]
        validate_columns = [set(), set(), set(), set(), set(), set(), set(), set(), set()]
        validate_rows = [set(), set(), set(), set(), set(), set(), set(), set(), set()]
        
        while i < len_row:
            j = 0
            add_i = False
            while j < len_col:
                cur = board[i][j]       
                if cur != '.':
                    sub_box = self.get_sub_box(i, j)
                    
                    if cur in validate_columns[j]:
                        return False
                    else:
                        validate_columns[j].add(cur)
                            
                    if cur in validate_rows[i] and add_i == False:
                        return False
                    else:
                        validate_rows[i].add(cur)
                    
                    if cur in validate_sub_boxes[sub_box]:
                        return False
                    else:
                        validate_sub_boxes[sub_box].add(cur)
                
                j += 1
            i += 1
            
        return True
    
solution = Solution()

print(solution.is_valid_sudoku(
    [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
    ))
        