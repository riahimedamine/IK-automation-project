import keyboard
import time
from util import click_button, SHORT_DELAY, LONG_DELAY, back, log


def donate_alliance():
    if not click_button(
        "assets/alliance_tab.png",
        "Alliance Tab",
        confidence=0.45,
        delay=LONG_DELAY(),
    ):
        return

    if not click_button(
        "assets/technology_tab.png",
        "Technology Tab",
        confidence=0.4,
        delay=LONG_DELAY(),
    ):
        back()
        return

    if click_button(
        "assets/recom_donate.png",
        "Recommended Donation",
        confidence=0.8,
        delay=LONG_DELAY(),
    ):
        for _ in range(0, 10):
            if not click_button(
                "assets/donate_btn.png",
                "Donate Button",
                confidence=0.9,
                delay=SHORT_DELAY(),
            ):
                break
            time.sleep(SHORT_DELAY())
        back(3)
    else:
        back(2)

    log("Done 10 donations!")
    print("Done 10 donations!")


def main():
    print("Bot started. Press 'q' to stop.")
    log("Bot started")

    while not keyboard.is_pressed("q"):
        donate_alliance()
        print("Waiting 3 hours for the next donation cycle...")
        time.sleep(10)

    print("Bot stopped.")
    log("Bot stopped")


if __name__ == "__main__":
    main()
