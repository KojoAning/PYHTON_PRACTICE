import random
import webbrowser
import time
while True:
    random.choice(["youtube.com ","facebook.com" , "amazonprime.com"])
    visit = "http://{}".format(sites)
    webbrowser.open(visit)
    seconds = random.randrange(1, 5)
    time.sleep(seconds)
