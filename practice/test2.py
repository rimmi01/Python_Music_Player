
import tkinter as tk
import os
from tkinter import filedialog
from playsound import playsound
import multiprocessing

# Global variable to store the process
music_process = None

def add_path(importedMusic):
    file_path = filedialog.askopenfilename(filetypes=[("MP3 music files", "*.mp3")])
    if file_path:
        importedMusic.append(file_path)
        if len(importedMusic) == 1:
            play_music(importedMusic)

def play_music(importedMusic):
    global music_process
    if not importedMusic:
        return
    
    path = importedMusic[0]
    # Start a new process to play the music
    music_process = multiprocessing.Process(target=playsound, args=(path,))
    music_process.start()

def stop_music():
    global music_process
    if music_process and music_process.is_alive():
        # Terminate the process if it's running
        music_process.terminate()

if __name__ == "__main__":
    importedMusic = []

    main_window = tk.Tk()
    main_window.title("Music Player")
    main_window.minsize(width=600, height=600)
    main_window.maxsize(width=800, height=800)

    text_label = tk.Label(main_window, text="GUI Based Python Music Player")
    text_label.pack()

    stop_button = tk.Button(main_window, text="STOP", bg="grey", fg="black", command=stop_music)
    stop_button.pack()

    start_button = tk.Button(main_window, text="START", bg="grey", fg="black", command=lambda: play_music(importedMusic))
    start_button.pack()

    path_button = tk.Button(main_window, text="ADD PATH", bg="grey", fg="black", command=lambda: add_path(importedMusic))
    path_button.pack()

    main_window.mainloop()

