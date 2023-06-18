# import pyautogui
# import time
#
# # Delay before sending each letter (in seconds)
# delay = 0.2
#
#
# # Text to be typed
# # text = " "
# #
# # # Give some time to switch to the target application
# # time.sleep(3)
# #
# #
# # # Type each letter in the text
# # time.sleep(2)
# # pyautogui.press('right')
# class KeyControl:
#     def __init__(self, time_delay=.2):
#         self.delay = time_delay
#
#     def send_letter(self, letter):
#         pyautogui.typewrite(letter)
#         time.sleep(self.delay)

import pyautogui
import time


class MediaController:
    def __init__(self, state=0, delay=0.5):
        self.state = state
        self.delay = delay
        self.last_time_pressed = time.time()

    def controller_delay(self):
        return time.time() - self.last_time_pressed <= self.delay

    def media_control(self, control_type):
        if self.controller_delay():
            return
        if control_type < 2:
            if self.state ^ control_type:
                pyautogui.press('space')
                self.state = control_type
        elif control_type == 2:
            pyautogui.press('left')
        elif control_type == 3:
            pyautogui.press('right')
        elif control_type == 4:
            pyautogui.press('up')
        elif control_type == 5:
            pyautogui.press('down')

        # time.sleep(self.delay)
