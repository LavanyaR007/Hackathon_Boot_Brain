# importing packages
from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import pygame
from pygame import mixer


# to initialize mixer
pygame.init()


# function to start the Jumbled word game page
def start_fourth_page():
    def show_setting():
        from Setting import What_am_I_Setting                             # to import Setting.py program
        What_am_I_Setting.setting()                                       # to call the setting() from Setting.py

    def show_last_page():
        riddle_window.destroy()
        import Sec_page
        Sec_page.start_sec_page()

    def start_riddle_game(args):
        riddle_window.destroy()
        if args == 1:
            # to give background music
            mixer.music.load('Audio/Riddles.mpeg')
            mixer.music.play(-1)
            from Options import What_Am_I
            What_Am_I.main()
        elif args == 2:
            # to give background music
            mixer.music.load('Audio/Guess_the_Emoji.mpeg')
            mixer.music.play(-1)
            from Options import Emoji_world
            Emoji_world.main()

    def animate(counter):
        canvas.itemconfig(image, image=sequence[counter])
        canvas.after(150, lambda: animate((counter + 1) % len(sequence)))

    riddle_window = Tk()                                                         # creation of window
    riddle_window.title("Boot Brain \U0001F9E0----->Riddles")                    # to show window title
    riddle_window.configure(background="black")                                  # window background colour
    riddle_window.wm_iconbitmap('Pictures/logo.ico')                             # to show window icon
    riddle_window.geometry("1540x825+0+0")                                             # window size(width,height)
    riddle_window.resizable(0, 0)                                                # to restrict user from resizing window

    canvas = Canvas(riddle_window, width=1540, height=825)
    canvas.pack()
    sequence = [ImageTk.PhotoImage(img)
                for img in ImageSequence.Iterator(Image.open(r'Riddle_video.gif'))]
    image = canvas.create_image(770, 412, image=sequence[0])
    animate(1)

    # to set up background image
    riddle_img = Image.open("Pictures/Riddle_back.jpg")
    riddle_photo = ImageTk.PhotoImage(riddle_img)
    back_image = Label(image=riddle_photo)
    back_image.pack()

    # to set up setting button image
    setting_img = Image.open("Pictures/setting.jpg")
    setting_photo = ImageTk.PhotoImage(setting_img)
    setting = Button(image=setting_photo, bg='black', relief="solid", command=lambda: show_setting())
    setting.place(x=1450, y=5)

    # to set up Back button image
    back_img = Image.open("Pictures/back.png")
    back_photo = ImageTk.PhotoImage(back_img)
    back_btn = Button(image=back_photo, bg='black', relief="solid", command=lambda: show_last_page())
    back_btn.place(x=5, y=5)

    # to set up Animal button image
    what_am_i_img = Image.open("Pictures/What_am_i.png")
    what_am_i_photo = ImageTk.PhotoImage(what_am_i_img)
    what_am_i_btn = Button(image=what_am_i_photo, bg="black", relief="solid", command=lambda: start_riddle_game(1))
    what_am_i_btn.place(x=1050, y=400)

    # to set up Birds and Insects button image
    emoji_img = Image.open("Pictures/Emoji_world.png")
    emoji_photo = ImageTk.PhotoImage(emoji_img)
    emoji_btn = Button(image=emoji_photo, bg="black", relief="solid", command=lambda: start_riddle_game(2))
    emoji_btn.place(x=1050, y=600)

    # to give background music
    mixer.music.load('Audio/Riddles.mpeg')
    mixer.music.play(-1)

    riddle_window.mainloop()                                               # to run the event loop
