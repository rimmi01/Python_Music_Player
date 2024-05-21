from tkinter import *
from PIL import Image, ImageTk
import os
import playsound

class MusicPlayer:
    def __init__(self, Tk):
        self.root = Tk
        self.root.title("Music Player")

        # Stop button with Remixicon image
        self.stop_image = ImageTk.PhotoImage(file="stop_icon.ico")  # Replace with actual Remixicon image path
        self.stop_button = Button(self.root, image=self.stop_image, bd=0, bg='white', command=self.stop_music)
        self.stop_button.place(x=5, y=300)  # Adjust position as needed

        # ... other code elements (music directory, search functionality, etc.)

    def stop_music(self):
        playsound.stop_all()  # Halt currently playing music

        # (Optional) Update UI to reflect stopped state (e.g., disable stop button)

    # ... other methods (play_music, populate_song_list, etc.)

root = Tk()
object = MusicPlayer(root)
root.mainloop()
