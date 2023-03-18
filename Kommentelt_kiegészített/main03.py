from nqueen import NQueens

# nqueen kezdő és célállapot kiírása
nq4 = NQueens(4)
print(nq4.initial, nq4.goal)

# trial-erroral nézzük meg hogyan néz ki

from search import trial_error

#nq4 = NQueens(4)
#print(nq4.initial, nq4.goal)
trial_error(nq4) # nem mindig ugyan azt a választ adja, vn h megtudja oldani van hogy nem

from search import breadth_first_tree_search
from search import depth_first_graph_search

#szélességi és mélységi keresést is megpróbálni

breadth_first_tree_search(nq4) #szélességi
depth_first_graph_search(nq4) # mélységi

# ez nem egy optimális heurisztika!
# az út költsége legyen 1 és válasszuk mindig a legnagyobb indexű...
def sort_by_heur(items):
    """Válasszuk mindig a lehető legnagyobb indexű sort"""
    return sorted(items, key=lambda x: sum(x.state))
# a heurisztika má majdnem olyan jó mint a random

# 4 királynő - A* algoritmussal
from search import astar_search

#nq4 = NQueens(4)
#print(nq4.initial, nq4.goal)
print(astar_search(nq4, sort_by_heur))