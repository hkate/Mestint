import numpy as np
from node_2 import Node
from collections import deque
from problem_2 import Problem

def trial_error(problem):
    state = Node(problem.initial)

    while True:
        if problem.goal_test(state.state):
            return state
 
        succesors=state.expand(problem)
        if len(succesors)==0:
            return 'Unsolvable'

        state=succesors[np.random.randint(0,len(succesors))]
        print(state)

def hill_climbing_for_3Cup(problem, heuristic):
    state = Node(problem.initial)

    while True:
        if problem.goal_test(state.state):
            return state

        succesors=state.expand(problem)

        test_succesors=[]
        for s_test in succesors:
            if heuristic(state.state)>=heuristic(s_test.state):
                test_succesors.append(s_test)

        if len(test_succesors)==0:
            return 'Unsolvable'

        state=test_succesors[np.random.randint(0,len(test_succesors))]

#actually egy fifo sor szelessegi kereses 
def breadth_first_tree(problem):
    #kezdo allapot kiolvasasa es fifo helyezése
    frontier = deque([Node(problem.initial)])

    #amig nem erulnk el hatart
    while frontier:
        
        #legszelsobb elem kiemelese
        node = frontier.popleft()

        #ha cel allapotban vagyunk akkor vege
        if problem.goal_test(node.state):
            return node
        
        #a kiemelt elembol az osszes uj allapot legyartasa az operatorok segitsegevel
        frontier.extend(node.expand(problem))

#actually egy verem melysegi kereses
def depth_first_tree(problem):
    #kezdo elem veremve helyezes
    frontier = ([Node(problem.initial)])
    #halmaz deklarálása a már bejárt elemhez
    explored = set()

    #amig tudunk melyre menni
    while frontier:
        
        #lefelso elem kiemelese a verembol
        node = frontier.pop()

        #ha cel allapotban vagyunk akkor vege
        if problem.goal_test(node.state):
            return node
        
        #allapot feljegyzese hogy mar tudjuk h jartunk itt
        explored.add(node.state)

        #verem bovitese a bejart elemekkel
        frontier.extend(child for child in node.expand(problem) if child.state not in explored and child not in frontier)


