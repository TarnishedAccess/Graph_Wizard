import json
import pandas

class ConsoleDisplay:
    
    def display_basic(data):
        for node, neighbors in data.items():
            print(f"Node {node} is connected to: {neighbors}")    

    def display_matrix(data):
        nodes = list(data.keys())
        matrix = [[0 for x in range(len(nodes))] for x in range(len(nodes))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if nodes[j] in data.get(nodes[i]):
                    matrix[i][j] = 1 
        #Data, Y labels, X labels        
        df = pandas.DataFrame(matrix, columns=nodes, index=nodes)
        print(df)

    def display_matrix_ow(data):
        nodes = list(data.keys())
        matrix = [[0 for x in range(len(nodes))] for x in range(len(nodes))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if nodes[j] in data.get(nodes[i]):
                    matrix[i][j] = 1 
                    #matrix[j][i] = -1
        df = pandas.DataFrame(matrix, columns=nodes, index=nodes)
        print(df)