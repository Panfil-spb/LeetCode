class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            g = set()
            v = set()
            for j in range(len(board)):
                if board[i][j].isdigit():
                    if board[i][j] not in g:
                        g.add(board[i][j])
                    else:
                        return False
                if board[j][i].isdigit():
                    if board[j][i] not in v:
                        v.add(board[j][i])
                    else:
                        return False
                
                if i % 3 == 0 and j % 3 == 0:
                    s = set()
                    for k in range(i, i + 3):
                        for l in range(j, j + 3):
                            if board[k][l].isdigit():
                                if board[k][l] not in s:
                                    s.add(board[k][l])
                                else:
                                    return False
        return True

        