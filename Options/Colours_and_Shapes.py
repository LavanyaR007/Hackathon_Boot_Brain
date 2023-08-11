# importing packages
from tkinter import *
from random import *
import random
from PIL import Image, ImageTk
from tkinter import messagebox
import time
import pygame
from pygame import mixer


# to initialize mixer
pygame.init()

start_time = time.time()

hints = ['Colours/nonagon.jpg', 'Colours/octagon.jpg', 'Colours/heptagon.jpg', 'Colours/hexagon.png', 'Colours/tri.png',
         'Colours/scalene.png', 'Colours/right.png', 'Colours/parallelogram.png', 'Colours/rhombus.png',
         'Colours/square.png', 'Colours/pentagon.png', 'Colours/circle.png', 'Colours/oval.png', 'Colours/heart.png',
         'Colours/arrow.png', 'Colours/cube.png', 'Colours/cross.png', 'Colours/cylinder.png', 'Colours/star.jpg',
         'Colours/crescent.png', 'Colours/white.png', 'Colours/yellow.png', 'Colours/blue.png', 'Colours/red.png',
         'Colours/green.png', 'Colours/black.png', 'Colours/brown.png', 'Colours/azure.png', 'Colours/ivory.png',
         'Colours/teal.png', 'Colours/silver.png', 'Colours/purple.png', 'Colours/navy.png', 'Colours/pea.png',
         'Colours/grey.png', 'Colours/orange.png', 'Colours/maroon.png', 'Colours/charcoal.png',
         'Colours/aquamarine.png', 'Colours/coral.png', 'Colours/fuchsia.png', 'Colours/wheat.png', 'Colours/lime.png',
         'Colours/crimson.png', 'Colours/khaki.png', 'Colours/hot.png', 'Colours/magenta.png', 'Colours/golden.png',
         'Colours/plum.png', 'Colours/olive.png', 'Colours/cyan.png']

colours = ['nonagon', 'octagon', 'heptagon', 'hexagon', 'triangle', 'scalene triangle', 'right triangle',
           'parallelogram', 'rhombus', 'square', 'pentagon', 'circle', 'oval', 'heart', 'arrow', 'cube', 'cross',
           'cylinder', 'star', 'crescent', 'white', 'yellow', 'blue', 'red', 'green', 'black', 'brown', 'azure',
           'ivory', 'teal', 'silver', 'purple', 'navy blue', 'pea green', 'grey', 'orange', 'maroon', 'charcoal',
           'aquamarine', 'coral', 'fuchsia', 'wheat', 'lime', 'crimson', 'khaki', 'hot pink', 'magenta', 'golden',
           'plum', 'olive', 'cyan']

ran_num = randrange(0, (len(colours)))
jumbled_rand_word = colours[ran_num]

points = 0
count = 0


def jumbled_word(words):
    words = random.sample(words, len(words))
    words_jumbled = "".join(words)
    if words_jumbled != jumbled_rand_word:
        return words_jumbled


words_shuffled = jumbled_word(jumbled_rand_word)


def main():
    # function to go back to last page
    def show_last_page():
        colours_window.destroy()
        from Options import Jumbled_Words
        Jumbled_Words.start_third_page()

    # function to show setting
    def show_setting():
        from Setting import Setting
        Setting.setting()

    # function to change the word if user cannot guess the answer
    def change():
        global ran_num, jumbled_rand_word
        sound = mixer.Sound("Audio/Change_Word.mp3")
        sound.play()

        ran_num = randrange(0, (len(colours)))
        jumbled_rand_word = colours[ran_num]
        jumbled_word(jumbled_rand_word)
        word_shuffled = jumbled_word(jumbled_rand_word)
        word.configure(text=word_shuffled)

        get_input.delete(0, END)
        time_show.configure(text="Time:")
        ans_btn.configure(state="disabled")
        ans_lab.configure(text="Answer:")

    # function to check whether the answer is correct or not
    def check():
        global points, ran_num, jumbled_rand_word, count
        user_word = get_input.get().lower()
        if user_word == colours[ran_num]:
            crt_ans = mixer.Sound("Audio/Correct_Answer.mp3")
            crt_ans.play()

            points += 5
            score.configure(text="Score:- " + str(points))

            time_taken = time.time() - start_time
            time_taken = int(time_taken)
            time_show.configure(text="Time : " + str(time_taken) + " Sec")
            messagebox.showinfo('Correct', "Correct Answer.. Keep it Up!")

            ran_num = randrange(0, (len(colours)))
            jumbled_rand_word = colours[ran_num]
            jumbled_word(jumbled_rand_word)
            word_shuffled = jumbled_word(jumbled_rand_word)
            word.configure(text=word_shuffled)

            get_input.delete(0, END)
            ans_lab.configure(text="Answer:")
            ans_btn.configure(state="disabled")
            time_show.configure(text="Time:")
            crt_ans.stop()
        else:
            wrg_ans = mixer.Sound("Audio/Wrong_Answer.mp3")
            wrg_ans.play()
            if user_word == "":
                messagebox.showerror("Error", "Please Enter your guess")
            elif count == 1:
                messagebox.showerror("Error", "Incorrect Answer..Try your best!")
                get_input.delete(0, END)
                ans_btn.configure(state="normal")
            else:
                messagebox.showerror("Error", "Incorrect Answer..Try your best!\n Or look for hint\nEnter your guess")
                get_input.delete(0, END)
        count = 0

    def show_answer():
        global points
        if points > 4:
            points -= 5
            score.configure(text="Score:- " + str(points))
            ans_lab.configure(text='Answer:' + jumbled_rand_word)
        else:
            wrg_ans = mixer.Sound("Audio/Wrong_Answer.mp3")
            wrg_ans.play()
            messagebox.showerror("Answer", "Sorry!!!Not Enough Points")

    def show_hint():
        global points, count
        count = 1
        if points > 4:
            hint = mixer.Sound("Audio/Hint.mp3")
            hint.play()
            points -= 2
            score.configure(text="Score:- " + str(points))

            hint_window = Toplevel()
            hint_window.title("Hint Window")
            hint_window.wm_iconbitmap("Pictures/logo.ico")
            hint_window.geometry("500x500+1000+200")
            hint_window.resizable(0, 0)

            an_img = Image.open(hints[ran_num])
            resize_img = an_img.resize((500, 500), Image.ANTIALIAS)
            an_photo = ImageTk.PhotoImage(resize_img)
            hin_img = Label(hint_window, image=an_photo)
            hin_img.pack()
            hint_window.after(10000, hint_window.destroy)                                      # milliseconds
            hint_window.mainloop()
        else:
            wrg_ans = mixer.Sound("Audio/Wrong_Answer.mp3")
            wrg_ans.play()
            messagebox.showerror("Hint", "Sorry!!!Not Enough Points")

    colours_window = Tk()                                                                         # creation of window
    colours_window.title("Boot Brain \U0001F9E0-----Jumbled Words~Colours and Shapes")            # to show window title
    colours_window.configure(background="black")                                              # window background colour
    colours_window.wm_iconbitmap('Pictures/logo.ico')                                             # to show window icon
    colours_window.geometry("1540x825+0+0")                                                 # window size(width,height)
    colours_window.resizable(0, 0)                                               # to restrict user from resizing window

    # to set up background image
    colours_img = Image.open("Pictures/Jumbled_words.jpg")
    colours_photo = ImageTk.PhotoImage(colours_img)
    back_image = Label(image=colours_photo)
    back_image.pack()

    # to set up setting button image
    setting_img = Image.open("Pictures/setting.jpg")
    setting_photo = ImageTk.PhotoImage(setting_img)
    setting = Button(image=setting_photo, bg='black', relief="solid", command=lambda: show_setting())
    setting.place(x=1200, y=120)

    # to show time taken
    time_show = Label(text="Time:", bg="#B45F06", fg="black", relief="solid", font="Cambria 16 italic")
    time_show.place(x=600, y=120)

    # to show score
    score = Label(text="Score:- 0", bg="#B45F06", fg="black", relief="solid", font="Cambria 16 italic")
    score.place(x=900, y=120)

    word = Label(text=words_shuffled, bg="black", fg="white", font="Cambria  30 bold")
    word.place(x=700, y=190)

    get_input = Entry(font="none 26 bold", borderwidth=10, justify='center')
    get_input.place(x=570, y=250)

    # to set up submit button
    submit_img = Image.open("Pictures/Submit.png")
    submit_photo = ImageTk.PhotoImage(submit_img)
    submit_btn = Button(image=submit_photo, bg="black", justify='center', relief="solid", command=lambda: check())
    submit_btn.place(x=650, y=320)

    # to set up change word button
    change_img = Image.open("Pictures/Change_word.png")
    change_photo = ImageTk.PhotoImage(change_img)
    change_btn = Button(image=change_photo, bg="black", justify='center', relief="solid", command=lambda: change())
    change_btn.place(x=650, y=400)

    # to set up hint button
    hint_img = Image.open("Pictures/Hint.png")
    hint_photo = ImageTk.PhotoImage(hint_img)
    hint_btn = Button(image=hint_photo, bg="black", justify='center', relief="solid", command=lambda: show_hint())
    hint_btn.place(x=650, y=480)

    # to set up answer button
    ans_img = Image.open("Pictures/Answer.png")
    ans_photo = ImageTk.PhotoImage(ans_img)
    ans_btn = Button(image=ans_photo, bg="black", relief="solid", command=lambda: show_answer())
    ans_btn.place(x=650, y=560)
    ans_btn.configure(state="disabled")

    ans_lab = Label(text="Answer:", bg="#B45F06", fg="black", font="Cambria 12 bold")
    ans_lab.place(x=650, y=660)

    # to set up Back button image
    back_img = Image.open("Pictures/back.png")
    back_photo = ImageTk.PhotoImage(back_img)
    back_btn = Button(image=back_photo, bg='black', relief="solid", command=lambda: show_last_page())
    back_btn.place(x=200, y=120)

    colours_window.mainloop()                                                          # to run the event loop
