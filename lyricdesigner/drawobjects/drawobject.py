class DrawObject:
    def __init__(self, pos: tuple[int, int], width: int, height: int, bgcolor: tuple[int, int, int] = None):
        self.pos = pos
        self.width = width
        self.height = height
        self.bgcolor = bgcolor

    @property
    def x(self):
        return self.pos[0]

    @x.setter
    def x(self, val: int):
        self.pos = (val, self.pos[1])

    @property
    def y(self):
        return self.pos[1]

    @x.setter
    def x(self, val: int):
        self.pos = (self.pos[0], val)

    @property
    def max_x(self):
        return self.x + self.width

    @property
    def max_y(self):
        return self.y - self.height

    @property
    def center(self):
        return (self.x + (self.width // 2), self.y - (self.height // 2))

    @property
    def center_x(self):
        return self.center[0]

    @property
    def center_y(self):
        return self.center[1]
