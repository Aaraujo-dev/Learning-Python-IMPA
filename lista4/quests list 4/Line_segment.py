class Line_Segment:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def ponto_sobre(self, ponto):
        x1, y1 = self.point1
        x2, y2 = self.point2
        x, y = ponto
        
        if min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2):
            return True
        else:
            return False