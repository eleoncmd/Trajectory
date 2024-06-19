import cv2
import numpy as np
from math import *

"""Читаем изображение"""
path = r'BLACKOUT.jpg'
img = cv2.imread(path)
cv2.cvtColor(img[..., ::-1], cv2.COLOR_RGB2BGR)
"""Иницализация точки A и B"""
A = np.array([10, 10])
B = np.array([300, 300])
cv2.circle(img, A, 0, (0, 255, 255), 3)
cv2.circle(img, B, 0, (0, 255, 255), 3)
"""Инициализация точек прямоугольника и опорных точек"""
points = np.array([
    [100, 100], [200, 100],
    [200, 700], [100, 700]
])
ref_points = np.array([
    [10, 10], [97, 97],
    [203, 97], [203, 703],
    [97, 703], [300, 300]
])
"""Инциализация матрицы расстояний"""
distance = np.full((ref_points.shape[0], ref_points.shape[1]), np.inf)
print(distance)
distance[0][0] = 0
print(distance)
"""Матрица предшественников"""
prev = np.full((ref_points.shape[0], ref_points[1]), -1)
"""Отрисовка контурных точек"""
for i in ref_points:
    image_point = cv2.circle(img, i, 0, (255, 0, 50), 2)

"""Поиск ближайшей точки до точки A"""
# nearest_p = ref_points[0]  # [97, 97]
# signal = False
# print(len(ref_points))  # 4

# for j in range(-1, len(ref_points) + 1):  # (-1, 3)
#     print('j', j)
#     if j < 0:  # j= -1
#         start = A  # start = [10, 10]
#         print('start:', start)
#     elif j >= len(ref_points):
#         start = B
#         signal = True
#     else:
#         start = ref_points[j]
#         print('startelse:', start)
#     for i in range(1, len(ref_points)):
#         if (ref_points[i][0] == start[0]) and (ref_points[i][1] == start[1]):
#             dist_prev = sqrt((ref_points[i][0] - start[0]) ** 2 + (ref_points[i][1] - start[1]) ** 2)
#             continue
#         dist_prev = sqrt((nearest_p[0] - start[0]) ** 2 + (nearest_p[1] - start[1]) ** 2)
#         print('dist_prev', dist_prev)  # 123.03657992645927
#         dist_temp = sqrt((ref_points[i][0] - start[0]) ** 2 + (ref_points[i][1] - start[1]) ** 2)
#         print('dist_temp', dist_temp)  # 123.03657992645927
#         if dist_prev >= dist_temp and abs(dist_prev - dist_temp) != 0:
#             nearest_p = ref_points[i]
#             print('near:', nearest_p)
#             print('i', i)
#             print('ifstart', start)
#         print('starti:', start)
#         print('nearest_p:', nearest_p)
#     cv2.line(img, nearest_p, start, (255, 255, 255), 1)

path = []
current = (7, 7)
while current != (0, 0):
    path.append(current)
    current = prev[current[0]][current[1]]
path.append((0, 0))
path.reverse()
print(path)

"""Отрисовка фигуры и точек"""
cv2.fillPoly(img, pts=[points], color=(0, 0, 255))
"""Вывод изображения"""
cv2.imshow("Rectangle", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
