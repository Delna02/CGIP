import numpy as ny
n = int(input("Enter the number of vertices: "))
points = []
for i in range(n):
    x = float(input(f"Enter the x-coordinate of point {i+1}: "))
    y = float(input(f"Enter the y-coordinate of point {i+1}: "))
    points.append((x, y))
factor = float(input("Enter the shear factor: "))
shear_matrix = ny.array([[1, factor], [0, 1]])
sheared_points = []
for point in points:
    vector = ny.array([[point[0]], [point[1]]])
    sheared_vector = ny.dot(shear_matrix, vector)
    sheared_point = (sheared_vector[0][0], sheared_vector[1][0])
    sheared_points.append(sheared_point)
print("Sheared points:")
for i, point in enumerate(sheared_points):
    print(f"Point {i+1}: ({point[0]}, {point[1]})")

