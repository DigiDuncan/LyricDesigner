import arcade

from lyricdesigner.drawobjects.drawobject import DrawObject


class ProgressBar(DrawObject):
    def __init__(self, pos: tuple[int, int], width: int, height: int, bgcolor: tuple[int, int, int] = None,
                 fgcolor: tuple[int, int, int] = (255, 255, 255), *, progress = 0):
        super().__init__(pos, width, height, bgcolor=bgcolor)
        self.fgcolor = fgcolor
        self._progress = progress

    @property
    def progress(self):
        return self._progress

    @progress.setter
    def progress(self, value):
        self._progress = arcade.clamp(value, 0, 1)

    def draw(self):
        super().draw()
        arcade.draw_lrtb_rectangle_filled(self.x, self.x + (self.width * self.progress), self.y, self.max_y, self.fgcolor)
