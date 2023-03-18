#Hanoi-n kipróbálni a szélességi keresést:
from hanoi import Hanoi
from search import breadth_first_tree_search

# Hanoi példányosítás
h = Hanoi(3)
print(h.size, h.initial, h.goal)

#Szélességi keresés futtatása
breadth_first_tree_search(h).solution()

#3 korsó szélességi kereséssel:
from cup3 import Cup3

"""
# 3 korsó példányosítása
c = Cup3((5,0,0), [(4,1,0)(4,0,1)],)
print(c.initial, c.goal)

# Szélességi keresés futtatása
breadth_first_tree_search(c).solution()
"""
#nem működik, nem tudom miért