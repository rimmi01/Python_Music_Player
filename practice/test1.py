import os
import tkinter as tk
from tkinter import filedialog
from playsound import playsound
import multiprocessing

def add_track(playlist):
    file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
    if file_path:
        playlist.append(file_path)
        if len(playlist) == 1:
            play_music(playlist)

def play_music(playlist):
    if not playlist:
        return

    track = playlist[0]
    playsound(track)

def pause_music():
    pass  # To be implemented: logic to pause playback

def stop_music():
    pass  # To be implemented: logic to stop playback

def update_track_label(track_label, track):
    track_name = os.path.basename(track)
    track_label.config(text=track_name)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Simple Music Player")
    
    playlist = []
    
    # GUI Elements

    root.minsize(width=600, height=600)
    track_label = tk.Label(root, text="No Track Selected", font=("Helvetica", 12))
    track_label.pack(pady=10)
    
    play_button = tk.Button(root, text="Play", command=lambda: play_music(playlist))
    play_button.pack(pady=5)
    
    pause_button = tk.Button(root, text="Pause", command=pause_music)
    pause_button.pack(pady=5)
    
    stop_button = tk.Button(root, text="Stop", command=stop_music)
    stop_button.pack(pady=5)
    
    add_button = tk.Button(root, text="Add Track", command=lambda: add_track(playlist))
    add_button.pack(pady=5)
    
    root.mainloop()
