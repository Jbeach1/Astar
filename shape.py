class Node:
    def __init__(self, cord, shape):
        self.cord = cord
        self.shape = shape
        self.g = 0 # exact cost of node to goal ( total running cost )
        self.h = 0 # estimated cost from node to goal ( Euclidean )
        self.f = 0
        self.l = 0
        self.r = 0
        self.parent = 0