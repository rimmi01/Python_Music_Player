from tkinter import * 

main_window = Tk()
main_window.title("Music Player")
main_window.minsize(width=600, height=600)
main_window.maxsize(width=800, height=800)

text_label = Label(main_window, text="GUI Based Python Music Player")
text_label.pack()


# Variable for ()
v = StringVar()
def edtech():
    X= v.get()
    print(X)
    label_start.config(text=X, bg="yellow", fg="blue")
    label_stop.config(text=X, bg="yellow", fg="blue")


# image_path = PhotoImage(file="playsound/imagesUsed/MusicPlayer.png")
# text_label = Label(main_window, image=image_path)
text_label.pack()


# stop button
stop_button = Button(main_window, text="Stop", bg="grey", fg="black")
stop_button.pack()


# search bar using Entry
search_bar = Entry(main_window, width=20, font=("Calibri", 20), bd=5, textvariable=v)
# search_bar.place(x=80, y=10)
search_bar.pack()
# search_bar.insert('1.0', 'search the song here')
search_bar.pack()


# start button
start_button = Button(main_window, text="Start", bg="grey", fg="black", command=edtech)
start_button.pack()


# Label for showing that the start button has started the execution, or, started the music 
label_start = Label(main_window, text="Music Starts", fg="yellow", bg="green")
label_start.pack()


# Label for showing that the stop button has stopped the execution, or, stopped the music 
label_stop = Label(main_window, text="Music Stops", fg="yellow", bg="green")
label_stop.pack()
main_window.mainloop()





### created buttons stop and start, and search bar, now, only thing left is implementing logics, from the cli code, through using functions as, suggested using, command in the label, of the defined variable, and, in serch bar giving the text variable, as, the function's variable name, as, defined in the function, and, using this after creating function, write, the varible_name.config(code...), and, it, will work!!!!! Enjoy!!!!!
