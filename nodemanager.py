import json

class NodeManager:
    
    def add_node(node, connections, storage_file):
        #this also by sheer accident handles adding connections to already existing nodes
        #TODO: this code is dogwater. Fix it.

        with open(storage_file, 'r') as file:
            data = json.load(file)
            
            #if the node already exists, we extend its connections
            if node in data.keys():
                for connection in connections:
                    #check each connection and only add if the node is valid and not a duplicate
                    if (connection not in data.get(node)) and (connection in data.keys()):
                        data[node].append(connection)

            #otherwise, we create it
            else:
                new_connections = []
                for connection in connections:
                    #check each connection and only add if the node is valid and not a duplicate
                    if ((connection in data.keys()) or (connection == node)) and (connection not in new_connections):
                        new_connections.append(connection)
                data[node] = new_connections

        with open(storage_file, 'w') as file:
            json.dump(data, file)

def delete_node(node, storage_file):

    with open(storage_file, 'r') as file:
        data = json.load(file)

    #if the node exists, we remove it.
    if node in data:
        data.pop(node)
        with open(storage_file, 'w') as file:
            json.dump(data, file)
            
def delete_connection(node, connection, storage_file):

    with open(storage_file, 'r') as file:
        data = json.load(file)

    #if both the node and the connection exist, we remove the connection
    if (node in data) and (connection in data.get(node)):
        data.get(node).remove(connection)
        with open(storage_file, 'w') as file:
            json.dump(data, file)    