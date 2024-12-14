import queue
from pathlib import Path
from threading import Thread
from time import sleep

from PIL import ImageGrab

from spyware.my_queue import q


class ScreenshotThread(Thread):
    def __init__(self):
        super().__init__()
        self._buffer = []
        self.action_counter = 0

    def button_clicked(self):
        self.action_counter += 1
        screenshot = self._buffer[-1]
        # breakpoint()
        # draw = ImageDraw.Draw(screenshot)


        self._buffer[-1].save(Path(__file__).parent.parent / "data" / f"screenshot-{self.action_counter}.png")
        # self._buffer[-1].show()
    #
    def run(self):
        while True:
            self._buffer.append(ImageGrab.grab())

            try:
                result = q.get(block=False)
                self.button_clicked()
                continue
            except queue.Empty:
                pass
            sleep(0.5)
