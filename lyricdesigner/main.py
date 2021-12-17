import importlib.resources as pkg_resources

import arcade

from lyricdesigner import __version__
from lyricdesigner.data import charts
from lyricdesigner.views.start import StartView


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = f"LyricDesigner {__version__}"

arcade.enable_timings()


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.start_view = StartView()
        self.current_song = pkg_resources.read_text(charts, "notes.chart")

    def setup(self):
        self.start_view.setup()
        self.show_view(self.start_view)


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
