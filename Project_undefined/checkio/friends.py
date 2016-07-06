class Friends:
    def __init__(self, connections):
        self.all_connection = list(connections)
    def add(self, connection):
        if connection in self.all_connection:
            return False
        else:
            self.all_connection.append(connection)
            return True
        
    def remove(self, connection):
        if connection in self.all_connection:
            self.all_connection.remove(connection)
            return True
        else:
            return False
            
    def names(self):
        return reduce(lambda a,b: a.union(b), self.all_connection)
        
    def connected(self, name):
        related = [pair for pair in self.all_connection if name in pair]
        if related:
            related = reduce(lambda a,b: a.union(b), related)
            related.remove(name)
            return related
        else:
            return set([])
