class Friends:
    def __init__(self, connections):
        self.connections = list(connections)

    def add(self, connection):
        if connection in self.connections:
            return False

        self.connections.append(connection)
        return True

    def remove(self, connection):
        if connection not in self.connections:
            return False

        self.connections.remove(connection)
        return True

    def names(self):
        flat = [n for f in self.connections for n in f]
        return set(flat)

    def connected(self, name):
        conn = [n for f in self.connections if name in f for n in f if n != name]
        return set(conn)
