import tkinter as tk
import customtkinter as ctk
from tkdnd import TkinterDnD
import views 
from PIL import Image, ImageTk

import user_management

class AppController(ctk.CTk, TkinterDnD.DnDWrapper):
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 500

    def temp(self):
        pass
    
    def login(self, username, password):
        user_management.login(username, password)
    
    def register(self, username, password, name, surname):
        user_management.register(username, password, name, surname)
    
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

        ico = Image.open('./media/icon.png')
        photo = ImageTk.PhotoImage(ico)
        self.wm_iconphoto(False, photo)
        
        self.frames = {}
        self.file_path = None
        for F in (views.MainMenu, views.RegisterPage, views.LoginPage,
                  views.LoginSuccess, views.LoginFail,
                  views.RegisterSuccess, views.RegisterFail,
                  views.HomePage):
            frame = F(master=self, controller=self)
            self.frames[F] = frame
        self.current_frame = self.frames[views.MainMenu]
        self.show_frame(views.MainMenu)