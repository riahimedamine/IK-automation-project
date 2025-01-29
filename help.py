import keyboard
import time
from util import click_button, SHORT_DELAY, LONG_DELAY, log


def main():
    print("Bot started. Press 'q' to stop.")
    log("Bot started")

    while not keyboard.is_pressed("q"):
        click_button(
            "assets/help_btn.png",
            "Help Button",
            confidence=0.65,
            delay=SHORT_DELAY(),
            gray=False,
        )
        time.sleep(LONG_DELAY())

    print("Bot stopped.")
    log("Bot stopped")


if __name__ == "__main__":
    main()
