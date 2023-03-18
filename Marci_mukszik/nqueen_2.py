from problem_2 import Problem

class NQueens(Problem):

    def __init__(self, N):
        super().__init__(tuple([-1]*N))
        self.N = N

    def actions(self, state):
        if state[-1] != -1:
            return []
        else:
            col = state.index(-1)
            return [row for row in range(self.N)
                    if not self.conflicted(state, row, col)]
    def result(self, state, row):
        """helyezze a kiralynot a megadott sorban"""
        col = state.index(-1)
        new = list(state[:])
        new[col] = row
        return tuple(new)
    
    def conflicted(self, state, row, col):
        return any(self.conflict(row, col, state[c], c)
                   for c in range(col))
    
    def conflict(self, row1, col1, row2, col2):
        """osszeutkozesbe kerulne ket kiralyno elhelyezese(sor1 oszlop1) es (sor2 oszlop2)"""
        return(row1 == row2 or
               col1 == col2 or
               row1 - col1 == row2 - col2 or
               row1 + col1 == row2 + col2)
    
    def goal_test(self, state):
        """ellenorzs h minden oszlop megtelt-e es nincs utkozes"""
        if state[-1] == -1:
            return False
        return not any(self.conflicted(state, state[col], col)
                       for col in range(len(state)))