class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        count = len(board)
        for i in range(count):
            vertical = []
            for j in range(count):
                if board[j][i] in vertical and board[j][i] != '.':
                    return False
                elif board[j][i] != '.':
                    vertical.append(board[j][i])
            horizontal = []
            for j in range(count):
                if board[i][j] in horizontal and board[i][j] != '.':
                    return False
                elif board[i][j] != '.':
                    horizontal.append(board[i][j])
            
        #3x3
        for box_row in range(0, count, 3):
            for box_col in range(0, count, 3):
                box_seen = set()
                for i in range(3):
                    for j in range(3):
                        val = board[box_row + i][box_col + j]
                        if val != '.':
                            if val in box_seen:
                                return False
                            box_seen.add(val)



        return True