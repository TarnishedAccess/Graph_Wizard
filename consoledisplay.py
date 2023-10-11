import json
import pandas

class ConsoleDisplay:
    
    def display_basic(storage_file):
        with open(storage_file, 'r+') as file:
            data = json.load(file)
            for node, neighbors in data.items():
                print(f"Node {node} is connected to: {neighbors}")    

    def display_matrix(storage_file):
        with open(storage_file, 'r') as file:
            data = json.load(file)
            nodes = list(data.keys())
            matrix = [[0 for x in range(len(nodes))] for x in range(len(nodes))]
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    if nodes[j] in data.get(nodes[i]):
                        matrix[i][j] = 1 

        #Data, Y labels, X labels        
        df = pandas.DataFrame(matrix, columns=nodes, index=nodes)
        print(df)