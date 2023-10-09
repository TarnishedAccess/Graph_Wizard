import json
from nodemanager import NodeManager

if __name__ == "__main__":
    with open('data.json', 'r+') as file:
        data = json.load(file)
        NodeManager.add_node("G", ["A", "A", "G", "G"], 'data.json')
        #delete_node("G", 'data.json')
        #delete_connection("G", "R", "data.json")
        for node, neighbors in data.items():
            print(f"Node {node} is connected to: {neighbors}")    