import arcade

from lyricdesigner.drawobjects.progressbar import ProgressBar


class StartView(arcade.View):
    def __init__(self):
        super().__init__()
        self.current_text = "Loading..."
        self.done = False
        self.current_time = 0
        self.progress_bar = ProgressBar((0, 0), 400, 50, (64, 64, 64))
        self.progress_bar.center_x = self.window.width / 2
        self.progress_bar.center_y = 200
        self.frame = 0
        self.last_dump = 0

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_update(self, delta_time: float):
        self.current_time += delta_time
        self.current_time = round(self.current_time, 2)
        self.progress_bar.progress += (delta_time / 60)
        self.frame += 1
        self.last_dump += delta_time
        if self.last_dump > 1:
            print(arcade.get_fps())
            self.last_dump = 0

    def on_draw(self):
        arcade.start_render()
        y = self.window.height - 260
        txt1 = arcade.Text("Test Program", self.window.width / 2, y, arcade.color.YELLOW, 96, anchor_x="center", bold=True)
        txt2 = arcade.Text(f"{self.current_time:.2f}", self.window.width / 2, y, arcade.color.YELLOW, 60, anchor_x="center", anchor_y="top")
        # txt2.y -= txt2._label.content_height
        arcade.draw_line(0, y, self.window.width, y, arcade.color.BLUE)
        arcade.draw_lrtb_rectangle_outline(txt2.x - txt2._label.content_width / 2, txt2.x + txt2._label.content_width / 2, txt2.y, txt2.y - txt2._label.content_height, arcade.color.RED)
        txt1.draw()
        txt2.draw()
        arcade.draw_text(self.current_text, self.window.width / 2, 250, arcade.color.WHITE, 32, anchor_x="center")
        self.progress_bar.draw()

    def setup(self):
        pass
