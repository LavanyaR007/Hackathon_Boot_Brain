# importing packages
import os
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import pygame
import tensorflow as tf
import cv2
import numpy as np
from gtts import gTTS
from IPython.display import Audio, display
import io
from pygame import mixer



# to initialize mixer
pygame.init()

model = tf.keras.models.load_model(os.getcwd() + '\model.h5')


def main():
    # function to go back to last page
    def show_last_page():
        obj_window.destroy()
        import Sec_page
        Sec_page.start_sec_page()

    # function to show setting
    def show_setting():
        from Setting import Setting
        Setting.setting()

    def upload_file():
        f_types = [('Image Files', '*.jpg *.png')]
        file_path = filedialog.askopenfilename()
        if file_path:
            imag = cv2.imread(file_path)
            img_from_ar = Image.fromarray(cv2.cvtColor(imag, cv2.COLOR_BGR2RGB))
            resized_image = img_from_ar.resize((50, 50))
            test_image = np.expand_dims(resized_image, axis=0)
            result = model.predict(test_image)

            labels = ["Apple", "Banana", "Beetroot", "Cabbage", "Carrot", "Grapes", "Guva", "Mango", "Lady's Finger",
                      "Pumpkin"]
            prediction_index = np.argmax(result)
            prediction = labels[prediction_index]
            ans_lab.config(text=f"Prediction: {prediction}")

            img = Image.open(file_path)
            img = img.resize((200, 200))
            img = ImageTk.PhotoImage(img)
            image_label.config(image=img)
            image_label.image = img

            language = 'en'
            output = gTTS(text=prediction, lang=language, slow=False)

            # Save gTTS output to an in-memory buffer
            buffer = io.BytesIO()
            output.write_to_fp(buffer)
            buffer.seek(0)

            mixer.music.load(Audio(buffer.read()))
            mixer.music.play(-1)

            # Play the audio directly using IPython's Audio widget
            display(Audio(buffer.read(), autoplay=True))

    def open_camera():
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

            labels = ["Apple", "Banana", "Beetroot", "Cabbage", "Carrot", "Grapes", "Guava", "Mango", "Lady's Finger",
                      "Pumpkin"]
            prediction_index = np.argmax(result)
            prediction = labels[prediction_index]
            ans_lab.config(text=f"Prediction: {prediction}")

            img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            img = img.resize((200, 200))
            img = ImageTk.PhotoImage(img)
            image_label.config(image=img)
            image_label.image = img

        cap.release()

    obj_window = Tk()                                                         # creation of window
    obj_window.title("Boot Brain \U0001F9E0-----Jumbled Words~Object Detection")       # to show window title
    obj_window.configure(background="black")                                  # window background colour
    obj_window.wm_iconbitmap('Pictures/logo.ico')                             # to show window icon
    obj_window.geometry("1540x825+0+0")                                             # window size(width,height)
    obj_window.resizable(0, 0)                                                # to restrict user from resizing window

    # to set up background image
    fruits_img = Image.open("Pictures/Fruits_back.jpg")
    fruits_photo = ImageTk.PhotoImage(fruits_img)
    back_image = Label(image=fruits_photo)
    back_image.pack()

    # to set up setting button image
    setting_img = Image.open("Pictures/setting.jpg")
    setting_photo = ImageTk.PhotoImage(setting_img)
    setting = Button(image=setting_photo, bg='black', relief="solid", command=lambda: show_setting())
    setting.place(x=1450, y=5)

    word = Label(text="OBJECT DETECTION", bg="black", fg="white", font="Cambria  30 bold")
    word.place(x=1000, y=120)

    # to set up submit button
    u_img = Image.open("Pictures/upload.png")
    u_photo = ImageTk.PhotoImage(u_img)
    u_btn = Button(image=u_photo, bg="black", justify='center', relief="solid",command=lambda: upload_file())
    u_btn.place(x=1050, y=270)

    # to set up change word button
    c_img = Image.open("Pictures/camera.png")
    c_photo = ImageTk.PhotoImage(c_img)
    c_btn = Button(image=c_photo, bg="black", justify='center', relief="solid",command=lambda :open_camera())
    c_btn.place(x=1070, y=360)

    image_label = Label()
    image_label.place(x=1050,y=450)

    ans_lab = Label(text="Prediction: ", bg="#B45F06", fg="black", font="Cambria 16 italic")
    ans_lab.place(x=1050, y=650)

    # to set up Back button image
    back_img = Image.open("Pictures/back.png")
    back_photo = ImageTk.PhotoImage(back_img)
    back_btn = Button(image=back_photo, bg='black', relief="solid", command=lambda: show_last_page())
    back_btn.place(x=650, y=5)

    obj_window.mainloop()                                                          # to run the event loop
