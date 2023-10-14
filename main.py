import json
from nodemanager import NodeManager
from consoledisplay import ConsoleDisplay
from helper import Helper

json_file = 'data.json'

#TODO: Node operations
#TODO: Node Visualisation
#TODO: Graph algorithms?
#TODO: values, 8, 9, 10, 11

if __name__ == "__main__":
    
    #NodeManager.add_node("G", ["A", "A", "G", "G"], json_file)
    #NodeManager.delete_node("G", json_file)
    #NodeManager.delete_connection("G", "R", json_file)
    #ConsoleDisplay.display_basic(json_file)  
    #ConsoleDisplay.display_matrix(json_file) 
    #ConsoleDisplay.display_matrix_ow(json_file)   
    #print(Helper.ordre(json_file))
    print(Helper.taille(json_file))
    
    with open(json_file, 'r+') as file:
        pass