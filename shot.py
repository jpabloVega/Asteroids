from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.radius = SHOT_RADIUS

    def draw():
        pass

    def update():
        pass