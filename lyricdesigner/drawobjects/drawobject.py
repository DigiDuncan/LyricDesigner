import arcade


class DrawObject:
    def __init__(self, pos: tuple[float, float], width: float, height: float, bgcolor: tuple[int, int, int] = None):
        self.pos = pos
        self.width = width
        self.height = height
        self.bgcolor = bgcolor

    @property
    def x(self) -> float:
        return self.pos[0]

    @x.setter
    def x(self, val: float):
        self.pos = (val, self.pos[1])

    @property
    def y(self) -> float:
        return self.pos[1]

    @y.setter
    def y(self, val: float):
        self.pos = (self.pos[0], val)

    @property
    def max_x(self) -> float:
        return self.x + self.width

    @property
    def max_y(self) -> float:
        return self.y - self.height

    @property
    def center(self) -> tuple[float, float]:
        return (self.x + (self.width / 2), self.y - (self.height / 2))

    @center.setter
    def center(self, new_pos: tuple[float, float]):
        self.x = new_pos[0] - self.width / 2
        self.y = new_pos[1] + self.height / 2

    @property
    def center_x(self) -> float:
        return self.center[0]

    @center_x.setter
    def center_x(self, val: float):
        self.center = (val, self.center[1])

    @property
    def center_y(self) -> float:
        return self.center[1]

    @center_y.setter
    def center_y(self, val: float):
        self.center = (self.center[0], val)

    def draw(self):
        if self.bgcolor:
            arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.bgcolor)
