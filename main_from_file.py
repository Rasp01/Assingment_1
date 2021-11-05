if __name__ == '__main__':

###Instructions

#read a list of coordinates from a CSV file and create a polygon

#Read a list of coordinate from a file and create a list of testing points

#Catergorise these points into inside,outside and boundary

#Output the result of each point in a csv file

# plot the points and polygon in a plot window

#### Re-written as logical sequence

#1

#import  a list of corrdinate from polygon.csv file

# convert into a list

# run the list through the polygon in the geometry class



#2

# import  a list of coordinates from the input.csv file

#

with open('polygon.csv') as p:
    polygon = p.readlines()

print(polygon)

#cannot use numpy

import numpy as np
import matplotlib.pylab as plt

class Geometry:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

class Point(Geometry):

    def __init__(self,name,x,y):
        super().__init__(name)
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

class Line(Geometry):

    def __init__(self, name, point_1, point_2):
        super().__init__(name)
        self.__point_1 = point_1
        self.__point_2 = point_2

class Polygon(Geometry):

    def __init__(self,name,points):
        super().__init__(name)
        self._points = points

    def get_points(self):
        return self._points

    def lines(self):
        res = []
        points = self.get_points()
        point_a = points[0]
        for point_b in points[1:]:
            res.append(Line(point_a.get_name() + '-' + point_b.get_name(), point_a, point_b))
            point_a=point_b
        res.append(Line(point_a.get_name() + '-' + points[0].get_name(), point_a, points[0]))

class Plotter:

    def __init__(self):
        plt.figure()

    def add_polygon(self, xs, ys):
        plt.fill(xs, ys, 'lightgray', label='Polygon')

    def add_point(self, x, y, kind=None):
        if kind == 'outside':
            plt.plot(x, y, 'ro', label='Outside')
        elif kind == 'boundary':
            plt.plot(x, y, 'bo', label='Boundary')
        elif kind == 'inside':
            plt.plot(x, y, 'go', label='Inside')
        else:
            plt.plot(x, y, 'ko', label='Unclassified')

    def show(self):
        handles, labels = plt.gca().get_legend_handles_labels()
        by_label = OrderedDict(zip(labels, handles))
        plt.legend(by_label.values(), by_label.keys())
        plt.show()


polygon_data=np.genfromtxt('polygon.csv',delimiter=',',usecols=(1,2))
polygon_x=data[:,0]
polygon_y=data[:,1]

testing_points=np.genfromtxt('input.csv',delimiter=',',usecols=(1,2))
testing_points_x=data[:,0]
testing_points_y=data[:,1]

plotter= Plotter()
plotter.add_polygon(x,y)
plotter
plt.show()

#polygon = Polygon('polygon',)

#plt.plot()