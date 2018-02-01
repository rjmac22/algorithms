import sys;

class Node(object):
    
    def __init__(self, name):
        self.name = name;
        self.visisted = False;
        self.ajacenciesList = [];
        self.predecessor = None;
        self.minDistance = sys.maxsize;
        