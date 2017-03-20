from collections import defaultdict

class VisitedStatus:
    WHITE = "Not visited at all"
    GRAY = "Visited partially"
    BLACK = "Visited completely"

class Vertex:
    def __init__(self, identifier=None):
        self.color = VisitedStatus.WHITE
        self.identifier = identifier
        self.distance = float("inf")
        self.pi = None
        
    def __str__(self):
        return self.identifier
        
class DFSAdjucencyList:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        

    def dfs_visit(self, vertex):
        print("Nodes in graph:", len(self.graph))
        
        vertex.color = VisitedStatus.GRAY
        print(vertex.identifier, "is", vertex.color)
        if vertex in self.graph and self.graph[vertex]:
            for adjcent in self.graph[vertex]:
                if adjcent.color == VisitedStatus.WHITE:
                    print(self.graph)
                    adjcent.pi = vertex
                    self.dfs_visit(adjcent)
        vertex.color = VisitedStatus.BLACK
        
        print(vertex.identifier, "is", vertex.color)
        
    def __str__(self):
        string = ""
        for node in self.graph:
            string = string + ", " + node.identifier
        return string
    
    def dfs_traversel(self):
        
        for vertex in self.graph:
            if vertex.color == VisitedStatus.WHITE:
                self.dfs_visit(vertex)
            
class DFSAdjucencyListTester:
        
    def test2(self):
        A = Vertex("A")
        B = Vertex("B")
        C = Vertex("C")
        D = Vertex("D")
        E = Vertex("E")
        F = Vertex("F")
        G = Vertex("G")
        I = Vertex("I")
        J = Vertex("J")
        list_of_vertices = [A, B, C, D, E, F, G, I, J]
        tester = DFSAdjucencyList()
        tester.add_edge(A, D)
        tester.add_edge(D, A)
        tester.add_edge(A, B)
        tester.add_edge(B, I)
        tester.add_edge(E, G)
        tester.add_edge(D, E)
        tester.add_edge(C, F)
        tester.add_edge(F, C)
        tester.add_edge(A, G)
        tester.add_edge(G, J)
        tester.add_edge(F, J)
        tester.add_edge(F, I)
        tester.add_edge(I, D)
        tester.dfs_traversel()
        print("----------------")
        for elem in list_of_vertices:
            print(elem.identifier, elem.color, elem.distance)
            if elem.pi:
                print(elem.pi.identifier)

        
DFSAdjucencyListTester().test2()