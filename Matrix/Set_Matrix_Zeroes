def setZeroes(matrix: list[list[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        pairs_of_zeros = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    pairs_of_zeros.append((i,j))

        print(pairs_of_zeros)
        for (i, j) in pairs_of_zeros:
            for k in range(m):
                matrix[k][j] = 0
            for z in range(n):
                matrix[i][z] = 0

        print(matrix)


matrix2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

setZeroes(matrix2)
