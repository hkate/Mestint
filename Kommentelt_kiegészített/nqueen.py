from problem import Problem #absztrakciója az állapottér reprezentációnak
# result és actions minden esetben megírandó, anélkül nem lehet dolgozni

class NQueens(Problem):
    """N királynő elhelyezésének problémája egy NxN táblán úgy, hogy egyik sem üti a másikat.
    Egy állapotot N elemű tömbbként ábrázolunk, ahol a c-edik bejegyzésben szereplő r értéke azt jelenti a c oszlopban, az r sorban van
    egy királynő, a -1 érték pedig azt, hogy a c-edik oszlop még nem lett kitöltve.
    Balról jobbra töltjük ki az oszlopokat"""

    def __init__(self, N):
        super().__init__(tuple([-1] * N))
        self.N = N

    def actions(self, state):
        """A bla szélső üres oszlopban ki az összes nem ütköző sort."""
        if state[-1] != -1:
            return [] # Minden oszlop kitöltve;
        else:
            col = state.index(-1)
            return [row for row in range(self.N)
                    if not self.conflicted(state, row, col)]

    def result(self, state, row):
        """Helyezze a következő királynőt a megadott sorba."""
        col = state.index(-1)
        new = list(state[:])
        new[col] = row
        return tuple(new)

    def conflicted(self, state, row, col):
        return any(self.conflict(row, col, state[c], c)
                   for c in range(col))

    def conflict(self, row1, col1, row2, col2): # megnézi hol van ütés
        """összeütközésbe kerülbe két királynő elhelyezése (sor1, oszlop1) és (sor2, oszlop2)?"""
        return(row1 == row2 or # ugyanabban a sorban
               col1 == col2 or # ugyanabban az oszlopban
               row1 - col1 == row2 - col2 or # ugyanabban az átlóban, irány: \
               row1 + col1 == row2 + col2) # ugyanabban az átlóban, irány: /

    def goal_test(self, state):
        """Ellenőrizze, hogy minden oszlop megtelt e és nincsen ütközés."""
        if state[-1] == -1:
            return False
        return not any(self.conflicted(state, state[col], col)
                       for col in range(len(state)))

    # meg kell próbálni példányosítani az osztlytés kezdő cél álapotot adni neki / definiálni