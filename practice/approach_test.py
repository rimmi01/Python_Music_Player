import tkinter as tk
import os
from tkinter import filedialog
from playsound import playsound
from multiprocessing import process
import multiprocessing

playing_process = None



def add_path(importedMusic):
    file_path = filedialog.askopenfilename(filetypes=[("MP3 music files", "*.mp3")])
    if file_path:
        importedMusic.append(file_path)
        if len(importedMusic) == 1:
            play_music(importedMusic)

def play_music(importedMusic):
    global playing_process
    if not importedMusic:
        return
        
    path = importedMusic[0]

    #starting of a new process to play the music
    playing_process = multiprocessing.Process(target=playsound, args=(path,))
    playing_process.start()


    # playsound(path)


def stop_music():
    global playing_process
    if playing_process and playing_process.is_alive():

        playing_process.terminate()

# def update_path_label(path_label, path):
#     path_name = os.path.basename(path)
#     path_label.config(text=path_name)

if __name__=="__main__":
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




    # path_label = tk.Label(main_window, text="")
    # path_label.pack()
    # gui components
    # label_path_button = Label(main_window)




    main_window.mainloop()