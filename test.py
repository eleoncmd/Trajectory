import cv2
import numpy as np

# Создаем граф
graph = np.array([
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
])

# Создаем матрицу расстояний
distance = np.full((graph.shape[0], graph.shape[1]), np.inf)
distance[0][0] = 0

# Создаем матрицу предшественников
prev = np.full((graph.shape[0], graph.shape[1]), -1)

# Алгоритм Дейкстры
for _ in range(graph.shape[0] * graph.shape[1]):
    min_dist = np.inf
    min_index = -1
    for i in range(graph.shape[0]):
        for j in range(graph.shape[1]):
            if distance[i][j] < min_dist and graph[i][j] != 0:
                min_dist = distance[i][j]
                min_index = (i, j)
    if min_index == -1:
        break
    distance[min_index[0]][min_index[1]] = np.inf
    for i in range(graph.shape[0]):
        for j in range(graph.shape[1]):
            if graph[i][j] != 0 and distance[i][j] > distance[min_index[0]][min_index[1]] + graph[i][j]:
                distance[i][j] = distance[min_index[0]][min_index[1]] + graph[i][j]
                prev[i][j] = min_index

# Вывод кратчайшего пути
path = []
current = (7, 7)
while current != (0, 0):
    path.append(current)
    current = prev[current[0]][current[1]]
path.append((0, 0))
path.reverse()
print(path)

# Вывод кратчайшего расстояния
print(distance[7][7])