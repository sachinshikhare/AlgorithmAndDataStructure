'''
Created on 14-Apr-2017

@author: sachin
'''
from algo.ads.disjoint_sets.disjoint_set import DisjointSet

class Edge:
    def __init__(self, vertex_1, vertex_2, weight):
        self.vertex_1 = vertex_1
        self.vertex_2 = vertex_2
        self.weight = weight
        
class Graph:
    def __init__(self, edges, vertices):
        self.edges = edges
        self.vertices = vertices

class TesterForMSTKruskal:
    
    def prepare_test_data(self):
        vertices = ['a','b','c','d','e','f']
        edges = [Edge('a','b',4),
             Edge('b','c',6),
             Edge('c','d',3),
             Edge('d','e',2),
             Edge('e','f',4),
             Edge('a','f',2),
             Edge('b','f',5),
             Edge('c','f',1)]
        self.graph = Graph(edges, vertices)
        
    def calculate_mst_using_kruskal(self):
        mst = []
        disjoint_set = DisjointSet()
        for vertex in self.graph.vertices:
            disjoint_set.make_set(vertex)
        self.graph.edges = sorted(self.graph.edges, key=lambda edge: edge.weight)
        for edge in self.graph.edges:
            if disjoint_set.find_set(edge.vertex_1) != disjoint_set.find_set(edge.vertex_2):
                mst.append(edge)
                disjoint_set.union(edge.vertex_1, edge.vertex_2)
        return mst
    
tester = TesterForMSTKruskal()
tester.prepare_test_data()
mst = tester.calculate_mst_using_kruskal()

for edge in mst:
    print("vertex 1: {0}, vertex 2: {1}, weight: {2}".format(edge.vertex_1, edge.vertex_2, edge.weight))
