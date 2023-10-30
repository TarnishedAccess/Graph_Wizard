from nodemanager import NodeManager

class Algorithms:

    def parcours_largeur(starting_point, data):

        marked = [starting_point]
        working_file = [starting_point]
        result = []

        """
        #A little too easy?
        for node in working_file:
            for connection in data.get(node):
                if connection not in marked:
                    marked.append(connection)
                    working_file.append(connection)
        """

        while working_file:
            node = working_file[0]
            for connection in data.get(node):
                if connection not in marked:
                    marked.append(connection)
                    working_file.append(connection)
            #print(f"working file: {working_file}")
            #print(f"marked: {marked}")
            #print(f"result: {result}")
            result.append(node)
            working_file.pop(0)
        return result
        
    def parcours_profondeur(starting_point, data):

        marked = []
        working_file = [starting_point]
        result = []

        """
        #but no its too simple
        while len(working_file) != 0:
            node = working_file[0]
            for connection in data.get(node):
                if connection not in marked:
                    marked.append(connection)
                    #its like i MIGHT just be the goat
                    working_file.insert(1, connection)
            #print(f"working file: {working_file}")
            #print(f"marked: {marked}")
            #print(f"result: {result}")
            result.append(node)
            working_file.pop(0)
        """

        while working_file:
            node = working_file.pop()
            if node not in marked:
                marked.append(node)
                result.append(node)
                for connection in data.get(node):
                    if connection not in marked:
                        working_file.append(connection)
        return result
    

    def composantes_connexes_faible(data): 

        result = []
        for node in data:
            if node not in [item for sublist in result for item in sublist]:
                #sum(result, [])
                component = Algorithms.parcours_profondeur(node, data)
                result.append(component)
        return result

    def tritopologie(data):
        levels = []
        total_nodes = list(data.keys())
        while total_nodes:
            nodes_list = total_nodes.copy()
            for node_1 in data:
                for node_2 in data:
                    for connection in data.get(node_2, []):
                        if connection == node_1:
                            try:
                                nodes_list.remove(connection)
                            except ValueError:
                                pass
            levels.append(nodes_list)
            for node in nodes_list:
                total_nodes.remove(node)
                del data[node]
        print(levels)