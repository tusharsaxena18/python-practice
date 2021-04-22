import time
from plyer import notification
user_time=input("Time batao(in seconds): ")
while True:
    notification.notify(
        title = "Paani pe le yaar",
        message = "Kab tak paani dega mai",
        app_icon = "D:\Documents\Coding\ico files\icon.ico",
        timeout = 2
        )
    time.sleep(int(user_time))