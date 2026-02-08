from screen_manager import ScreenManager
from gpio_listener import GPIOListener

def main():
    screen_manager = ScreenManager(start_screen="boot")
    gpio = GPIOListener()

    while True:
        event = gpio.get_event()
        if event:
            screen_manager.handle_event(event)

        screen_manager.update()
        screen_manager.draw()

if __name__ == "__main__":
    main()