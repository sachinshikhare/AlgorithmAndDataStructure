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
        return 
        
class DFSAdjucencyList:
    def __init__(self, is_directed_graph = True):
        self.graph = defaultdict(list)
        self.is_directed_graph = is_directed_graph

    def add_edge(self, u, v):
        self.graph[u].append(v)
        if not self.is_directed_graph:
            self.graph[v].append(u)
        
    def dfs_traversel(self, source):
        queue = []
        source.color = VisitedStatus.GRAY
        print(source.identifier, "is", source.color)
        source.distance = 0
        queue.append(source)
        
        while queue:
            node = queue.pop(0)
            for to_node in self.graph[node]:
                if to_node.color == VisitedStatus.WHITE:
                    to_node.color = VisitedStatus.GRAY
                    print(to_node.identifier, "is", to_node.color)
                    to_node.distance = node.distance + 1
                    to_node.pi = node
                    queue.append(to_node)
            node.color = VisitedStatus.BLACK
            print(node.identifier, "is", node.color)
            
class DFSAdjucencyListTester:
    def test(self):
        tester = DFSAdjucencyList()
        A = Vertex("A")
        B = Vertex("B")
        C = Vertex("C")
        D = Vertex("D")
        tester.add_edge(A, B)
        tester.add_edge(A, C)
        tester.add_edge(B, C)
        tester.add_edge(C, B)
        tester.add_edge(C, D)
        tester.add_edge(D, D)
        tester.dfs_traversel(A)
        print()
        tester.dfs_traversel(B)
        print()
        tester.dfs_traversel(C)
        print()
        tester.dfs_traversel(D)
        
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
        tester.dfs_traversel(A)
        print("----------------")
        for elem in list_of_vertices:
            print(elem.identifier, elem.color, elem.distance)
            if elem.pi:
                print(elem.pi.identifier)
                
    def test_3(self):
        A = Vertex("A")
        B = Vertex("B")
        C = Vertex("C")
        D = Vertex("D")
        E = Vertex("E")
        F = Vertex("F")
        G = Vertex("G")
        list_of_vertices = [A, B, C, D, E, F, G]
        tester = DFSAdjucencyList(False)
        tester.add_edge(A, B)
        tester.add_edge(C, B)
        tester.add_edge(D, B)
        tester.add_edge(E, F)
        tester.dfs_traversel(A)
        print("----------------")
        for elem in list_of_vertices:
            print(elem.identifier, elem.color, elem.distance)
            if elem.pi:
                print(elem.pi.identifier)
        
DFSAdjucencyListTester().test_3()