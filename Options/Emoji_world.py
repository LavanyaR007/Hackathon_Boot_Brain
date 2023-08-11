# importing packages
from tkinter import *
from random import *
from PIL import Image, ImageTk, ImageSequence
from tkinter import messagebox
import time
import pygame
from pygame import mixer


# to initialize mixer
pygame.init()

start_time = time.time()

emoji = ['\U0001F436 \U000026A1', '\U0001F478\U0001F478\U00002744\U000026C4', '\U0001F476\U0001F9DC', '\U0001F925',
         '\U0001F50D\U0001F921\U0001F41F', '\U0001F478\U0001F438', '\U0001F467\U0001F383\U0001F3F0\U0001F460\U0001F478',
         '\U0001F388\U0001F388\U0001F388\U0001F3E0\U0001F468', '\U0001F467\U0001F5E1\U0001F479\U0001F409',
         '\U0001F52B\U0001F4D6', '\U0001F418\U0001F3AA', '\U0001F634\U0001F467', '\U0001F981\U0001F451',
         '\U0001F467\U0001F479\U0001F940', '\U0001F5A4\U0001F411']

category = ['MOVIE', 'MOVIE', 'MOVIE', 'MOVIE', 'MOVIE', 'MOVIE', 'MOVIE', 'MOVIE', 'MOVIE', 'MOVIE', 'MOVIE', 'MOVIE',
            'MOVIE', 'MOVIE', 'RHYMES']

answer = ['bolt', 'frozen', 'the little mermaid', 'pinocchio', 'finding nemo', 'the princess and the frog',
          'cinderella', 'up', 'mulan', 'toy story', 'dumbo', 'sleeping beauty', 'the lion king', 'beauty and the beast',
          'ba ba black sheep']

ran_num = randrange(0, (len(emoji)))
rand_word = emoji[ran_num]
category_word = category[ran_num]
points = 0


def main():
    def show_last_page():
        emoji_window.destroy()
        from Options import Riddles
        Riddles.start_fourth_page()

    def show_setting():
        from Setting import What_am_I_Setting                             # to import Setting.py program
        What_am_I_Setting.setting()                                       # to call the setting() from Setting.py

    def change():
        global ran_num
        sound = mixer.Sound("Audio/Change_Word.mp3")
        sound.play()
        ran_num = randrange(0, (len(emoji)))
        word.configure(text=emoji[ran_num])
        category_lab.configure(text=category[ran_num])
        get_input.delete(0, END)
        time_show.configure(text="Time:")
        ans_btn.configure(state="disabled")
        ans_lab.configure(text="Answer:")

    def check():
        global points, ran_num
        user_word = get_input.get().lower()
        if user_word == answer[ran_num]:
            crt_ans = mixer.Sound("Audio/Correct_Answer.mp3")
            crt_ans.play()

            points += 5
            score.configure(text="Score:- " + str(points))

            time_taken = time.time() - start_time
            time_taken = int(time_taken)
            time_show.configure(text="Time : " + str(time_taken) + " Sec")
            messagebox.showinfo('Correct', "Correct Answer.. Keep it Up!")

            ran_num = randrange(0, (len(emoji)))
            word.configure(text=emoji[ran_num])
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
            else:
                messagebox.showerror("Error", "Incorrect Answer..Try your best!")
                get_input.delete(0, END)
                ans_btn.configure(state="normal")

    def show_answer():
        global points
        if points > 4:
            points -= 5
            score.configure(text="Score:- " + str(points))
            ans_lab.configure(text='Answer:' + answer[ran_num])
        else:
            wrg_ans = mixer.Sound("Audio/Wrong_Answer.mp3")
            wrg_ans.play()
            messagebox.showerror("Answer", "Sorry!!!Not Enough Points")

    def animate(counter):
        canvas.itemconfig(image, image=sequence[counter])
        canvas.after(150, lambda: animate((counter + 1) % len(sequence)))

    emoji_window = Tk()                                                                      # creation of window
    emoji_window.title("Boot Brain \U0001F9E0----->Riddles~Emoji World")                       # to show window title
    emoji_window.configure(background="black")                                            # window background colour
    emoji_window.wm_iconbitmap('Pictures/logo.ico')                                          # to show window icon
    emoji_window.geometry("1540x825+0+0")                                                    # window size(width,height)
    emoji_window.resizable(0, 0)                                             # to restrict user from resizing window

    canvas = Canvas(emoji_window, width=1540, height=825)
    canvas.pack()
    sequence = [ImageTk.PhotoImage(img)
                for img in ImageSequence.Iterator(Image.open(r'Riddle_video.gif'))]
    image = canvas.create_image(770, 412, image=sequence[0])
    animate(1)

    # to set up setting button image
    setting_img = Image.open("Pictures/setting.jpg")
    setting_photo = ImageTk.PhotoImage(setting_img)
    setting = Button(image=setting_photo, bg='black', relief="solid", command=lambda: show_setting())
    setting.place(x=1450, y=5)

    # to show time taken
    time_show = Label(text="Time:", bg="black", fg="white", relief="solid", font="Cambria 16 italic")
    time_show.place(x=550, y=80)

    # to show score
    score = Label(text="Score:- 0", bg="black", fg="white", relief="solid", font="Cambria 16 italic")
    score.place(x=1350, y=80)

    word = Label(text=rand_word, bg="black", fg="white", font="Cambria  50", justify='center')
    word.place(x=950, y=250)

    get_input = Entry(font="none 26 bold", borderwidth=10, justify='center')
    get_input.place(x=900, y=370)

    # to set up submit button
    submit_img = Image.open("Pictures/Submit.png")
    submit_photo = ImageTk.PhotoImage(submit_img)
    submit_btn = Button(image=submit_photo, bg="black", justify='center', relief="solid", command=lambda: check())
    submit_btn.place(x=970, y=450)

    # to set up change word button
    change_img = Image.open("Pictures/Change_word.png")
    change_photo = ImageTk.PhotoImage(change_img)
    change_btn = Button(image=change_photo, bg="black", justify='center', relief="solid", command=lambda: change())
    change_btn.place(x=970, y=550)

    # to set up answer button
    ans_img = Image.open("Pictures/Answer.png")
    ans_photo = ImageTk.PhotoImage(ans_img)
    ans_btn = Button(image=ans_photo, bg="black", relief="solid", command=lambda: show_answer())
    ans_btn.place(x=970, y=650)
    ans_btn.configure(state="disabled")

    ans_lab = Label(text="Answer: ", bg="black", fg="white", font="Cambria 14 italic")
    ans_lab.place(x=970, y=750)

    category_lab = Label(text=category_word,  bg="black", fg="white", font="Cambria 20 ", justify='center')
    category_lab.place(x=1050, y=150)

    # to set up Back button image
    back_img = Image.open("Pictures/back.png")
    back_photo = ImageTk.PhotoImage(back_img)
    back_btn = Button(image=back_photo, bg='black', relief="solid", command=lambda: show_last_page())
    back_btn.place(x=5, y=3)

    emoji_window.mainloop()                                                          # to run the event loop
