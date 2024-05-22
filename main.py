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
points = np.array([[100, 100], [200, 100],
                   [200, 700], [100, 700]])
ref_points = np.array([[97, 97], [203, 97],
                       [203, 703], [97, 703]])
"""Поиск ближайшей точки до точки A"""
nearest_p = ref_points[0]
left_p = A
nearest_dist = 10000
for i in range(1, len(ref_points)):
    if nearest_dist > sqrt((left_p[0]-nearest_p[0])**2 - (left_p[1]-nearest_p[1])**2):
        nearest_dist = sqrt((left_p[0]-nearest_p[0])**2 - (left_p[1]-nearest_p[1])**2)
        nearest_p = ref_points[i-1]
        cv2.line(img, nearest_p, left_p, (0, 0, 255), 1)
    else:
        continue
"""Отрисовка фигуры и точек"""
cv2.fillPoly(img, pts=[points], color=(0, 0, 255))
for i in ref_points:
    image_point = cv2.circle(img, i, 0, (255, 0, 50), 2)

"""Вывод изображения"""
cv2.imshow("Rectangle", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
