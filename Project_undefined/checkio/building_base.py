class Building:
    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.south = south
        self.west = west
        self.width_WE = width_WE
        self.width_NS = width_NS
        self.height = height
        #raise NotImplementedError
        
    def corners(self):
        self.north = self.south + self.width_NS
        self.east = self.west + self.width_WE
        return {"north-west": [self.north, self.west], "north-east":[self.north, self.east], "south-west":[self.south, self.west], "south-east":[self.south, self.east]}
        raise NotImplementedError
        
    def area(self):
        return self.width_WE * self.width_NS
        raise NotImplementedError
        
    def volume(self):
        return self.width_WE * self.width_NS * self.height
        raise NotImplementedError
        
    def __repr__(self):
        return "Building({}, {}, {}, {}, {})".format(self.south, self.west, self.width_WE, self.width_NS, self.height)
        raise NotImplementedError
