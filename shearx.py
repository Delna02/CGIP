import numpy as np
import matplotlib.pyplot as plt
n = int(input("Enter the number of vertices: "))
points = []
for i in range(n):
    x = float(input(f"Enter the x-coordinate of vertex {i+1}: "))
    y = float(input(f"Enter the y-coordinate of vertex {i+1}: "))
    points.append((x, y))
factor = float(input("Enter the shear factor: "))
shear_matrix = np.array([[1, factor], [0, 1]])
sheared_points = []
for point in points:
    vector = np.array([[point[0]], [point[1]]])
    sheared_vector = np.dot(shear_matrix, vector)
    sheared_point = (sheared_vector[0][0], sheared_vector[1][0])
    sheared_points.append(sheared_point)
fig, ax = plt.subplots()
ax.set_aspect('equal', adjustable='box')
original_poly = plt.Polygon(points, fill=None, edgecolor='g')
ax.add_patch(original_poly)
sheared_poly = plt.Polygon(sheared_points, fill=None, edgecolor='b')
ax.add_patch(sheared_poly)
xmin = min([point[0] for point in points + sheared_points])
xmax = max([point[0] for point in points + sheared_points])
ymin = min([point[1] for point in points + sheared_points])
ymax = max([point[1] for point in points + sheared_points])
ax.set_xlim([xmin - 1, xmax + 1])
ax.set_ylim([ymin - 1, ymax + 1])
plt.show()

