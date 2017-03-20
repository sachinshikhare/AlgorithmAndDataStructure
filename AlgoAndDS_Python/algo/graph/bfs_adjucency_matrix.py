def bfs_graph_traversel(matrix, source):
    number_of_nodes = len(matrix[source])
    visited = [False]*number_of_nodes
    visited[source] = True
    
    queue = []
    queue.insert(0, source)
    t = ""
    while len(queue) > 0:
        node = queue.pop(0)
        t = t + str(node) + ","
        counter = 0
        while counter < len(matrix[node]):
            if matrix[node][counter] == 1 and not visited[counter]:
                visited[counter] = True
                queue.insert(len(queue), counter)
            counter+=1
            
    print("Traversal:", t)
                
matrix = [[0,1,0,1],[0,0,1,0],[0,1,0,1],[0,0,0,1]]
bfs_graph_traversel(matrix, 0)
bfs_graph_traversel(matrix, 1)
bfs_graph_traversel(matrix, 2)
bfs_graph_traversel(matrix, 3)
print()
matrix = [[0,1,0,1],[1,0,1,0],[0,1,0,1],[1,0,1,1]]
bfs_graph_traversel(matrix, 0)
bfs_graph_traversel(matrix, 1)
bfs_graph_traversel(matrix, 2)
bfs_graph_traversel(matrix, 3)