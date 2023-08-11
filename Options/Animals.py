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

hints = ['Animals/giraffe.jpg', 'Animals/deer.jpg', 'Animals/horse.jpg', 'Animals/sheep.jpg', 'Animals/squirrel.jpg', 
         'Animals/dog.jpg', 'Animals/cat.jpg', 'Animals/pig.jpg', 'Animals/lion.jpg', 'Animals/monkey.jpg',
         'Animals/elephant.jpg', 'Animals/mouse.jpg', 'Animals/fox.jpeg', 'Animals/kangaroo.jpg', 'Animals/cow.jpg',
         'Animals/goat.jpg', 'Animals/otter.jpg', 'Animals/raccoon.jpg', 'Animals/hippo.jpg', 'Animals/mole.jpg',
         'Animals/chimpanzee.jpg', 'Animals/walrus.jpg', 'Animals/bat.jpg', 'Animals/hedgehog.jpg', 'Animals/panda.jpg',
         'Animals/rabbit.jpg', 'Animals/zebra.jpg', 'Animals/tiger.jpg', 'Animals/turtle.jpg', 'Animals/hamster.jpg',
         'Animals/chipmunk.jpg', 'Animals/badger.jpg', 'Animals/Antelope.jpg', 'Animals/bear.jpg', 'Animals/camel.jpg',
         'Animals/gorilla.jpg', 'Animals/koala.jpg', 'Animals/leopard.jpg', 'Animals/rhino.jpg', 'Animals/possum.jpg',
         'Animals/porcupine.jpg', 'Animals/wombat.jpg', 'Animals/bison.jpg', 'Animals/wolf.jpg', 'Animals/r_panda.jpg',
         'Animals/donkey.jpg', 'Animals/lynx.jpg', 'Animals/orangutan.jpg', 'Animals/okapi.jpg', 'Animals/reindeer.jpg',
         ]

animals = ['giraffe', 'deer', 'horse', 'sheep', 'squirrel', 'dog', 'cat', 'pig', 'lion', 'monkey', 'elephant', 'mouse',
           'fox', 'kangaroo', 'cow', 'goat', 'otter', 'raccoon', 'hippopotamus', 'mole', 'chimpanzee', 'walrus', 'bat',
           'hedgehog', 'panda', 'rabbit', 'zebra', 'tiger', 'turtle', 'hamster', 'chipmunk', 'badger', 'antelope',
           'bear', 'camel', 'gorilla', 'koala', 'leopard', 'rhinoceros', 'possum', 'porcupine', 'wombat', 'bison',
           'wolf', 'red panda', 'donkey', 'lynx', 'orangutan', 'okapi', 'reindeer']

ran_num = randrange(0, (len(animals)))
jumbled_rand_word = animals[ran_num]

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
        animal_window.destroy()
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

        ran_num = randrange(0, (len(animals)))
        jumbled_rand_word = animals[ran_num]
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
        if user_word == animals[ran_num]:
            crt_ans = mixer.Sound("Audio/Correct_Answer.mp3")
            crt_ans.play()

            points += 5
            score.configure(text="Score:- " + str(points))

            time_taken = time.time() - start_time
            time_taken = int(time_taken)
            time_show.configure(text="Time : " + str(time_taken) + " Sec")
            messagebox.showinfo('Correct', "Correct Answer.. Keep it Up!")

            ran_num = randrange(0, (len(animals)))
            jumbled_rand_word = animals[ran_num]
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

    animal_window = Tk()                                                         # creation of window
    animal_window.title("Boot Brain \U0001F9E0-----Jumbled Words~Animals")       # to show window title
    animal_window.configure(background="black")                                  # window background colour
    animal_window.wm_iconbitmap('Pictures/logo.ico')                             # to show window icon
    animal_window.geometry("1540x825+0+0")                                       # window size(width*height+right+down)
    animal_window.resizable(0, 0)                                                # to restrict user from resizing window

    # to set up background image
    animal_img = Image.open("Pictures/Animals_back.png")
    animal_photo = ImageTk.PhotoImage(animal_img)
    back_image = Label(image=animal_photo)
    back_image.pack()

    # to set up setting button image
    setting_img = Image.open("Pictures/setting.jpg")
    setting_photo = ImageTk.PhotoImage(setting_img)
    setting = Button(image=setting_photo, bg='black', relief="solid", command=lambda: show_setting())
    setting.place(x=1200, y=3)

    # to show time taken
    time_show = Label(text="Time:", bg="#B45F06", fg="black", relief="solid", font="Cambria 16 italic")
    time_show.place(x=400, y=50)

    # to show score
    score = Label(text="Score:- 0", bg="#B45F06", fg="black", relief="solid", font="Cambria 16 italic")
    score.place(x=1000, y=50)

    word = Label(text=words_shuffled, bg="black", fg="white", font="Cambria  30 bold")
    word.place(x=700, y=100)

    get_input = Entry(font="none 26 bold", borderwidth=10, justify='center')
    get_input.place(x=570, y=190)

    # to set up submit button
    submit_img = Image.open("Pictures/Submit.png")
    submit_photo = ImageTk.PhotoImage(submit_img)
    submit_btn = Button(image=submit_photo, bg="black", justify='center', relief="solid", command=lambda: check())
    submit_btn.place(x=650, y=270)

    # to set up change word button
    change_img = Image.open("Pictures/Change_word.png")
    change_photo = ImageTk.PhotoImage(change_img)
    change_btn = Button(image=change_photo, bg="black", justify='center', relief="solid", command=lambda: change())
    change_btn.place(x=650, y=350)

    # to set up hint button
    hint_img = Image.open("Pictures/Hint.png")
    hint_photo = ImageTk.PhotoImage(hint_img)
    hint_btn = Button(image=hint_photo, bg="black", justify='center', relief="solid", command=lambda: show_hint())
    hint_btn.place(x=650, y=430)

    # to set up answer button
    ans_img = Image.open("Pictures/Answer.png")
    ans_photo = ImageTk.PhotoImage(ans_img)
    ans_btn = Button(image=ans_photo, bg="black", relief="solid", command=lambda: show_answer())
    ans_btn.place(x=650, y=510)
    ans_btn.configure(state="disabled")

    ans_lab = Label(text="Answer:", bg="#B45F06", fg="black", font="Cambria 12 bold")
    ans_lab.place(x=650, y=620)

    # to set up Back button image
    back_img = Image.open("Pictures/back.png")
    back_photo = ImageTk.PhotoImage(back_img)
    back_btn = Button(image=back_photo, bg='black', relief="solid", command=lambda: show_last_page())
    back_btn.place(x=335, y=3)

    animal_window.mainloop()                                                          # to run the event loop
