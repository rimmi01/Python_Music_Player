from tkinter import * 

main_window = Tk()
main_window.title("Music Player")
main_window.minsize(width=600, height=600)

# Create a Label with text
label_text = Label(main_window, text="GUI Based Python Music Player")
label_text.pack()

# Load the image
image_path = "playsound/imagesUsed/MusicPlayer.png"
image = PhotoImage(file=image_path)

# Create a Label with the loaded image
label_image = Label(main_window, image=image)
label_image.pack()

main_window.mainloop()
