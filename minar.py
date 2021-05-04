from threading import Thread
import pyautogui as kbm
import time
import logging
import requests
import sys


def exit_minar():
    logging.info("Stopping Everything")
    print("Cleaning Up...")
    kbm.mouseDown()
    time.sleep(0.3)
    kbm.mouseUp()
    kbm.keyDown("shift")
    time.sleep(0.3)
    kbm.keyUp("shift")
    kbm.keyDown("d")
    time.sleep(0.3)
    kbm.keyUp("d")
    kbm.keyDown("a")
    time.sleep(0.3)
    kbm.keyUp("a")
    kbm.keyDown("w")
    time.sleep(0.3)
    kbm.keyUp("w")
    kbm.keyDown("s")
    time.sleep(0.3)
    kbm.keyUp("s")
    logging.warning("Exiting")
    print("Exiting...")
    time.sleep(2)
    sys.exit()


def movar():
    print("movar started")
    logging.info("movar started")
    kbm.keyDown("shift")
    x_interval = float(blocks / 2)
    y_interval = float(0.5)
    while True:
        kbm.keyDown("d")
        time.sleep(x_interval)
        kbm.keyUp("d")
        kbm.keyDown("s")
        time.sleep(y_interval)
        kbm.keyUp("s")
        kbm.keyDown("a")
        time.sleep(x_interval)
        kbm.keyUp("a")
        kbm.keyDown("w")
        time.sleep(y_interval)
        kbm.keyUp("w")


def minar():
    print("minar starter")
    logging.info("minar started")
    kbm.mouseDown()


open("minar_logs.log", "w+")
try:
    open("minar_logs.log", "w+").truncate()
except Exception:
    pass
logging.basicConfig(filename='minar_logs.log', filemode='r+', level="DEBUG", format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
url = "https://github.com/teekar2023/endstone-minar/releases/latest"
r = requests.get(url, allow_redirects=True)
redirected_url = r.url
if str(redirected_url) != "https://github.com/teekar2023/endstone-minar/releases/tag/v2.0":
    logging.warning("There Is A New Update Available")
    print("Press 'ENTER' To Exit...")
    input(f"There Is An Update Available! Please Download It At This Link: {str(redirected_url)}")
    exit()
else:
    pass
num = int(input("How Many Minutes Would You Like To Mine For:"))
blocks = int(input("How Many Blocks Wide Would You Like To Mine:"))
print("You Have 10 Seconds To Get Back Into Minecraft And Position Yourself...")
time.sleep(10)
logging.info(f"Starting With {num} Seconds Of Time And Parameter Of {blocks} Blocks On X-Axis")
try:
    logging.info("Starting Threads")
    move_thread = Thread(target=movar)
    move_thread.daemon = True
    move_thread.start()
    mine_thread = Thread(target=minar)
    mine_thread.daemon = True
    mine_thread.start()
    logging.info("Starting Timar")
    print("starting timar")
    for i in range(num):
        time.sleep(1)
        num -= 1
        print(f"Time Left: {str(num)} Seconds")
    logging.info("Timar Ended")
    print("timar ended")
    logging.info("Stopping Everything")
    print("Cleaning Up...")
    kbm.mouseDown()
    time.sleep(0.3)
    kbm.mouseUp()
    kbm.keyDown("shift")
    time.sleep(0.3)
    kbm.keyUp("shift")
    kbm.keyDown("d")
    time.sleep(0.3)
    kbm.keyUp("d")
    kbm.keyDown("a")
    time.sleep(0.3)
    kbm.keyUp("a")
    kbm.keyDown("w")
    time.sleep(0.3)
    kbm.keyUp("w")
    kbm.keyDown("s")
    time.sleep(0.3)
    kbm.keyUp("s")
    logging.warning("Exiting")
    print("Exiting...")
    time.sleep(2)
    sys.exit()
except KeyboardInterrupt:
    exit_minar()
except Exception as e:
    kbm.mouseUp()
    kbm.keyUp("shift")
    kbm.keyUp("d")
    kbm.keyUp("a")
    kbm.keyUp("w")
    kbm.keyUp("s")
    input(f"Error: {e}...Press Enter To Restart")
    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
