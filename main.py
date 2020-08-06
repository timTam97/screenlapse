import time

import pyautogui

import actions
import constants


def main():
    actions.set_session_key()
    while True:
        # grab screenshot
        # push to aws
        # wait 5 secs
        pyautogui.screenshot(constants.IMG_NAME)
        actions.push_img()
        time.sleep(5)


if __name__ == "__main__":
    main()
