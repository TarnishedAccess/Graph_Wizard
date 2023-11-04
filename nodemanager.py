from node import Node

class NodeManager:

    @staticmethod
    def add_node(node, connections, nodes):
        if node in nodes:
            existing_node = nodes[node]
            for connection in connections:
                if connection in nodes and connection not in existing_node.connections:
                    existing_node.add_connection(nodes[connection])
        else:
            new_node = Node(node)
            nodes[node] = new_node
            for connection in connections:
                if connection in nodes:
                    new_node.add_connection(nodes[connection])

    @staticmethod
    def delete_node(node_label, nodes):
        if node_label in nodes:
            node = nodes[node_label]
            for connected_node in nodes.values():
                connected_node.connections = [n for n in connected_node.connections if n != node]
            del nodes[node_label]

    @staticmethod
    def delete_connection(node_label, connection_label, nodes):
        if node_label in nodes and connection_label in nodes:
            node = nodes[node_label]
            connection = nodes[connection_label]
            node.connections = [n for n in node.connections if n != connection]

