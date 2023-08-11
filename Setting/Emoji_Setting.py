# importing packages
from tkinter import *
from tkinter import scrolledtext
from PIL import Image, ImageTk
import pygame
from pygame import mixer

# to initialize mixer
pygame.init()


# setting()
def setting():
    def about_game():
        about_window = Toplevel()                                      # to represent information about game
        about_window.title("About Game")                               # to show window title
        about_window.wm_iconbitmap("Pictures/logo.ico")                # to show window icon
        about_window.configure(bg="black")                             # window background colour
        about_window.minsize(1020, 400)                                 # window size(width,height)
        about_window.resizable(0, 0)                                   # to restrict user from resizing window

        txt = scrolledtext.ScrolledText(about_window, width=100, height=17, bg="black", fg="white",
                                        font="Cambria 14 italic",
                                        relief="solid")
        txt.insert(INSERT,
                   '                                                              Grades  don’t  measure  Intelligence,'
                   '\n                                                                 Age  does  not  define  maturity'
                   '.\nThis  game  is  a  simple  undertaking  for  supporting  children  grow  in  IQ. Click  on  the '
                   'NEXT  Button  to  start  the  game       after  you  read  the  rules  and  learn  about  the  game'
                   '.\n 1. Click  on  start  button. \n 2. Select  your  category - either  Jumbled  words  or  Riddles'
                   '.\n 3. After  selecting  your  category  -\n             a) if  you  have  selected  Jumbled  words'
                   '  category  there  are  - animals , birds  and  insects , body  parts  and  internal     organs , '
                   'colours  and  shapes , vehicles , vegetables , fruits  categories.\n             b) if  you  have  '
                   'selected  Riddles  category  there  are - What  am  I ?  and  Emoji  world.\n\n How  does  the  '
                   'game  work ?\n1. You  have  to  enter  your  guess - \n                a) if  correct  you  are  '
                   'given  5  points.\n                b) if  wrong  you  can  click  on  HINT  button  and  image  '
                   'related  to  answer  is  popped  up  and  you  are  given  only  10  seconds  to  see  the  hint  '
                   'and  the  hint  window  destroys  itself  and  2  points  are  cut  down  from  ur  current  score.'
                   '\n\n2. If  you  have  no  points  or  less  points  you  can  change  the  word , and  no  points  '
                   'are  cut  down  for  this.\n\n 3. The  answer  button  is  enabled  only  after  you  have  seen  '
                   'hint  and  you  have  made  mistake  and  5  points  are  cut  down  from  your  current  score.'
                   '\n\n4. There  is  a  time  label  to  show  how  much  time  you  have  taken  to  answer.'
                   '\n\n\n              There  is  a  back  button  to  go  back.\n\n\n      There  is  a  Setting  '
                   'button  where  you  can  see  this  rules  and  you  can  off  or  on  the  background  music.'
                   '\n\n\n                                                                                             '
                   '                                                                                       Thank  You,'
                   '\n                                                                                                 '
                   '                                                          Hope  you  guys  enjoy  our  small  game')
        txt.configure(state='disabled')
        txt.place(x=0, y=0)
        about_window.mainloop()

    def on():
        mixer.music.load('Audio/Guess_the_emoji.mpeg')
        mixer.music.play(-1)

    def off():
        mixer.music.stop()

    setting_window = Toplevel()                                       # to represent some extra information
    setting_window.title("Settings")                                  # to show window title
    setting_window.wm_iconbitmap("Pictures/setting_icon.ico")         # to show window icon
    setting_window.configure(bg="black")                              # window background colour
    setting_window.minsize(450, 250)                                  # window size(width,height)
    setting_window.resizable(0, 0)                                    # to restrict user from resizing window

    # to set up About_Game button image
    about_img = Image.open("Pictures/About_Game.png")
    about_photo = ImageTk.PhotoImage(about_img)
    about = Button(setting_window, image=about_photo, bg='black', relief="solid", command=lambda: about_game())
    about.place(x=100, y=80)

    # to set up Audio_on button image
    audio_on = Image.open("Pictures/Audio_on.jpg")
    audio_photo = ImageTk.PhotoImage(audio_on)
    audio_btn = Button(setting_window, image=audio_photo, bg='black', relief="solid", command=lambda: on())
    audio_btn.place(x=100, y=200)

    # to set up Mute button image
    audio_of = Image.open("Pictures/Mute.jpg")
    audio_photo1 = ImageTk.PhotoImage(audio_of)
    audio_btn = Button(setting_window, image=audio_photo1, bg='black', relief="solid", command=lambda: off())
    audio_btn.place(x=200, y=200)

    setting_window.mainloop()
