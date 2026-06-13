from estruturas import Matriz, transpose

a = Matriz(2,3, [1,2,3,4,5,6])
b = transpose(a)

print(a)
print(b)


"""
1
10
4 1 0 0 0 0 0 0 0 0
1 4 1 0 0 0 0 0 0 0
0 1 4 1 0 0 0 0 0 0
0 0 1 4 1 0 0 0 0 0
0 0 0 1 4 1 0 0 0 0
0 0 0 0 1 4 1 0 0 0
0 0 0 0 0 1 4 1 0 0
0 0 0 0 0 0 1 4 1 0
0 0 0 0 0 0 0 1 4 1
0 0 0 0 0 0 0 0 1 4
5 6 6 6 6 6 6 6 6 5
"""
