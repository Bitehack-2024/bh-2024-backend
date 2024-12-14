import queue
from pathlib import Path
from threading import Thread
from time import sleep

from PIL import ImageGrab, ImageDraw

from spyware.my_queue import q


class ScreenshotThread(Thread):
    def __init__(self):
        super().__init__()
        self._buffer = []
        self.action_counter = 0

    @staticmethod
    def draw_circle(image, position):
        draw = ImageDraw.Draw(image)
        draw.ellipse((position[0] - 20, position[1] - 20, position[0] + 20, position[1] + 20), outline="red", width=3)

    def button_clicked(self, position):
        self.action_counter += 1
        screenshot = self._buffer[-1]
        self.draw_circle(screenshot, position)
        screenshot.save(Path(__file__).parent.parent / "data" / f"screenshot-{self.action_counter}.png")

    def run(self):
        while True:
            self._buffer.append(ImageGrab.grab((0, 0, 1920, 1080)))

            try:
                position = q.get(block=False)
                self.button_clicked(position)
                continue
            except queue.Empty:
                pass
            sleep(0.3)
