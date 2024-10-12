from datastructures import *

#----------------------------------------------------------------------

class Node:
    """
    This class is used to represent nodes of the search tree.  Each
    node contains a state representation, a reference to the node's
    parent node, a string that describes the action that generated
    the node's state from the parent state, the path cost g from
    the start node to this node, and the estimated path cost h
    from this node to the goal node.
    """
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action
        self.g = 0
        self.h = 0

    def __eq__(self, other):
        if other:
            return self.state == other.state
        else:
            return False
    
    def expand(self):
        successors = []
        for (newState, action) in self.state.next_states():
            newNode = Node(newState, self, action)
            successors.append(newNode)
        return successors

#----------------------------------------------------------------------

def uninformed_search(initial_state, goal_state, frontier):
    """
    Implementación de búsqueda no informada usando Graph-Search.
    Utiliza la estructura de datos que se le pasa en 'frontier' para manejar los nodos.
    """
    initial_node = Node(initial_state, None, None)
    frontier.insert(initial_node) 
    explored = set() 
    expanded = 0 
    generated = 0 
    
    while not frontier.is_empty():
        node = frontier.remove()  # Extrae el siguiente nodo de la frontera
        if node.state == goal_state:
            return (node, expanded, generated)  # Si encontramos el objetivo, terminamos
        explored.add(node.state) 
        expanded += 1
        for child in node.expand():  # Expandimos el nodo
            g = node.g + 1
            if child.state not in explored and not frontier.contains(child): 
                frontier.insert(child)  # Añadimos el nuevo nodo a la frontera
                generated += 1 

    return (None, expanded, generated) 

#----------------------------------------------------------------------
# Test functions for uninformed search

def breadth_first(initial_state, goal_state):
    frontier = Queue()  # Utilizar una cola para la búsqueda en anchura
    return uninformed_search(initial_state, goal_state, frontier)

def depth_first(initial_state, goal_state):
    frontier = Stack() #Indicar estructura de datos adecuada para depth_first
    return uninformed_search(initial_state, goal_state, frontier)

def uniform_cost(initial_state, goal_state):
    frontier = PriorityQueue(lambda x: 1) #Indicar estructura de datos adecuada para uniform_cost
    return uninformed_search(initial_state, goal_state, frontier)


#----------------------------------------------------------------------

def informed_search(initial_state, goal_state, frontier, heuristic):
    initial_node = Node(initial_state, None, None)
    initial_node.h = heuristic(initial_state, goal_state)
    frontier.insert(initial_node)
    explored = set()
    expanded = 0
    generated = 0
    
    while not frontier.is_empty():
        node = frontier.remove()
        if node.state == goal_state:
            return (node, expanded, generated)
        
        explored.add(node.state)
        expanded += 1
        
        for child in node.expand():
            child.g = node.g + 1
            child.h = heuristic(child.state, goal_state)
            if child.state not in explored and not frontier.contains(child):
                frontier.insert(child)
                generated += 1

    return (None, expanded, generated)

    """
    Parametros:
       initial_state: estado inicial de busqueda (objeto de clase MissionariesState)
       goal_state: estado inicial de busqueda (objeto de clase MissionariesState)
       frontier: estructura de datos para contener los estados de la frontera (objeto de clase
           contenida en el modulo DataStructures)
       heuristic: funcion heuristica utilizada para guiar el proceso de busqueda. La
           funcion recibe dos parametros (estado actual y estado objetivo) y devuelve
           una estimacion de coste entre ambos estados
    """

    initial_node = Node(initial_state, None, None)
    expanded = 0
    generated = 0

    """
    Rellenar con el codigo necesario para realizar una busqueda no informada
    siguiendo el pseudocodigo de los apuntes (Graph-Search), modificada para
    actualizar el valor heuristico (h) de los nodos
    La funcion debe devolver una tupla con 3 variables:
        1. Nodo del grafo con el estado objetivo (None si no se ha alcanzado el objetivo)
        2. Numero de nodos expandidos (expanded)
        3. Numero de nodos generados (generated)
    """
    
    return (None, expanded, generated)
    
#----------------------------------------------------------------------
# Test functions for informed search

def greedy(initial_state, goal_state, heuristic):
    frontier = PriorityQueue(lambda node: node.h)  # La prioridad es solo la heurística
    return informed_search(initial_state, goal_state, frontier, heuristic)


def a_star(initial_state, goal_state, heuristic):
    frontier = PriorityQueue(lambda node: node.g + node.h) 
    return informed_search(initial_state, goal_state, frontier, heuristic)

#---------------------------------------------------------------------
# Heuristic functions

"""
def h1(current_state, goal_state):
    people_left = current_state.miss[0] + current_state.cann[0]
    return (people_left + current_state.capacity - 1) // current_state.capacity
"""
def h1(current_state, goal_state):
    # Sumar el número de misioneros y caníbales en la orilla izquierda
    people_left = current_state.miss[0] + current_state.cann[0]
    
    trips = (people_left + current_state.capacity - 1) // current_state.capacity
    
    if current_state.boat_position == "right" and people_left > 0:
        trips += 1
    
    return trips

#----------------------------------------------------------------------

def show_solution(node, expanded, generated):
    path = []
    while node != None:
        path.insert(0, node)
        node = node.parent
    if path:
        print ("Solution took %d steps" % (len(path) - 1))
        print (path[0].state)
        for n in path[1:]:
            print ('%s %s %s' % (n.action[0], n.action[1], n.action[2]))

            print (n.state)
    print ("Nodes expanded:  %d" % expanded)
    print ("Nodes generated: %d\n" % generated)

