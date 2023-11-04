from node import Node

class NodeManager:

    @staticmethod
    def add_node(node, connections, nodes):
        existing_node = nodes.get(node)
        if existing_node:
            for connection, weight in connections:
                if connection in nodes and connection not in [c[0] for c in existing_node.connections]:
                    existing_node.add_connection(nodes[connection], weight)
        else:
            new_node = Node(node)
            nodes[node] = new_node
            for connection, weight in connections:
                if connection in nodes:
                    new_node.add_connection(nodes[connection], weight)

    @staticmethod
    def delete_node(node_label, nodes):
        node = nodes.get(node_label)
        if node:
            for connected_node in nodes.values():
                connected_node.connections = [(n, w) for n, w in connected_node.connections if n != node]
            del nodes[node_label]

    @staticmethod
    def delete_connection(node_label, connection_label, nodes):
        node = nodes.get(node_label)
        connection = nodes.get(connection_label)
        if node and connection:
            node.connections = [(n, w) for n, w in node.connections if n != connection]
