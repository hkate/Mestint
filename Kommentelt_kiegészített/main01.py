from problem import Problem
from node import Node
from cup3 import Cup3
from search import hill_climbing_for_3Cup

problem = Problem((5,0,0), [(4,1,0),(4,0,1)])
problem.initial, problem.goal

state1 = Node(1)
type(state1)

# __repr__
state2 = Node(state=2, parent=state1)

# print(state2)
state2

# __eq__
print(state1 is object)
False

# __lt__
if state1 > state2:
    print("state1 a nagyobb")
elif state1 < state2:
    print("state2 a nagyobb")
else:
    print("Egyenlőek")

# __hash__
state1 = Node(1)
hash(state1)

########################

c = Cup3((5,0,0), [(4,1,0), (4,0,1)])

#######################

#A heurisztika lényeg az hogy ha minél több üres korsót találunk
#annál távolabb vagyunk a megoldástól
def heuristic_calc_emtpy_jar(State):
    if State==(4,0,1) or State==(4,1,0):
        return 0
    c=0
    for i in State:
        if i == 0:
            c+=1
    return c+1

print(hill_climbing_for_3Cup(c, heuristic_calc_emtpy_jar).solution())

from hanoi import Hanoi

h = Hanoi(3)
h.size, h.initial, h.goal

from search import trial_error
trial_error(h).solution()