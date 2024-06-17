import tkinter as tk
import customtkinter as ctk
from tkdnd import TkinterDnD
import views 
from PIL import Image, ImageTk
import os

import user_management
import pendrive_recognition
import signature

class AppController(ctk.CTk, TkinterDnD.DnDWrapper):
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 500
    drive_name = None
    username = None

    def sign_file(self):
        self.show_frame(views.InsertPendrive)
        self.drive_name = pendrive_recognition.detect_usb_insertion()
        self.show_frame(views.InputPin)

    def save_signed(self, pin):
        file_valid = False
        
        while not file_valid:
            file_path = ctk.filedialog.askopenfilename(initialdir="/", title="Pick a file to sign")
            if os.path.isfile(file_path):
                file_valid = True
        
        user_data = user_management.get_name_and_surname(self.username)

        private_key_path = os.path.join(self.drive_name, 'private_key')

        signature.create_xml_signature(file_path, user_data, private_key_path, pin)

        self.show_frame(views.SignSuccess)
        self.after(2000, lambda: self.show_frame(views.HomePage))

    def temp(self):
        pass
    
    def login(self, username, password):
        if user_management.login(username, password):
            self.username = username
            self.show_frame(views.LoginSuccess)
            self.after(2000, lambda: self.show_frame(views.HomePage))
        else:
            self.show_frame(views.LoginFail)
    
    def register(self, username, password, name, surname):
        answer = user_management.register(username, password, name, surname)

        if answer == 'Username is already taken':
            self.show_frame(views.RegisterFail)
        if answer == 'User registered successfully':
            self.show_frame(views.RegisterSuccess)
            self.after(2000, lambda: self.show_frame(views.MainMenu))
    
    def show_frame(self, cont):
        self.current_frame.pack_forget()
        self.current_frame = self.frames[cont]
        self.current_frame.pack(expand=True, fill="both")
        self.update_idletasks()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("blue")
        self.current_frame = None
        self.TkdndVersion = TkinterDnD._require(self)
        self.resizable(width=False, height=False)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.x_pos = (screen_width / 2) - (AppController.WINDOW_WIDTH / 2)
        self.y_pos = (screen_height / 2) - (AppController.WINDOW_HEIGHT / 2)
        self.geometry('%dx%d+%d+%d' % (AppController.WINDOW_WIDTH, AppController.WINDOW_HEIGHT, self.x_pos, self.y_pos))
        self.title("Electronic Signature Project")

        ico = Image.open('media/icon.png')
        photo = ImageTk.PhotoImage(ico)
        self.wm_iconphoto(False, photo)
        
        self.frames = {}
        self.file_path = None
        for F in (views.MainMenu, views.RegisterPage, views.LoginPage,
                  views.LoginSuccess, views.LoginFail,
                  views.RegisterSuccess, views.RegisterFail,
                  views.HomePage, views.InsertPendrive,
                  views.Temp, views.InputPin, views.SignSuccess):
            frame = F(master=self, controller=self)
            self.frames[F] = frame
        self.current_frame = self.frames[views.MainMenu]
        self.show_frame(views.MainMenu)