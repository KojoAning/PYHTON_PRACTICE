# this application will reminds you tu drink water,do some eye exersise and some physical activity, in certain time interval
import time
from plyer import notification



if __name__ == '__main__':
    while True:

        notification.notify(
            title = "Drink 437ml of water now!!",
            message = "Since an avarage person needs 3.7 liter of water in a day."
                      "This program will make you drink 3.7 liters of water in between your office hours.",
            app_icon = r"C:\Users\SRINATH\Desktop\c program\glass_icon.ico",
            timeout = 7

    )
        time.sleep(60*60)


