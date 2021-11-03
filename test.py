with open('polygon.csv') as p:
    polygon_coordinates = p.readlines()

print(len(polygon_coordinates))

print(polygon_coordinates)

x_coordinates = []

y_coordinates = []

for each_item in polygon_coordinates:
    id, x, y = each_item.split(',')
    if x:
        x_coordinates.append(x.strip())
    elif y:
        y_coordinates.append(y.strip())

print(x_coordinates)
print(y_coordinates)
