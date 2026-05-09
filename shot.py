import circleshape


class Shot(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y, radius)
        