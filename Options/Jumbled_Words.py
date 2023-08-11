# importing packages
from tkinter import *
from PIL import Image, ImageTk


# function to start the Jumbled word game page
def start_third_page():
    def show_setting():
        from Setting import Setting                                             # to import Setting.py program
        Setting.setting()                                                       # to call the setting() from Setting.py

    def show_last_page():
        jumble_window.destroy()                                                 # to destroy jumble game window
        import Sec_page
        Sec_page.start_sec_page()                                               # to start the second page

    def start_jumble_game(args):
        jumble_window.destroy()                                                 # to destroy the jumble game window
        if args == 1:
            from Options import Animals                                         # to import Animals game page
            Animals.main()                                                      # to start the main() of Animals page
        elif args == 2:
            from Options import Birds_and_Insects                               # to import Birds and Insects game page
            Birds_and_Insects.main()                                            # to start the main()
        elif args == 3:
            from Options import Body_parts                                      # to import Body parts game page
            Body_parts.main()                                                   # to start the main()
        elif args == 4:
            from Options import Colours_and_Shapes                              # to import Colours_and_Shapes game page
            Colours_and_Shapes.main()                                           # to start the main()
        elif args == 5:
            from Options import Fruits                                          # to import Fruits game page
            Fruits.main()                                                       # to start the main()
        elif args == 6:
            from Options import Vegetables                                      # to import Vegetables game page
            Vegetables.main()                                                   # to start the main()
        elif args == 7:
            from Options import Vehicles                                        # to import Vehicles game page
            Vehicles.main()                                                     # to start the main()

    jumble_window = Tk()                                                        # creation of window
    jumble_window.title("Boot Brain \U0001F9E0-----Jumbled Words")              # to show window title
    jumble_window.configure(background="black")                                 # window background colour
    jumble_window.wm_iconbitmap('Pictures/logo.ico')                            # to show window icon
    jumble_window.geometry("1540x825+0+0")
    jumble_window.resizable(0, 0)                                               # to restrict user from resizing window

    # to set up background image
    jumble_img = Image.open("Pictures/Jumbled_words.jpg")
    jumble_photo = ImageTk.PhotoImage(jumble_img)
    back_image = Label(image=jumble_photo)
    back_image.pack()

    # to set up setting button image
    setting_img = Image.open("Pictures/setting.jpg")
    setting_photo = ImageTk.PhotoImage(setting_img)
    setting = Button(jumble_window, image=setting_photo, bg='black', relief="solid", command=lambda: show_setting())
    setting.place(x=1200, y=120)

    # to set up Animal button image
    animal_img = Image.open("Pictures/Animals.png")
    animal_photo = ImageTk.PhotoImage(animal_img)
    animal_btn = Button(jumble_window, image=animal_photo, bg="black", relief="solid",
                        command=lambda: start_jumble_game(1))
    animal_btn.place(x=710, y=170, anchor='center')

    # to set up Birds and Insects button image
    birds_img = Image.open("Pictures/Birds_and_Insects.png")
    birds_photo = ImageTk.PhotoImage(birds_img)
    birds_btn = Button(jumble_window, image=birds_photo, bg="black", relief="solid",
                       command=lambda: start_jumble_game(2))
    birds_btn.place(x=710, y=250, anchor='center')

    # to set up Body Parts button image
    body_img = Image.open("Pictures/Body_Parts.png")
    body_photo = ImageTk.PhotoImage(body_img)
    body_btn = Button(jumble_window, image=body_photo, bg="black", relief="solid",
                      command=lambda: start_jumble_game(3))
    body_btn.place(x=710, y=330, anchor='center')

    # to set up Colours and Shapes button image
    colours_img = Image.open("Pictures/Colours_Shapes.png")
    colours_photo = ImageTk.PhotoImage(colours_img)
    colours_btn = Button(jumble_window, image=colours_photo, bg="black", relief="solid",
                         command=lambda: start_jumble_game(4))
    colours_btn.place(x=710, y=410, anchor='center')

    # to set up Fruits button image
    fruits_img = Image.open("Pictures/Fruits.png")
    fruits_photo = ImageTk.PhotoImage(fruits_img)
    fruits_btn = Button(jumble_window, image=fruits_photo, bg="black", relief="solid",
                        command=lambda: start_jumble_game(5))
    fruits_btn.place(x=710, y=500, anchor='center')

    # to set up Vegetable button image
    vegetable_img = Image.open("Pictures/Vegetables.png")
    vegetable_photo = ImageTk.PhotoImage(vegetable_img)
    vegetable_btn = Button(jumble_window, image=vegetable_photo, bg="black", relief="solid",
                           command=lambda: start_jumble_game(6))
    vegetable_btn.place(x=710, y=580, anchor='center')

    # to set up Vehicles button image
    vehicles_img = Image.open("Pictures/Vehicles.png")
    vehicles_photo = ImageTk.PhotoImage(vehicles_img)
    vehicles_btn = Button(jumble_window, image=vehicles_photo, bg="black", relief="solid",
                          command=lambda: start_jumble_game(7))
    vehicles_btn.place(x=710, y=660, anchor='center')

    # to set up Back button image
    back_img = Image.open("Pictures/back.png")
    back_photo = ImageTk.PhotoImage(back_img)
    back_btn = Button(jumble_window, image=back_photo, bg='black', relief="solid",
                      command=lambda: show_last_page())
    back_btn.place(x=200, y=650)

    jumble_window.mainloop()                                               # to run the event loop
