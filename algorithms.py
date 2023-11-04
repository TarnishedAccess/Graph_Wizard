from nodemanager import NodeManager

class Algorithms:

    @staticmethod
    def parcours_largeur(starting_node, nodes):
        marked = [starting_node]
        working_queue = [starting_node]
        result = []

        while working_queue:
            current_node = working_queue.pop(0)
            node = nodes[current_node]
            for connection, weight in node.connections:
                if connection.label not in marked:
                    marked.append(connection.label)
                    working_queue.append(connection.label)
            result.append(current_node)
        return result

    @staticmethod
    def parcours_profondeur(starting_node, nodes):
        marked = set()
        working_stack = [starting_node]
        result = []

        while working_stack:
            current_node = working_stack.pop()
            if current_node not in marked:
                marked.add(current_node)
                result.append(current_node)
                node = nodes[current_node]
                for connection, weight in node.connections:
                    working_stack.append(connection.label)
        return result

    @staticmethod
    def composantes_connexes_faible(nodes):
        result = []
        visited = set()

        for node_label, node in nodes.items():
            if node_label not in visited:
                component = Algorithms.parcours_profondeur(node.label, nodes)
                result.append(component)
                visited.update(component)
        return result

    @staticmethod
    def tritopologie(data):
        levels = []
        total_nodes = list(data.keys())
        connections = {node.label: [(conn.label, weight) for conn, weight in node.connections] for node in data.values()}

        while total_nodes:
            nodes_list = total_nodes.copy()
            for node_1 in data:
                for node_2, _ in connections.get(node_1, []):
                    try:
                        nodes_list.remove(node_2)
                    except ValueError:
                        pass
            levels.append(nodes_list)
            for node in nodes_list:
                total_nodes.remove(node)
                del data[node]
        return levels






