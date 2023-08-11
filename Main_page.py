# importing packages
from tkinter import *
from PIL import Image, ImageTk, ImageSequence
from tkinter import messagebox
import pygame
from pygame import mixer

# to initialize mixer
pygame.init()


# function to start the main page
def start_main_page():
    def show_setting():
        from Setting import Setting                                              # to import Setting.py program
        Setting.setting()                                                        # to call the setting() from Setting.py

    def start_game():
        main_window.destroy()                                                    # to destroy main window
        import Sec_page
        Sec_page.start_sec_page()                                                # to start second page

    def show_end():
        messagebox.askyesno("Exit", "Do you really want to exit????")            # to show message box when exit
        main_window.destroy()
        exit()

    def animate(counter):
        canvas.itemconfig(image, image=sequence[counter])
        canvas.after(150, lambda: animate((counter + 1) % len(sequence)))

    main_window = Tk()                                                           # creation of window
    main_window.title("Boot Brain \U0001F9E0")                                   # to show window title
    main_window.configure(background="black")                                    # window background colour
    main_window.wm_iconbitmap('Pictures/logo.ico')                               # to show window icon
    main_window.geometry("1540x825+0+0")                                                 # to position window
    main_window.resizable(0, 0)                                                  # to restrict user from resizing window

    canvas = Canvas(main_window, width=1540, height=825)
    canvas.pack()
    sequence = [ImageTk.PhotoImage(img)
                for img in ImageSequence.Iterator(Image.open(r'video-to-gif-converter.gif'))]
    image = canvas.create_image(770, 412, image=sequence[0])
    animate(1)

    # to set up start button image
    start_img = Image.open("Pictures/Start.png")
    start_photo = ImageTk.PhotoImage(start_img)
    start = Button(main_window, image=start_photo, bg='black', relief="solid", command=lambda: start_game())
    start.place(x=1200, y=570)

    # to set up exit button image
    exit_img = Image.open("Pictures/Exit.png")
    exit_photo = ImageTk.PhotoImage(exit_img)
    exit_btn = Button(main_window, image=exit_photo, bg='black', relief="solid", command=lambda: show_end())
    exit_btn.place(x=1200, y=690)

    # to set up setting button image
    setting_img = Image.open("Pictures/setting.jpg")
    setting_photo = ImageTk.PhotoImage(setting_img)
    setting = Button(main_window, image=setting_photo, bg='black', relief="solid", command=lambda: show_setting())
    setting.place(x=5, y=5)

    # to give background music
    #mixer.music.load('Audio/Main.mpeg')
    #mixer.music.play(-1)

    main_window.mainloop()                                                           # to run the event loop


start_main_page()
