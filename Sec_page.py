# importing packages
from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import pygame
from pygame import mixer

# to initialize mixer
pygame.init()


# function to start the second  page
def start_sec_page():
    def show_setting():
        from Setting import Setting                                              # to import Setting.py program
        Setting.setting()                                                        # to call the setting() from Setting.py

    def start_game(args):
        second_window.destroy()                                                  # to destroy second window
        if args == 1:
            # to give background music
            #mixer.music.load('Audio/Main.mpeg')
            #mixer.music.play(-1)
            import obj
            obj.main()
        if args == 2:
            # to give background music
            mixer.music.load('Audio/Main.mpeg')
            mixer.music.play(-1)
            from Options import Jumbled_Words                                   # to import Jumbled word game page
            Jumbled_Words.start_third_page()                                    # to start the Jumbled word game

        if args == 3:
            from Options import nom
            nom.main()
        if args == 4:
            # to give background music
            mixer.music.load('Audio/Riddles.mpeg')
            mixer.music.play(-1)
            from Options import Riddles                                         # to import Riddles game page
            Riddles.start_fourth_page()                                         # to start the Riddles game

    def show_last_page():
        second_window.destroy()                                                 # to destroy the second window
        mixer.music.pause()                                                     # to pause the current music running
        import Main_page
        Main_page.start_main_page()                                             # to show the Main page

    def animate(counter):
        canvas.itemconfig(image, image=sequence[counter])
        canvas.after(150, lambda: animate((counter + 1) % len(sequence)))

    second_window = Tk()                                                         # creation of window
    second_window.title("Boot Brain \U0001F9E0")                                 # to show window title
    second_window.configure(background="black")                                  # window background colour
    second_window.wm_iconbitmap('Pictures/logo.ico')                             # to show window icon
    second_window.geometry("1540x825+0+0")                                             # window size(width,height)
    second_window.resizable(0, 0)                                                # to restrict user from resizing window

    canvas = Canvas(second_window, width=1540, height=825)
    canvas.pack()
    sequence = [ImageTk.PhotoImage(img)
                for img in ImageSequence.Iterator(Image.open(r'brain_waves.gif'))]
    image = canvas.create_image(770, 412, image=sequence[0])
    animate(1)

    # to set up Jumble words button image
    obj = Image.open("Pictures/obj.png")
    obj_photo = ImageTk.PhotoImage(obj)
    obj_btn = Button(image=obj_photo, bg='black', relief="solid", command=lambda: start_game(1))
    obj_btn.place(x=100, y=270)

    # to set up Jumble words button image
    jumble = Image.open("Pictures/Play_Jumble.png")
    jumble_photo = ImageTk.PhotoImage(jumble)
    jumble_btn = Button(image=jumble_photo, bg='black', relief="solid", command=lambda: start_game(2))
    jumble_btn.place(x=100, y=410)

    # to set up Jumble words button image
    nom = Image.open("Pictures/nom.png")
    nom_photo = ImageTk.PhotoImage(nom)
    nom_btn = Button(image=nom_photo, bg='black', relief="solid", command=lambda: start_game(3))
    nom_btn.place(x=100, y=540)

    # to set up Riddles button image
    riddles = Image.open("Pictures/Little_Riddle.png")
    riddles_photo = ImageTk.PhotoImage(riddles)
    riddles_btn = Button(image=riddles_photo, bg='black', relief="solid", command=lambda: start_game(4))
    riddles_btn.place(x=100, y=680)

    # to set up Back button image
    back_img = Image.open("Pictures/back.png")
    back_photo = ImageTk.PhotoImage(back_img)
    back_btn = Button(image=back_photo, bg='black', relief="solid", command=lambda: show_last_page())
    back_btn.place(x=5, y=5)

    # to set up setting button image
    setting_img = Image.open("Pictures/setting.jpg")
    setting_photo = ImageTk.PhotoImage(setting_img)
    setting = Button(image=setting_photo, bg='black', relief="solid", command=lambda: show_setting())
    setting.place(x=1450, y=5)

    # to give background music
    #mixer.music.load('Audio/Main.mpeg')
    #mixer.music.play(-1)

    second_window.mainloop()                                                          # to run the event loop
