import json
from nodemanager import NodeManager
from consoledisplay import ConsoleDisplay

json_file = 'data.json'

#TODO: Node operations
#TODO: Node Visualisation
#TODO: Graph algorithms?

if __name__ == "__main__":
    
    #NodeManager.add_node("G", ["A", "A", "G", "G"], json_file)
    #NodeManager.delete_node("G", json_file)
    #NodeManager.delete_connection("G", "R", json_file)
    #ConsoleDisplay.display_basic(json_file)  
    ConsoleDisplay.display_matrix(json_file)  
    
    with open(json_file, 'r+') as file:
        pass