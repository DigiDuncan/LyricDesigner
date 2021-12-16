import arcade

from lyricdesigner.drawobjects.progressbar import ProgressBar


class StartView(arcade.View):
    def __init__(self):
        super().__init__()
        self.current_text = "Loading..."
        self.done = False
        self.current_time = 0
        self.progress_bar = ProgressBar((0, 0), 400, 50, (64, 64, 64))
        self.progress_bar.center_x = self.window.get_size()[0] / 2
        self.progress_bar.center_y = 200

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_update(self, delta_time: float):
        self.current_time += delta_time
        self.current_time = round(self.current_time, 2)
        self.progress_bar.progress += (delta_time / 60)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("LyricDesigner", self.window.width / 2, self.window.height - 260, arcade.color.YELLOW, 96, anchor_x="center", bold=True)
        arcade.draw_text(f"{self.current_time:.2f}", self.window.width / 2, self.window.height - 400, arcade.color.YELLOW, 60, anchor_x="center")
        self.progress_bar.draw()

    def setup(self):
        pass
