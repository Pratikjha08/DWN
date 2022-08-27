import time
from plyer import notification

if __name__== "__main__":
    # while True:
        notification.notify(
            title = "Please drink water now!",
            message = "You should drink atleast 3.7 ltr water",
            app_icon = "C:/Users/prati/OneDrive/Desktop/DWN/icon.ico",
            timeout = 12
        )
        # time.sleep(60*60)
# PS: Use "pythonw .\main.py" to run it in the background
