from nodemanager import NodeManager
from consoledisplay import ConsoleDisplay
from helper import Helper
from algorithms import Algorithms
import json

json_file = 'data.json'

#TODO: Fortement connexe, Tri topologie
#TODO: values, 8, 9, 10, 11 (what the fuck does this mean)

#{"A": ["B", "C", "F"], "B": ["F"], "C": ["D"], "D": ["F", "E"], "E": ["F"], "F": ["G"], "G": []}
#{"A": ["B", "C"], "B": ["D"], "C": ["F"], "D": [], "F": []}

with open(json_file, 'r') as file:
    data = json.load(file)

graph = data.copy()

if __name__ == "__main__":
    
    #NodeManager.add_node("W", ["A"], graph)
    NodeManager.delete_node("F", graph)
    #NodeManager.delete_connection("G", "R", graph)
    #ConsoleDisplay.display_basic(graph)  
    #ConsoleDisplay.display_matrix(graph) 
    ConsoleDisplay.display_matrix_ow(graph)   
    #print(f'ordre: {Helper.ordre(graph)}')
    #print(f'taille: {Helper.taille(graph)}')
    #print(Algorithms.parcours_largeur('A', graph))
    #print(Algorithms.parcours_profondeur('A', graph))
    #print(Algorithms.composantes_connexes_faible(graph))

    with open(json_file, 'w') as file:
        json.dump(graph, file)