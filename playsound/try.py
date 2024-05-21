import playsound 
import os
from multiprocessing import Process
import random 
import sys 

def musicPlayer(type_music):
    music_path = f"/home/rimmi/Desktop/music_player_py/playsound/music_import{type_music}"
    playsound.playsound(music_path)


if __name__ == "__main__":
    music_list = os.listdir("/home/rimmi/Desktop/music_player_py/playsound/music_import")
    song_play = random.choice(music_list)
    while True:
        variable_process = Process(target=musicPlayer, args = [song])
        variable_process.start()
        choice = input()
        if choice =="start":
            song_naam = input("Enter song name: ")
            for x in music_list:
                if song_naam in x:
                    print("Song found: ", x)
                    variable_process.terminate()
                    song = x
                    break


        elif choice == "end":
            variable_process.terminate()
            sys.exit()