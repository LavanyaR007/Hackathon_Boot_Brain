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

riddles = \
 ['I  have  two  hands, but  I  can  not  scratch  myself.\n What  am  I?',
  'I  am  a  seed  with  three  letters  in  my  name.\nTake  away  the  last  two  and  I  still  sound  the  same.'
  '\nWhat am I?',
  'What  has  to  be  broken  before  you  can  use  it?',
  'What  has  one  eye  but  cannot  see?',
  'What  begins  with  T  ends  with  T  and  has  T  in  it?',
  'What  occurs  once  in  a  minute,  twice  in  a  moment,\n and  never  in  one  thousand  years?',
  'What  is  full  of  holes  but  still  holds  water?',
  'Turn  us  on  our  backs  and  open  up  our  stomachs,\n and  you  will  be  the  wisest  but  at  the  start  a  '
  'lummox.\nWhat  are  we?',
  'What  is  always  in  front  of  you  but  can’t  be  seen?',
  'Where  can  you  find  cities, towns, shops, and  streets  but  no  people?',
  'I  am  an  odd  number.\n Take  away  a  letter  and  I  become  even. \nWhat number am I?',
  'What  goes  up  but  never  comes  back  down?',
  'I’m  tall  when  I’m  young, and  I’m  short  when  I’m  old.\nWhat  am  I?',
  'What  type  of  cheese  is  made  backwards?',
  'What  has  a  neck  but  no  head?',
  'How  many  months  of  the  year  have  28  days?',
  'What  needs  an  answer  but  does  not  ask  a  question?',
  'What  is  as  light  as  a  feather  but  even  the  \nstrongest  man  in  the  world  can’t  hold  it  for  long?',
  'Forward  I  am  heavy, but  backward  I  am  not. \nWhat  am  I?',
  'Poor  people  have  it. Rich  people  need  it.\n If  you  eat  it  you  die. What  is  it?',
  'What’s  bright  orange  with  green  on  top  \nand  sounds  like  a  parrot?',
  'What  word  contains  26  letters,  but  only  has  three  syllables?',
  'I  am  often  following  you  and  copying  your  every  move. \nYet  you  can  never  touch  me  or  catch  me. '
  '\nWhat  am  I?',
  'I  add  lots  of  flavor  and  have  many  layers,but  if  you  \nget  to  close  I’ll  make  you  cry.What  am  I?',
  'What  can  you  break, even  if  you  never  pick  it  up  or  touch  it?',
  'Come  up  and  we  go, Go  down  and  we  stay.',
  'White  and  thin,  red  within,  with  a  nail  at  the  end.\n What  is  it?',
  'It  can  be  said: To  be  gold  is  to  be  good; \nTo  be  stone  is  to  be  nothing;\n To  be  glass  is  to  be'
  ' fragile; \nTo  be  cold  is  to  be  cruel; \nUnmetaphored, what am I?',
  'Give  me  food  and  I  will  live, \nGive  me  water, and  I  will  die.',
  'Use  me  well  and  I  am  everybody, \nScratch  my  back  and  I  am  nobody.']

answer = ['clock', 'pea', 'egg', 'needle', 'teapot', 'm', 'sponge', 'books', 'future', 'map', 'seven', 'age', 'candle',
          'edam', 'bottle', '12', 'telephone', 'breath', 'ton', 'nothing', 'carrot', 'alphabet', 'shadow',
          'onion', 'promise', 'anchor', 'finger', 'heart', 'fire', 'mirror']

ran_num = randrange(0, (len(riddles)))
rand_word = riddles[ran_num]

points = 0


def main():
    def show_last_page():
        what_am_i_window.destroy()
        from Options import Riddles
        Riddles.start_fourth_page()

    def show_setting():
        from Setting import What_am_I_Setting                             # to import Setting.py program
        What_am_I_Setting.setting()                                       # to call the setting() from Setting.py

    def change():
        global ran_num
        sound = mixer.Sound("Audio/Change_Word.mp3")
        sound.play()
        ran_num = randrange(0, (len(riddles)))
        word.configure(text=riddles[ran_num])
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

            ran_num = randrange(0, (len(riddles)))
            word.configure(text=riddles[ran_num])
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

    what_am_i_window = Tk()                                                                      # creation of window
    what_am_i_window.title("Boot Brain \U0001F9E0----->Riddles~What Am I")                       # to show window title
    what_am_i_window.configure(background="black")                                            # window background colour
    what_am_i_window.wm_iconbitmap('Pictures/logo.ico')                                          # to show window icon
    what_am_i_window.geometry("1540x825+0+0")                                               # window size(width,height)
    what_am_i_window.resizable(0, 0)                                             # to restrict user from resizing window

    canvas = Canvas(what_am_i_window, width=1540, height=825)
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

    word = Label(text=rand_word, bg="black", fg="white", font="Cambria  14 italic")
    word.place(x=900, y=150)

    get_input = Entry(font="none 26 bold", borderwidth=10, justify='center')
    get_input.place(x=900, y=270)

    # to set up submit button
    submit_img = Image.open("Pictures/Submit.png")
    submit_photo = ImageTk.PhotoImage(submit_img)
    submit_btn = Button(image=submit_photo, bg="black", justify='center', relief="solid", command=lambda: check())
    submit_btn.place(x=970, y=350)

    # to set up change word button
    change_img = Image.open("Pictures/Change_word.png")
    change_photo = ImageTk.PhotoImage(change_img)
    change_btn = Button(image=change_photo, bg="black", justify='center', relief="solid", command=lambda: change())
    change_btn.place(x=970, y=450)

    # to set up answer button
    ans_img = Image.open("Pictures/Answer.png")
    ans_photo = ImageTk.PhotoImage(ans_img)
    ans_btn = Button(image=ans_photo, bg="black", relief="solid", command=lambda: show_answer())
    ans_btn.place(x=970, y=550)
    ans_btn.configure(state="disabled")

    ans_lab = Label(text="Answer: ", bg="black", fg="white", font="Cambria 14 italic")
    ans_lab.place(x=970, y=650)

    # to set up Back button image
    back_img = Image.open("Pictures/back.png")
    back_photo = ImageTk.PhotoImage(back_img)
    back_btn = Button(image=back_photo, bg='black', relief="solid", command=lambda: show_last_page())
    back_btn.place(x=5, y=3)

    what_am_i_window.mainloop()                                                          # to run the event loop
