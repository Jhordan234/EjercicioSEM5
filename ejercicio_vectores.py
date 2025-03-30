import numpy as np

# Definir vectores
v1 = np.array([2, 3])
v2 = np.array([1, -1])

# Suma y resta de vectores
suma = v1 + v2
resta = v1 - v2

# Producto escalar
producto_escalar = np.dot(v1, v2)

# Definir matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[2, 0], [1, 3]])

# Suma de matrices
suma_matrices = A + B

# Producto de matrices
producto_matrices = np.dot(A, B)

# Matriz inversa
inversa_A = np.linalg.inv(A)

# Autovalores y autovectores
autovalores, autovectores = np.linalg.eig(A)

# Imprimir resultados
print("Suma de vectores:", suma)
print("Resta de vectores:", resta)
print("Producto escalar:", producto_escalar)
print("Suma de matrices:\n", suma_matrices)
print("Producto de matrices:\n", producto_matrices)
print("Matriz inversa de A:\n", inversa_A)
print("Autovalores de A:", autovalores)
print("Autovectores de A:\n", autovectores)