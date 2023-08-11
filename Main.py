from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import scrolledtext
from PIL import Image, ImageTk
import time
import pygame
from pygame import mixer

# to initialize mixer
pygame.init()


main_window = Tk()
main_window.title("Boot Brain \U0001F9E0")
main_window.wm_iconbitmap('Pictures/logo.ico')
main_window.configure(bg='black')
main_window.geometry("1540x825+0+0")
main_window.resizable(0, 0)

img = Image.open("Pictures/logo.ico")
photo = ImageTk.PhotoImage(img)
back_image = Label(image=photo, relief="solid")
back_image.place(x=0, y=0)

back_image1 = Label(image=photo, relief="solid")
back_image1.place(x=1250, y=650)

lab = Label(main_window, text="BOOT  BRAIN", font="Harrington 50 ", bg="black", fg="white")
lab.place(x=650, y=10)

txt = scrolledtext.ScrolledText(main_window, width=100, height=17, bg="black", fg="white", font="Cambria 14 italic",
                                relief="solid")
txt.insert(INSERT, '                                                              Grades  don’t  measure  Intelligence,'
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
txt.place(x=300, y=200)


def start():
    bar = Progressbar(main_window, orient=HORIZONTAL, length=500, mode='determinate')
    bar.place(x=550, y=700)

    label = Label(main_window, text="Loading.....")
    label.place(x=770, y=670)
    for x in range(11):
        bar['value'] += 10
        main_window.update_idletasks()
        time.sleep(1)

    main_window.destroy()
    import Main_page
    Main_page.start_main_page()


nxt_img = Image.open("Pictures/next.png")
nxt_photo = ImageTk.PhotoImage(nxt_img)
nxt = Button(main_window, image=nxt_photo, bg="black", relief="solid",  command=start)
nxt.place(x=700, y=730)

# to give background music
#mixer.music.load('Audio/Main.mpeg')
#mixer.music.play(-1)

main_window.mainloop()
