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


open("minar_logs.log", "w+")
logging.basicConfig(filename='minar_logs.log', filemode='r+', level="DEBUG", format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
url = "https://github.com/teekar2023/endstone-minar/releases/latest"
r = requests.get(url, allow_redirects=True)
redirected_url = r.url
if redirected_url not "https://github.com/teekar2023/endstone-minar/releases/tag/v1.0":
    logging.warning("There Is New Update Available")
    input("There Is An Update Available Check Discord And Download It Nigga...")
    exit()
else:
    pass
print("You Have 5 Seconds To Get Back Into Minecraft...")
time.sleep(5)
try:
    logging.info("Starting Threads")
    move_thread = Thread(target=movar)
    move_thread.daemon = True
    move_thread.start()
    mine_thread = Thread(target=minar)
    mine_thread.daemon = True
    mine_thread.start()
    logging.info("Starting Timar")
    print("timar started")
    num = 810
    for i in range(810):
        time.sleep(1)
        num -= 1
        print(f"Time Left: {str(num)}")
    logging.info("Timar Ended")
    print("timar ended")
    logging.warning("Exiting")
    sys.exit()
    exit()
except Exception as e:
    input(f"Error: {e}")
