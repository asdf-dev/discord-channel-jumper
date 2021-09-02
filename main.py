import os
import sys
import time
from pynput.keyboard import Key, Controller


keyboard = Controller()

#shellExecute('wmctrl -a discord')


def shellExecute(command):
    os.system(command)

def discordQuickSwitcher():
    keyboard.press(Key.ctrl)
    keyboard.press("k")
    keyboard.release(Key.ctrl)
    keyboard.release("k")


def pressLetters(letters):
    arr = list(letters)
    for i in arr:
        keyboard.press(i)
    time.sleep(0.1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


def doChannelJump(channelName):
    #jumps to discord window
    shellExecute('wmctrl -a discord')
    time.sleep(0.5)
    

    #open quick switcher
    discordQuickSwitcher()


    pressLetters(channelName)








if __name__ == "__main__":
    if len(sys.argv) > 1:
        doChannelJump(sys.argv[1])        
    else:
        print("Argument missing")