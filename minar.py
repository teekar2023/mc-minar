from threading import Thread
import pyautogui as kbm
import time
import sys


def movar():
    print("movar started")
    while True:
        for i in range(12):
            time.sleep(0.5)
            kbm.keyDown("d")
            time.sleep(0.03)
            kbm.keyUp("d")
        time.sleep(0.5)
        kbm.keyDown("s")
        time.sleep(0.05)
        kbm.keyUp("s")
        for i in range(12):
            time.sleep(0.5)
            kbm.keyDown("a")
            time.sleep(0.03)
            kbm.keyUp("a")
        time.sleep(0.5)
        kbm.keyDown("w")
        time.sleep(0.02)
        kbm.keyUp("w")


def minar():
    print("minar starter")
    kbm.mouseDown()


print("You Have 5 Seconds To Get Back Into Minecraft...")
time.sleep(5)
try:
    move_thread = Thread(target=movar)
    move_thread.daemon = True
    move_thread.start()
    mine_thread = Thread(target=minar)
    mine_thread.daemon = True
    mine_thread.start()
    print("timar started")
    num = 810
    for i in range(810):
        time.sleep(1)
        num -= 1
        print(f"Time Left: {str(num)}")
    print("timar ended")
    sys.exit()
    exit()
except Exception as e:
    input(f"Error: {e}")
