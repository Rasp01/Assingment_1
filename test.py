with open('polygon.csv') as p:
    polygon_coordinates = p.readlines()

polygon_coordinates.pop(0)

print(polygon_coordinates)

x_coordinates = []

y_coordinates = []

for each_item in polygon_coordinates:
    id, x, y = each_item.split(',')
    x_coordinates.append(x.strip())
    y_coordinates.append(y.strip())


print(x_coordinates)
print(y_coordinates)
