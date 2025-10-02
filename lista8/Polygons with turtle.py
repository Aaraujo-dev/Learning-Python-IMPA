import re
import turtle
from typing import List, Tuple

class Point2D:
    def __init__(self, x: float, y: float):
        self.coord = (x, y)

class Polygon:
    def __init__(self, points: List[Point2D], color: str):
        self.points = points
        self.color = color

class Polygons:
    def __init__(self):
        self.polygons = {}
    
    def add_polygon(self, polygon: Polygon, name: str):
        self.polygons[name] = polygon

    def remove_polygon(self, name: str):
        if name in self.polygons:
            del self.polygons[name]

    def save_to_file(self, filename: str):
        with open(filename, 'w') as f:
            for name, polygon in self.polygons.items():
                points_str = '; '.join(f"({p.coord[0]}, {p.coord[1]})" for p in polygon.points)
                f.write(f"{points_str}; {polygon.color}; {name}\n")
                
    def load_from_file(self, filename: str):
        with open(filename, 'r') as f:
            for line in f:
                parts = line.strip().split('; ')
                points = [tuple(map(float, re.findall(r"-?\d+\.\d+|-?\d+", point))) for point in parts[:-2]]
                points = [Point2D(x, y) for x, y in points]
                color = parts[-2]
                name = parts[-1]
                self.add_polygon(Polygon(points, color), name)

def plot_polygons(polygons: Polygons):
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    
    for name, polygon in polygons.polygons.items():
        t.penup()
        t.goto(polygon.points[0].coord)
        t.pendown()
        t.color(polygon.color)
        t.begin_fill()
        for point in polygon.points:
            t.goto(point.coord)
        t.goto(polygon.points[0].coord)
        t.end_fill()
    
    screen.mainloop()
