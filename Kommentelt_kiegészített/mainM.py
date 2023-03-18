from problem import Problem
from node import Node
from search import hill_climbing_for_3Cup,trial_error,breadth_first_tree_search,depth_first_graph_search
from hanoi import Hanoi
from cup3 import Cup3
from nqueen import NQueens

nq4 = NQueens(4)
print(nq4.initial, nq4.goal)


print(trial_error(nq4))