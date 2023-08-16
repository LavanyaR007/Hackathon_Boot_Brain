# Core Packages
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog, messagebox, scrolledtext
from tkinter.scrolledtext import *
import tkinter.filedialog
import tensorflow as tf
import cv2
import os
from gtts import gTTS
import numpy as np
from PIL import Image, ImageTk, ImageFilter, ImageEnhance
import pyttsx3
from random import *
import random
from tkinter import messagebox
import time
import pygame
from pygame import mixer

# NLP Pkgs
from spacy_summarization import text_summarizer
from nltk_summarization import nltk_summarizer

# Web Scraping Pkg
from bs4 import BeautifulSoup
from urllib.request import urlopen


# to initialize mixer
pygame.init()

start_time = time.time()

hints = ['Fruits/apple.jpg', 'Fruits/acai.jpg', 'Fruits/apricot.jpg', 'Fruits/avocado.jpg', 'Fruits/banana.jpg',
         'Fruits/blue.jpg', 'Fruits/cherry.jpg', 'Fruits/custard.jpg', 'Fruits/cantaloupe.jpg', 'Fruits/carambola.jpg',
         'Fruits/coconut.jpg', 'Fruits/plum.jpg', 'Fruits/dates.jpg', 'Fruits/dewberry.jpg', 'Fruits/dragon.jpg',
         'Fruits/eggfruit.jpg', 'Fruits/fig.jpg', 'Fruits/feijoa.jpg', 'Fruits/grapefruit.jpg', 'Fruits/grapes.jpg',
         'Fruits/gooseberry.jpg', 'Fruits/guava.jpg', 'Fruits/honeydew.jpg', 'Fruits/honey.jpg', 'Fruits/jujube.jpg',
         'Fruits/jackfruit.jpg', 'Fruits/kiwi.jpg', 'Fruits/kiwano.jpg', 'Fruits/kumquat.jpg', 'Fruits/lime.jpg',
         'Fruits/lychee.jpg', 'Fruits/loquat.jpg', 'Fruits/mango.jpg', 'Fruits/mulberry.jpg', 'Fruits/melon.jpg',
         'Fruits/mangosteen.jpg', 'Fruits/monk.jpg', 'Fruits/nectarine.jpg', 'Fruits/makoy.jpg', 'Fruits/pear.jpg',
         'Fruits/olive.jpg', 'Fruits/orange.jpg', 'Fruits/papaya.jpg', 'Fruits/persimmon.jpg', 'Fruits/prickly.jpg',
         'Fruits/peach.jpg', 'Fruits/pomegranate.jpg', 'Fruits/pineapple.jpg', 'Fruits/palm.jpg', 'Fruits/quince.jpg',
         'Fruits/raspberry.jpg', 'Fruits/red.jpg', 'Fruits/strawberry.jpg', 'Fruits/soursop.jpg', 'Fruits/salak.jpg',
         'Fruits/star.jpg', 'Fruits/sloe.jpg', 'Fruits/sweet.jpg', 'Fruits/sugar.jpg', 'Fruits/tomato.jpg',
         'Fruits/tangerine.jpg', 'Fruits/tamarind.jpg', 'Fruits/tart.jpg', 'Fruits/vanilla.jpg', 'Fruits/water.jpg',
         'Fruits/wolfberry.jpg', 'Fruits/white.jpg', 'Fruits/bael.jpg', 'Fruits/yam.jpg', 'Fruits/zucchini.jpg', ]

fruits = ['apple', 'acai berry', 'apricot', 'avocado', 'banana', 'blueberry', 'cherry', 'custard apple', 'cantaloupe',
          'carambola', 'coconut', 'plum', 'dates', 'dewberry', 'dragon fruit', 'eggfruit', 'fig', 'feijoa',
          'grapefruit', 'grapes', 'gooseberry', 'guava', 'honeydew melon', 'honey berry', 'jujube fruit', 'jackfruit',
          'kiwi', 'kiwano', 'kumquat', 'lime', 'lychee', 'loquat', 'mango', 'mulberry', 'melon', 'mangosteen',
          'monk fruit', 'nectarine', 'makoy fruit', 'pear', 'olive', 'orange', 'papaya', 'persimmon', 'prickly pear',
          'peach', 'pomegranate', 'pineapple', 'palm fruit', 'quince', 'raspberry', 'red banana', 'strawberry',
          'soursop', 'salak', 'star apple', 'sloe', 'sweet potato', 'sugar cane', 'tomato', 'tangerine', 'tamarind',
          'tart cherry', 'vanilla bean', 'watermelon', 'wolfberry', 'white mulberry', 'bael', 'yam bean', 'zucchini']

ran_num = randrange(0, (len(fruits)))
jumbled_rand_word = fruits[ran_num]

points = 0
count = 0

labels = ["Apple", "Banana", "Beetroot", "Cabbage", "Carrot", "Grapes", "Guva", "Mango", "Lady's Finger",
                      "Pumpkin"]

model = tf.keras.models.load_model(os.getcwd() + '\model.h5')
prediction_index=-1
# Structure and Layout
window = Tk()
window.title("Object Detection and Summarizer")
window.geometry("1250x750+150+50")
#window.wm_iconbitmap("logo.ico")
window.config(background="#06283d")
window.resizable(False,False)

Label(window,text="Team: Dynamite\nEmail: lavanya.r@mca.christuniversity.in\nvibishna.b@mca.christuniversity.in",width=10,height=3,bg="#f0687c",anchor='e').pack(side=TOP,fill=X)
Label(window,text="BOOT BRAIN",width=10,height=2,bg="#06283d",fg="#fff",font='arial 20 bold').pack(side=TOP,fill=X)
Label(window,text="HACKATHON INTEL ONE API \t\t\t\t\t\t\t\t\t Libraries used:Tensorflow,openCV,oneDNN",width=10,height=2,bg="#c36464",fg="#fff",font='arial 12 bold').pack(side=BOTTOM,fill=X)


style = ttk.Style(window)
style.configure('lefttab.TNotebook', tabposition='wn',)
style.configure('lefttab.TNotebook.Tab', background='lightblue')


# TAB LAYOUT
tab_control = ttk.Notebook(window,style='lefttab.TNotebook')

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)


# ADD TABS TO NOTEBOOK
tab_control.add(tab1, text=f'{"Home":^20s}')
tab_control.add(tab2, text=f'{"Text":^20s}')
tab_control.add(tab3, text=f'{"File":^20s}')
tab_control.add(tab4, text=f'{"URL":^20s}')
tab_control.add(tab5, text=f'{"JUMBLED GAME":^20s}')

label1 = Label(tab1, text= 'Object Detection',padx=5, pady=5,font='arial 20 bold')
label1.grid(column=3, row=0)

label2 = Label(tab2, text= 'Summaryzer',padx=5, pady=5,font='arial 20 bold')
label2.grid(column=1, row=0)

label3 = Label(tab3, text= 'File Processing',padx=5, pady=5,font='arial 20 bold')
label3.grid(column=2, row=0)

label4 = Label(tab4, text= 'URL',padx=5, pady=5,font='arial 20 bold')
label4.grid(column=1, row=0)

label5 = Label(tab5, text= 'JUMBLED GAME',padx=5, pady=5,font='arial 20 bold')
label5.grid(column=4, row=0)

tab_control.pack(expand=1, fill='both')


# Functions
def jumbled_word(words):
   words = random.sample(words, len(words))
   words_jumbled = "".join(words)
   if words_jumbled != jumbled_rand_word:
      return words_jumbled


words_shuffled = jumbled_word(jumbled_rand_word)


# function to change the word if user cannot guess the answer
def change():
  global ran_num, jumbled_rand_word
  sound = mixer.Sound("Audio/Change_Word.mp3")
  sound.play()

  ran_num = randrange(0, (len(fruits)))
  jumbled_rand_word = fruits[ran_num]
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
  if user_word == fruits[ran_num]:
      crt_ans = mixer.Sound("Audio/Correct_Answer.mp3")
      crt_ans.play()

      points += 5
      score.configure(text="Score:- " + str(points))

      time_taken = time.time() - start_time
      time_taken = int(time_taken)
      time_show.configure(text="Time : " + str(time_taken) + " Sec")
      messagebox.showinfo('Correct', "Correct Answer.. Keep it Up!")

      ran_num = randrange(0, (len(fruits)))
      jumbled_rand_word = fruits[ran_num]
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
      hint_window.overrideredirect(True)
      hint_window.geometry("400x400+930+290")
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
def get_summary():
   raw_text = str(entry.get('1.0',tk.END))
   final_text = text_summarizer(raw_text)
   print(final_text)
   result = '\nSummary:{}'.format(final_text)
   tab1_display.insert(tk.END,result)


# Clear entry widget
def clear_text():
   entry.delete('1.0',END)


def clear_display_result():
   tab1_display.delete('1.0',END)


# Clear Text  with position 1.0
def clear_text_file():
   displayed_file.delete('1.0',END)


# Clear Result of Functions
def clear_text_result():
   tab2_display_text.delete('1.0',END)


# Clear For URL
def clear_url_entry():
   url_entry.delete(0,END)


def clear_url_display():
   tab3_display_text.delete('1.0',END)


def clear_compare_display_result():
   tab1_display.delete('1.0',END)


# Functions for TAB 2 FILE PROCESSER
# Open File to Read and Process
def openfiles():
   file1 = tkinter.filedialog.askopenfilename(filetypes=(("Text Files",".txt"),("All files","*")))
   read_text = open(file1).read()
   displayed_file.insert(tk.END,read_text)


def get_file_summary():
   raw_text = displayed_file.get('1.0',tk.END)
   final_text = text_summarizer(raw_text)
   result = '\nSummary:{}'.format(final_text)
   tab2_display_text.insert(tk.END,result)


# Fetch Text From Url
def get_text():
   raw_text = str(url_entry.get())
   page = urlopen(raw_text)
   soup = BeautifulSoup(page)
   fetched_text = ' '.join(map(lambda p:p.text,soup.find_all('p')))
   url_display.insert(tk.END,fetched_text)


def get_url_summary():
   raw_text = url_display.get('1.0',tk.END)
   final_text = text_summarizer(raw_text)
   result = '\nSummary:{}'.format(final_text)
   tab3_display_text.insert(tk.END,result)


def upload_file():
   reset()
   global prediction_index
   img_label.config(text="")
   l2.config(text="Prediction")
   f_types = [('Image Files', '*.jpg *.png')]
   file_path = filedialog.askopenfilename()

   if file_path:
      imag = cv2.imread(file_path)
      img_from_ar = Image.fromarray(cv2.cvtColor(imag, cv2.COLOR_BGR2RGB))
      resized_image = img_from_ar.resize((50, 50))
      test_image = np.expand_dims(resized_image, axis=0)
      result = model.predict(test_image)

      prediction_index = np.argmax(result)
      prediction = labels[prediction_index]
      l2.config(text=f"Prediction: {prediction}")

      img = Image.open(file_path)
      img = img.resize((200, 200))
      img = ImageTk.PhotoImage(img)
      img_label.config(image=img)
      img_label.image = img

   desc()


def open_camera():
   reset()
   global prediction_index
   cap = cv2.VideoCapture(0)  # 0 represents the default camera index

   if not cap.isOpened():
      messagebox.showerror("Error", "Could not open camera.")
      return

   ret, frame = cap.read()
   if ret:
      img_from_ar = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
      resized_image = img_from_ar.resize((50, 50))
      test_image = np.expand_dims(resized_image, axis=0)
      result = model.predict(test_image)

      prediction_index = np.argmax(result)
      prediction = labels[prediction_index]
      l2.config(text=f"Prediction: {prediction}")

      img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
      img = img.resize((200, 200))
      img = ImageTk.PhotoImage(img)
      img_label.config(image=img)
      img_label.image = img
   cap.release()

   desc()

def say():
   prediction = labels[prediction_index]
   engine = pyttsx3.init()
   engine.say(prediction)
   engine.setProperty('rate', 150)
   voices = engine.getProperty('voices')
   engine.setProperty('voice', voices[1].id)

   engine.runAndWait()


def spell():
   prediction = labels[prediction_index]
   engine = pyttsx3.init()
   ch = list(prediction)
   for c in ch:
      if c.isalpha():  # Speak only alphabetic characters
         engine.say(c.upper())  # Use upper case for better pronunciation
         engine.setProperty('rate', 150)
         engine.runAndWait()

   engine.say(prediction)
   engine.setProperty('rate', 150)
   voices = engine.getProperty('voices')
   engine.setProperty('voice', voices[1].id)

   engine.runAndWait()


def reset():
   l2.config(text="Prediction")
   img_label.config(image='')
   display.delete('1.0',END)
   tab1_display_text.delete('1.0', END)


def desc():
   str1="https://en.wikipedia.org/wiki/"
   prediction = labels[prediction_index]
   raw_text = str(str1+prediction)
   print(raw_text)
   page = urlopen(raw_text)
   soup = BeautifulSoup(page)
   fetched_text = ' '.join(map(lambda p:p.text,soup.find_all('p')))
   display.insert(tk.END,fetched_text)


def get_summary1():
   raw_text = display.get('1.0',tk.END)
   final_text = text_summarizer(raw_text)
   result = '\nSummary:{}'.format(final_text)
   tab1_display_text.insert(tk.END,result)


def sayoutloud():
   a=tab1_display_text.get('1.0',tk.END)
   engine = pyttsx3.init()
   engine.say(a)
   engine.setProperty('rate', 150)
   voices = engine.getProperty('voices')
   engine.setProperty('voice', voices[0].id)

   engine.runAndWait()

# Object Detection
button1=Button(tab1,text="Upload images",command=upload_file, width=12,bg='#03A9F4',fg='#fff')
button1.grid(row=1,column=0,padx=10,pady=10)

button2=Button(tab1,text="Open camera",command=open_camera, width=12,bg='#ced',fg='#fff')
button2.grid(row=1,column=1,padx=10,pady=10)

button3=Button(tab1,text="Reset",command=reset, width=12,bg='#03A9F4',fg='#fff')
button3.grid(row=1,column=2,padx=10,pady=10)

button4=Button(tab1,text="Say",command=say, width=12,bg='#03A9F4',fg='#fff')
button4.grid(row=5,column=0,padx=10,pady=10)

button5=Button(tab1,text="Spell",command=spell, width=12,bg='#03A9F4',fg='#fff')
button5.grid(row=5,column=1,padx=10,pady=10)

l2=Label(tab1,text="Prediction:")
l2.grid(row=2,column=0)

img_label = Label(tab1,text="")
img_label.grid(row=2,column=1)

l1=Label(tab1,text="Description")
l1.grid(row=1,column=3)

display = ScrolledText(tab1,height=10)
display.grid(row=2,column=3, columnspan=3,padx=5,pady=5)

l3=Label(tab1,text="Summary")
l3.grid(row=4,column=3)

tab1_display_text = ScrolledText(tab1,height=10)
tab1_display_text.grid(row=5,column=3, columnspan=3,padx=5,pady=5)

button6=Button(tab1,text="Summarize",command=get_summary1, width=12,bg='#03A9F4',fg='#fff')
button6.grid(row=4,column=4,padx=10,pady=10)

button7=Button(tab1,text="Say summary out loud",command=sayoutloud, width=16,bg='#03A9F4',fg='#fff')
button7.grid(row=9,column=4,padx=10,pady=10)

#Text summarization
l1=Label(tab2,text="Enter Text To Summarize")
l1.grid(row=1,column=0)

entry=Text(tab2,height=10)
entry.grid(row=2,column=0,columnspan=2,padx=5,pady=5)

# BUTTONS
button1=Button(tab2,text="Reset",command=clear_text, width=12,bg='#03A9F4',fg='#fff')
button1.grid(row=4,column=0,padx=10,pady=10)

button2=Button(tab2,text="Summarize",command=get_summary, width=12,bg='#ced',fg='#fff')
button2.grid(row=4,column=1,padx=10,pady=10)

button3=Button(tab2,text="Clear Result", command=clear_display_result,width=12,bg='#03A9F4',fg='#fff')
button3.grid(row=5,column=0,padx=10,pady=10)

button4=Button(tab2,text="Main Points", width=12,bg='#03A9F4',fg='#fff')
button4.grid(row=5,column=1,padx=10,pady=10)

# Display Screen For Result
tab1_display = Text(tab2)
tab1_display.grid(row=7,column=0, columnspan=3,padx=5,pady=5)


#FILE PROCESSING TAB
l1=Label(tab3,text="Open File To Summarize")
l1.grid(row=1,column=1)

displayed_file = ScrolledText(tab3,height=7)# Initial was Text(tab2)
displayed_file.grid(row=2,column=0, columnspan=3,padx=5,pady=3)

# BUTTONS FOR SECOND TAB/FILE READING TAB
b0=Button(tab3,text="Open File", width=12,command=openfiles,bg='#c5cae9')
b0.grid(row=3,column=0,padx=10,pady=10)

b1=Button(tab3,text="Reset ", width=12,command=clear_text_file,bg="#b9f6ca")
b1.grid(row=3,column=1,padx=10,pady=10)

b2=Button(tab3,text="Summarize", width=12,command=get_file_summary,bg='blue',fg='#fff')
b2.grid(row=3,column=2,padx=10,pady=10)

b3=Button(tab3,text="Clear Result", width=12,command=clear_text_result)
b3.grid(row=5,column=1,padx=10,pady=10)

b4=Button(tab3,text="Close", width=12,command=window.destroy)
b4.grid(row=5,column=2,padx=10,pady=10)

# Display Screen
# tab2_display_text = Text(tab2)
tab2_display_text = ScrolledText(tab3,height=10)
tab2_display_text.grid(row=7,column=0, columnspan=3,padx=5,pady=5)

# Allows you to edit
tab2_display_text.config(state=NORMAL)


# URL TAB
l1=Label(tab4,text="Enter URL To Summarize")
l1.grid(row=1,column=0)

raw_entry=StringVar()
url_entry=Entry(tab4,textvariable=raw_entry,width=50)
url_entry.grid(row=1,column=1)

# BUTTONS
button1=Button(tab4,text="Reset",command=clear_url_entry, width=12,bg='#03A9F4',fg='#fff')
button1.grid(row=4,column=0,padx=10,pady=10)

button2=Button(tab4,text="Get Text",command=get_text, width=12,bg='#03A9F4',fg='#fff')
button2.grid(row=4,column=1,padx=10,pady=10)

button3=Button(tab4,text="Clear Result", command=clear_url_display,width=12,bg='#03A9F4',fg='#fff')
button3.grid(row=5,column=0,padx=10,pady=10)

button4=Button(tab4,text="Summarize",command=get_url_summary, width=12,bg='#03A9F4',fg='#fff')
button4.grid(row=5,column=1,padx=10,pady=10)

# Display Screen For Result
url_display = ScrolledText(tab4,height=10)
url_display.grid(row=7,column=0, columnspan=3,padx=5,pady=5)


tab3_display_text = ScrolledText(tab4,height=10)
tab3_display_text.grid(row=10,column=0, columnspan=3,padx=5,pady=5)


# to show time taken
time_show = Label(tab5,text="Time: ", fg="black", font="Cambria 12 italic")
time_show.grid(row=1,column=0)

# to show score
score = Label(tab5,text="Score:- 0", fg="black", font="Cambria 12 italic")
score.grid(row=1,column=8)

word = Label(tab5,text=words_shuffled, fg="black", font="Cambria  20 bold")
word.grid(row=2,column=4)

get_input = Entry(tab5,font="none 26 bold", borderwidth=10, justify='center')
get_input.grid(row=3,column=4)


submit_btn = Button(tab5,text="SUBMIT",width=20,height=3,bg='#03A9F4',justify='center', command=lambda: check())
submit_btn.grid(row=4,column=4,padx=10,pady=10)


change_btn = Button(tab5,text="CHANGE",width=20,height=3,bg='#03A9F4',justify='center', command=lambda: change())
change_btn.grid(row=5,column=4,padx=10,pady=10)


hint_btn = Button(tab5,text="HINT",width=20,height=3,bg='#03A9F4',justify='center', command=lambda: show_hint())
hint_btn.grid(row=6,column=4,padx=10,pady=10)


ans_btn = Button(tab5,text="Answer",width=20,height=3,bg='#03A9F4', command=lambda: show_answer())
ans_btn.grid(row=7,column=4,padx=10,pady=10)
ans_btn.configure(state="disabled")

ans_lab = Label(tab5,text="Answer: ", fg="black", font="Cambria 16 italic")
ans_lab.grid(row=8,column=4)

obj=LabelFrame(tab5,text="Hint Window",font=20,bd=2,width=500,height=500,relief=GROOVE)
obj.place(x=600,y=50)
window.mainloop()
