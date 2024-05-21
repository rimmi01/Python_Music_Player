from tkinter import * 
from PIL import Image, ImageTk 
import os 
import playsound 

# ek_simple_variable = Tk()
# ek_simple_variable.mainloop()


#lets do it using function, 

class MusicPlayer:
    def __init__(self, Tk):
        self.root = Tk
        self.root.title("Music Player")
        # self.stop_button= Button(self.root, text='stop', command=self.stop_music)
        # self.stop_button.pack()
        self.photo_stop_button = ImageTk.PhotoImage(file='playsound/imagesUsed/stop-fill.png')
        photo_stop_button = Button(self.root, image=self.photo_stop_button, bd=0, bg='white').place(x=5, y=300)


        #os import ka code, ## variables defined 
        music_directory = '/home/rimmi/Music'
        vscode_music_directory = 'playsound/music_import'

        # def stop_music(self):
        #     playsound.stop_all()


        # def play_music(self, playsound/music_import):
        #     playsound.playsound('playsound/music_import')

        # self.play_music(music_directory)
        self.root.geometry("600x600")

        # chalo baad mein dekte hain es error ko, as, the image is not adjusting according to px's , and don't know how to adjust the image size which is visible in the gui, 
        # self.photo_variable=ImageTk.PhotoImage(file='playsound/imagesUsed/MusicPlayer.png')
        # photo_variable=Label(self.root,image=self.photo_variable).place(x=0, y=0)





        # using os listdir()
        for music_import in os.listdir(music_directory):
            src = os.path.join(music_directory, music_import)
            dst = os.path.join(vscode_music_directory, music_import)
            with open(src, 'rb') as source_file:
                with open(dst, 'wb') as dest_file:
                    dest_file.write(source_file.read())



        # Using os.walk() for traversing subdirectories
        for root, dirs, files in os.walk(music_directory):
            for music_import in files:
                if music_import.endswith('.mp3'):
                    src = os.path.join(root, music_import)
                    dst = os.path.join(vscode_music_directory, music_import)
                    with open(src, 'rb') as source_file:
                        with open(dst, 'wb') as dest_file:
                            dest_file.write(source_file.read())


root = Tk()
object = MusicPlayer(root)  # yha jo music player likha hai, voh uper bnai hui class ka naam hai
root.mainloop()
