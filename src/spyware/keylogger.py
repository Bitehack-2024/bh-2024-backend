from spyware.my_queue import q


def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if pressed:
        q.put((x, y))
        print("wkładam do kolejki")
    #     # Stop listener
    #     return False

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))


# def periodic_print():
    # while True:
    #     element = q.get()
    #     print("Processed", element, "click")
        # print('Press Ctrl+C to exit')
        # time.sleep(1)
