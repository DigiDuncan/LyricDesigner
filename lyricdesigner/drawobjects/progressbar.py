import arcade

from lyricdesigner.drawobjects.drawobject import DrawObject

class ProgressBar(DrawObject):
    def __init__(self, pos: tuple[int, int], width: int, height: int, bgcolor: tuple[int, int, int] = None,
                 fgcolor: tuple[int, int, int] = (255, 255, 255), *, progress = 0):
        super().__init__(pos, width, height, bgcolor=bgcolor)
        self.fgcolor = fgcolor
        self.progress = progress

    def draw(self):
        if self.bgcolor:
            arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.bgcolor)
        arcade.draw_lrtb_rectangle_filled(self.x, self.x + (self.width * self.progress), self.y, self.max_y, self.fgcolor)
