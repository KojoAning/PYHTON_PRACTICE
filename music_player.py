from pygame import mixer
from tkinter import Tk , Label ,Button , filedialog


current_volume = float(0.5)

#functions
def play_song() :
    FileName = filedialog.askopenfilename(initialdir = "C:\SONGS\\bollywood songs" , title = "Select a file")
    current_song_name = FileName
    song_title = FileName.split('/')
    song_title = song_title[-1]
    print(song_title)

    try:
        mixer.init()
        mixer.music.load(current_song_name)
        mixer.music.set_volume(current_volume)
        mixer.music.play()
        song_title_level.config(fg = 'black', text = 'Now Playing :'+ str(song_title_level))
        volume_level.config(fg = 'black', text = 'Volume :' + str(current_volume))
    except Exception as e :
        print(e)
        song_title_level.config(fg='red',text = 'ERROR IN PLAYING TRACK')



# main screen
master = Tk()
master.title("Musci Plyer")
#Lable
Label(master,text = "custom music player..." , font = ("Freestyle Script",30),fg = "Black").grid(sticky ="N",row =0,padx = 120)
Label(master,text = "# Select the song you wanna pay :" , font = ("Freestyle Script",25),fg = "Black").grid(sticky ="N",row = 1)
Label(master,text = "# Volume :" , font = ("Freestyle Script",25),fg = "blue").grid(sticky ="N",row = 4)
song_title_level = Label(master,font = ("Freestyle Script",20))
song_title_level.grid(sticky ="N",row = 3)
volume_level = Label(master,font = ("Freestyle Script",20))
volume_level.grid(sticky ="N",row = 5)

#buttons
Button(master , text = "Select Song" , font=("bold",10) , command = play_song).grid(row = 2 , sticky = "N")
Button(master , text = "Pause" , font=("Freestyle Script bold",10)).grid(row = 3 , sticky = "E", padx = 120)
Button(master , text = "Resume" , font=("Freestyle Script bold",10)).grid(row = 3 , sticky = "W", padx = 120)
Button(master , text = "-" , font=("Freestyle Script bold",10),width =5).grid(row = 5 , sticky = "W", padx = 120)
Button(master , text = "+" , font=("Freestyle Script bold",10),width = 5).grid(row = 5 , sticky = "E", padx = 120)



master.mainloop()