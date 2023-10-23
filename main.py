from nodemanager import NodeManager
from consoledisplay import ConsoleDisplay
from helper import Helper
from algorithms import Algorithms

json_file = 'data.json'

#TODO: Node operations
#TODO: Node Visualisation
#TODO: Graph algorithms?
#TODO: values, 8, 9, 10, 11

#{"A": ["B", "C", "F"], "B": ["F"], "C": ["D"], "D": ["F", "E"], "E": ["F"], "F": ["G"], "G": []}
#{"A": ["B", "C"], "B": ["D"], "C": ["F"], "D": [], "F": []}

if __name__ == "__main__":
    
    #NodeManager.add_node("G", ["A", "A", "G", "G"], json_file)
    #NodeManager.delete_node("G", json_file)
    #NodeManager.delete_connection("G", "R", json_file)
    #ConsoleDisplay.display_basic(json_file)  
    #ConsoleDisplay.display_matrix(json_file) 
    ConsoleDisplay.display_matrix_ow(json_file)   
    #print(f'ordre: {Helper.ordre(json_file)}')
    #print(f'taille: {Helper.taille(json_file)}')
    #print(Algorithms.parcours_largeur('A', json_file))
    #print(Algorithms.parcours_profondeur('A', json_file))
    #print(Algorithms.composantes_connexes(json_file))
    print(Algorithms.topological_sort(json_file))
    
    
    with open(json_file, 'r+') as file:
        pass