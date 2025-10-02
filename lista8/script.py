import random
from Polygons import Point2D, Polygon, Polygons, plot_polygons

#Função para gerar um polígono aleatório
def generate_random_polygon(num_points: int, color: str) -> Polygon:
    points = [Point2D(random.uniform(-200, 200), random.uniform(-200, 200)) for _ in range(num_points)]
    return Polygon(points, color)

def main():
    polygons = Polygons()

    polygons.add_polygon(generate_random_polygon(3, 'red'), 'triangle')
    polygons.add_polygon(generate_random_polygon(4, 'blue'), 'rectangle')
    polygons.add_polygon(generate_random_polygon(5, 'green'), 'pentagon')

    polygons.save_to_file('polygons.txt')

    loaded_polygons = Polygons()
    loaded_polygons.load_from_file('polygons.txt')

    plot_polygons(loaded_polygons)

if __name__ == '__main__':
    main()
