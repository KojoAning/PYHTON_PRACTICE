from pygame import mixer
import time

water_file=open("water.txt","w")
eyes_file=open("eyes.txt","w")
physical_file=open("physical.txt","w")

for i in range(2):
    time.sleep(5)

    mixer.init()
    mixer.music.load(r"C:\Users\SRINATH\Desktop\c program\alaramtune.mp3")
    mixer.music.play()
    while True:
        user_input1 = input("Drink 0.5 litre water. Enter 'WDone' to stop the alarm:")
        if user_input1=="WDone":
            mixer.music.stop()
            water_file.write(f"Drank water {i + 1}th time at {time.asctime(time.localtime(time.time()))}\n")
            break
        else:
            continue

    print("\n")

    time.sleep(5)
    mixer.init()
    mixer.music.load(r"C:\Users\SRINATH\Desktop\c program\alaramtune.mp3")
    mixer.music.play()
    while True:
        user_input2 = input("Do eye exercise. Enter 'EDone' to stop the alarm:")
        if user_input2 == "EDone":
            mixer.music.stop()
            eyes_file.write(f"Did eye exercise {i + 1}th time at {time.asctime(time.localtime(time.time()))}\n")
            break
        else:
            continue


    print("\n")

    time.sleep(5)
    mixer.init()
    mixer.music.load(r"C:\Users\SRINATH\Desktop\c program\alaramtune.mp3")
    mixer.music.play()
    while True:
        user_input3 = input("Do physical exercise. Enter 'PDone' to stop the alarm:")
        if user_input3 == "PDone":
            mixer.music.stop()
            physical_file.write(
                f"Did physical exercise {i + 1}th time at {time.asctime(time.localtime(time.time()))}\n")
            break
        else:
            continue
        print("\n")


water_file.close()
eyes_file.close()
physical_file.close()



