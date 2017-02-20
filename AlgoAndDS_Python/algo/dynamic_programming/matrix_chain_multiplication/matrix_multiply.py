matrix_a = [[x*y for x in range(1, 11)] for y in range(1, 16)]
matrix_b = [[x+y for x in range(1, 16)] for y in range(1, 11)]

# matrix_a = [[1,2],[3,4],[5,6]]
# matrix_b = [[1,2,3],[4,5,6]]

def multiply_matrices(matrix_a, matrix_b):
    
    if len(matrix_a[0]) != len(matrix_b):
        print("Multiplication not possible")
        return None
    
    result_matrix = [[0 for _ in range(len(matrix_a))] for _ in range(len(matrix_b[0]))]
    for row in range(len(matrix_a)):
        for column in range(len(matrix_b[0])):
            for cntr in range(len(matrix_a[0])):
                result_matrix[row][column] += matrix_a[row][cntr] * matrix_b[cntr][column]
            
    return result_matrix

print(multiply_matrices(matrix_a, matrix_b))