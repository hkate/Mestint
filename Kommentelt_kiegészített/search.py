#Hatékony csomag numerikus számításkhoz, n dimenziós tömbök kezeléséhez.
import numpy as np

#Csomópontok létrehozására szolgáló Node osztály
from node import Node
from collections import deque
from problem import Problem

#pórba hiba módszer
def trial_error(problem):
    #kezdő állapot
    state = Node(problem.initial)

    #végtelen ciklus definiálása
    while True:
        #Ha a probléma megoldva akkor leállítjuk a végtelen ciklusr
        if problem.goal_test(state.state):
            print('Got it')
            return state

        #Az alkalmazható operátorok segítségével
        #gyártsuk le az összes lehetséges utódot
        succesors = state.expand(problem)

        #Ha nincs új állapot(utód)
        if len(succesors)==0:
            return 'Unsolvable'

        #random választunk egy újat a legyártott utódok közül
        state=succesors[np.random.randint(0,len(succesors))]
        print(state)

def hill_climbing_for_3Cup(problem, heuristic):
    #kezdő állapot
    state = Node(problem.initial)

    #végtelen ciklus definiálása
    while True:
        #Ha a probléma megoldva akkor leállítjuk a végtelen ciklusr
        if problem.goal_test(state.state):
            return state

        #Az alkalmazható operátorok segítségével
        #gyártsuk le az összes lehetséges utódot
        succesors = state.expand(problem)

        #keresünk egy jobb állapotot a heurisztikának megfelelően
        test_succesors=[]
        for s_test in succesors:
            if heuristic(state.state)>=heuristic(s_test.state):
                test_succesors.append(s_test)

        #Ha nincs jobb állapot
        if len(test_succesors)==0:
            return 'Unsolvable'

        #ha több azonosan jó van akkor random választunk egyet
        state= test_succesors[np.random.randint(0,len(test_succesors))]

#actually egy fifo sor szelessegi kereses
def breadth_first_tree_search(problem): #breadth_first_tree Marcinak
    # kezdő állapot kiolvasása és FIFO sorba helyezése
    frontier = deque([Node(problem.initial)])

    # Amíg nem értük el a határt
    while frontier:
        # legszélsőbb elem kiemelése
        node = frontier.popleft()

        # ha cél állapotban vagyunk akkor vége
        if problem.goal_test(node.state):
            return node

        # A kiemelt elemből az össze új állapot legyártása az operátorok segítségével
        frontier.extend(node.expand(problem))

#méylségi keresés/bejárás
def depth_first_graph_search(problem): #depth_first_tree Marcinak
    # Kezdő elem verembe helyezése
    frontier = ([Node(problem.initial)])
    # halmaz deklarálása a már bejárt elemhez
    explored = set()

    # Amíg tudunk mélyebre menni
    while frontier:

        # Legelső elem kiemelése a veremből
        node = frontier.pop()

        # ha cél állapotban vagyunk vége
        if problem.goal_test(node.state):
            return node

        # állapot feljegyzése hogy tudjuk hogy már jártunk itt
        explored.add(node.state)

        # verem bővítése amíg benemjárt elemekkel
        frontier.extend(child for child in node.expand(problem)
                        if child.state not in explored and child not in frontier)

# Zárt csillag algoritmushoz best_first_graph_search bizbasz

def best_first_graph_search(problem, f):
    """A best-first kereső olyan keresőfával kereső, mely a legkisebb heurisztikájú nyílt csúcsot választja kiterjesztésre."""

    # kezdő állapot létrehozása
    node = Node(problem.initial)

    # priritásos (valamilyen heurisztika szerinte rendezett) sor létrehozása
    frontier = []

    # kezdő állapot felvétele a prioritásos sorba
    frontier.append(node)

    # halmaz létrehozása a már megvizsgált elemekhez
    explored = set()

    #amíg találunk elemet
    while frontier:
        # elem kivétele a verem tetejéről
        node = frontier.pop()

        # ha cél állapotban vagyunk akkor kész
        if problem.goal_test(node.state):
            return node

        # feldolgozott elemek bővítése
        explored.add(node.state)

        # operátorral legyártott gyermek elemek bejárása
        for child in node.expand(problem):
            # ha még nem dolgoztuk fel
            if child.state not in explored and child not in frontier:
                frontier.append(child)

            # Rendezzük a listát(sort) a heurisztikának megfelelően
            frontier = f(frontier)
            print(node.state)

# Zárt csillag algoritmus (egyik legjobb keresési algoritmus másolata, má változata?)

def astar_search(problem, f=None):
    """
    Az A* -algoritmus olyan A-algoritmusfajta, mely garantálja az optimális megoldás előállatását.
    h*(n) : az n-ből valamely célcsúcsba utás optimális költsége.
    g*(n) : a startcsúcsból n-be jutás optimális költsége.
    f*(n)=g*(n)+h*(n) : értelemszerűen startcsúcsból n-en keresztül valamely célcsúcs...
    """
    return best_first_graph_search(problem, f)