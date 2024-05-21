import playsound , os 
from multiprocessing import Process
import random,sys


def play_music(music_name):
    music_path = f"/home/rimmi/Desktop/music_player_py/playsound/music_import/{music_name}"
    playsound.playsound(music_path)



if __name__ =="__main__":
    musics = os.listdir("/home/rimmi/Desktop/music_player_py/playsound/music_import")
    song = random.choice(musics)
    while True :
        p1 = Process(target=play_music, args=[song])
        p1.start()
        choice = input()
        if choice =="s":
            song_name = input("Enter song name = ")
            for x in musics:
                if song_name in x:
                    print("song found = ", x)
                    p1.terminate()
                    song = x
                    break
             

        elif choice =="e":
            p1.terminate()
            sys.exit()