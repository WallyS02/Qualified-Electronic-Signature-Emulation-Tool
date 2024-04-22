from PIL import Image, ImageTk
import tkinter as tk

import customtkinter as ctk
from tkdnd import DND_FILES

class MainMenu(ctk.CTkFrame):
    def __init__(self, master: any, controller, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(corner_radius=10)

        title = ctk.CTkLabel(master=self, text="Welcome to the app", font=("Didot", 26))
        title.pack(pady=5, padx=10, fill="both", expand=False)

        box = ctk.CTkFrame(master=self)
        box.pack(expand=True)
        
        login_button = ctk.CTkButton(master=box, text="Login", command=lambda: controller.show_frame(LoginPage))
        login_button.pack(pady=10, padx=20)

        register_button = ctk.CTkButton(master=box, text="Register", command=lambda: controller.show_frame(RegisterPage))
        register_button.pack(pady=10, padx=20)

class LoginPage(ctk.CTkFrame):
    def __init__(self, master: any, controller, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(corner_radius=10)

        title = ctk.CTkLabel(master=self, text="Please log in", font=("Didot", 26))
        title.pack(pady=5, padx=10, fill="both", expand=False)

        box = ctk.CTkFrame(master=self)
        box.pack(expand=True)

        username_label = ctk.CTkLabel(master=box, text="Username:")
        username_label.pack(expand=False)
        
        username_entry = ctk.CTkEntry(master=box, width=400, height=50, justify='center')
        username_entry.pack(expand=False)
        
        password_label = ctk.CTkLabel(master=box, text="Password:")
        password_label.pack(expand=False)
        
        password_entry = ctk.CTkEntry(master=box, width=400, height=50, justify='center', show="*")
        password_entry.pack(expand=False)
        
        login_button = ctk.CTkButton(master=self, text="Login", command=lambda: controller.login(username_entry.get(), password_entry.get()))
        login_button.pack(pady=10, padx=20, expand=True)

        back_button = ctk.CTkButton(master=self, text="Back", command=lambda: controller.show_frame(MainMenu))
        back_button.pack(pady=10, padx=20, expand=True)

class RegisterPage(ctk.CTkFrame):
    def __init__(self, master: any, controller, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(corner_radius=10)

        title = ctk.CTkLabel(master=self, text="Registering a new user", font=("Didot", 26))
        title.pack(pady=5, padx=10, fill="both", expand=False)

        box = ctk.CTkFrame(master=self)
        box.pack(expand=True)

        name_label = ctk.CTkLabel(master=box, text="Name:")
        name_label.pack(expand=False)
        
        name_entry = ctk.CTkEntry(master=box, width=400, height=50, justify='center')
        name_entry.pack(expand=False)
        
        surname_label = ctk.CTkLabel(master=box, text="Surname:")
        surname_label.pack(expand=False)
        
        surname_entry = ctk.CTkEntry(master=box, width=400, height=50, justify='center')
        surname_entry.pack(expand=False)
        
        username_label = ctk.CTkLabel(master=box, text="Username:")
        username_label.pack(expand=False)
        
        username_entry = ctk.CTkEntry(master=box, width=400, height=50, justify='center')
        username_entry.pack(expand=False)
        
        password_label = ctk.CTkLabel(master=box, text="Password:")
        password_label.pack(expand=False)
        
        password_entry = ctk.CTkEntry(master=box, width=400, height=50, justify='center', show="*")
        password_entry.pack(expand=False)
        
        login_button = ctk.CTkButton(master=self, text="Login", command=lambda: controller.register(username_entry.get(), password_entry.get(), name_entry.get(), surname_entry.get()))
        login_button.pack(pady=10, padx=20, expand=True)

        back_button = ctk.CTkButton(master=self, text="Back", command=lambda: controller.show_frame(MainMenu))
        back_button.pack(pady=10, padx=20, expand=True)

class LoginSuccess(ctk.CTkFrame):
    def __init__(self, master: any, controller, **kwargs):
        super().__init__(master, **kwargs)

class LoginFail(ctk.CTkFrame):
    def __init__(self, master: any, controller, **kwargs):
        super().__init__(master, **kwargs)

class RegisterSuccess(ctk.CTkFrame):
    def __init__(self, master: any, controller, **kwargs):
        super().__init__(master, **kwargs)

class RegisterFail(ctk.CTkFrame):
    def __init__(self, master: any, controller, **kwargs):
        super().__init__(master, **kwargs)

class HomePage(ctk.CTkFrame):
    def __init__(self, master: any, controller, **kwargs):
        super().__init__(master, **kwargs)