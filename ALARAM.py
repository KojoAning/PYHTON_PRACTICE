import os,datetime,time
a,b,c = input("Enter the date : ").split("/")
hr,min,sec = input("Enter the time : ").split(":")
m = datetime.date(int(c),int(b),int(a))
n=1
while n>0:
    if time.localtime().tm_hour == int(hr) and time.localtime().tm_min == int(min) and time.localtime().tm_sec == int(sec) and datetime.date.today() == m :
        print("Playing the ringtone")
        os.startfile(r"PATH.mp3")
        break
    else:
        n=n+1
