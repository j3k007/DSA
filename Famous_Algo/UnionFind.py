class UnionFind:
    def __init__(self):
        self.parents = {}

    def create(self, value):
        self.parents[value] = value

    def find(self, value):
        if value not in self.parents:
            return None
        while value != self.parents[value]:
            value = self.parents[value]
        return value

    def union(self, valueOne, valueTwo):
        if valueOne not in self.parents or valueTwo not in self.parents:
            return
        valueOneRoot = self.parents[valueOne]
        valueTwoRoot = self.parents[valueTwo]
        self.parents[valueOneRoot] = valueTwoRoot