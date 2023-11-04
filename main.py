from nodemanager import NodeManager
from consoledisplay import ConsoleDisplay
from helper import Helper
from algorithms import Algorithms
from node import Node
import json

json_file = 'data.json'

#TODO: Fortement connexe

#{"A": ["B", "C", "F"], "B": ["F"], "C": ["D"], "D": ["F", "E"], "E": ["F"], "F": ["G"], "G": []}
#{"A": ["B", "C"], "B": ["D"], "C": ["F"], "D": [], "F": []}
#{"A": ["B", "C"], "B": ["D"], "C": [], "D": [], "X": ["Y"], "Y": []}

with open(json_file, 'r') as file:
    data = json.load(file)

graph = data.copy()

if __name__ == "__main__":
    
    nodes = {}

    # First, add all nodes
    for node_label in data.keys():
        node = Node(node_label)
        nodes[node_label] = node

    for node_label, connections in data.items():
        for connection_label, weight in connections:
            nodes[node_label].add_connection(nodes[connection_label], weight)

    #NodeManager.delete_node("F", graph)
    #NodeManager.delete_connection("G", "R", graph)
    #print(nodes)
    ConsoleDisplay.display_matrix_ow(nodes)   
    #print(f'ordre: {Helper.ordre(nodes)}')
    #print(f'taille: {Helper.taille(nodes)}')
    #print(Algorithms.parcours_largeur('A', nodes))
    #print(Algorithms.parcours_profondeur('A', nodes))
    #print(Algorithms.composantes_connexes_faible(nodes))
    print(Algorithms.tritopologie(nodes))

    """
    with open(json_file, 'w') as file:
        json.dump(graph, file)
    """