from problem_2 import Problem
from node_2 import Node
from search_2 import hill_climbing_for_3Cup,trial_error,breadth_first_tree,depth_first_tree
from hanoi_2 import Hanoi
from cup3_2 import Cup3
from nqueen_2 import NQueens

nq4 = NQueens(4)
print(nq4.initial, nq4.goal)


print(trial_error(nq4))