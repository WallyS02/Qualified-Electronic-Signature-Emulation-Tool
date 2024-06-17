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
        
        login_button = ctk.CTkButton(master=self, text="Register", command=lambda: controller.register(username_entry.get(), password_entry.get(), name_entry.get(), surname_entry.get()))
        login_button.pack(pady=10, padx=20, expand=True)

        back_button = ctk.CTkButton(master=self, text="Back", command=lambda: controller.show_frame(MainMenu))
        back_button.pack(pady=10, padx=20, expand=True)

class LoginSuccess(ctk.CTkFrame):
    def __init__(self, master: any, controller, **kwargs):
        super().__init__(master, **kwargs)

        title = ctk.CTkLabel(master=self, text="Logged in successfully", font=("Didot", 26))
        title.pack(pady=5, padx=10, fill="both", expand=False)

        text = ctk.CTkLabel(master=self, text="You will be redirected shortly")
        text.pack(expand=False)

class LoginFail(ctk.CTkFrame):
    def __init__(self, master: any, controller, **kwargs):
        super().__init__(master, **kwargs)

        title = ctk.CTkLabel(master=self, text="Login failed", font=("Didot", 26))
        title.pack(pady=5, padx=10, fill="both", expand=False)

        back_button = ctk.CTkButton(master=self, text="Back", command=lambda: controller.show_frame(LoginPage))
        back_button.pack(pady=10, padx=20, expand=True)

class RegisterSuccess(ctk.CTkFrame):
    def __init__(self, master: any, controller, **kwargs):
        super().__init__(master, **kwargs)

        title = ctk.CTkLabel(master=self, text="Registered successfully", font=("Didot", 26))
        title.pack(pady=5, padx=10, fill="both", expand=False)

        text = ctk.CTkLabel(master=self, text="You can now log in")
        text.pack(expand=False)

class RegisterFail(ctk.CTkFrame):
    def __init__(self, master: any, controller, **kwargs):
        super().__init__(master, **kwargs)

        title = ctk.CTkLabel(master=self, text="Could not register", font=("Didot", 26))
        title.pack(pady=5, padx=10, fill="both", expand=False)

        text = ctk.CTkLabel(master=self, text="Username already taken")
        text.pack(expand=False)

        back_button = ctk.CTkButton(master=self, text="Back", command=lambda: controller.show_frame(RegisterPage))
        back_button.pack(pady=10, padx=20, expand=True)

class HomePage(ctk.CTkFrame):
    def __init__(self, master: any, controller, **kwargs):
        super().__init__(master, **kwargs)

        title = ctk.CTkLabel(master=self, text="App main menu", font=("Didot", 26))
        title.pack(pady=5, padx=10, fill="both", expand=False)

        box = ctk.CTkFrame(master=self)
        box.pack(expand=True)
        
        sign_button = ctk.CTkButton(master=box, text="Sign a file", command=lambda: controller.sign_file())
        sign_button.pack(pady=10, padx=20)

        verify_button = ctk.CTkButton(master=box, text="Verify signature", command=lambda: controller.verify_signature())
        verify_button.pack(pady=10, padx=20)

        rsa_encrypt_button = ctk.CTkButton(master=box, text="RSA encrypt", command=lambda: controller.rsa_encrypt())
        rsa_encrypt_button.pack(pady=10, padx=20)

        rsa_decrypt_button = ctk.CTkButton(master=box, text="RSA decrypt", command=lambda: controller.show_frame(RSADecryptInputPin))
        rsa_decrypt_button.pack(pady=10, padx=20)

        aes_encrypt_button = ctk.CTkButton(master=box, text="AES encrypt", command=lambda: controller.show_frame(AESEncryptInputPin))
        aes_encrypt_button.pack(pady=10, padx=20)

        aes_decrypt_button = ctk.CTkButton(master=box, text="AES decrypt", command=lambda: controller.show_frame(AESDecryptInputPin))
        aes_decrypt_button.pack(pady=10, padx=20)
        
        back_button = ctk.CTkButton(master=box, text="Log out", command=lambda: controller.show_frame(MainMenu))
        back_button.pack(pady=10, padx=20)

class InsertPendrive(ctk.CTkFrame):
    def __init__(self, master: any, controller, **kwargs):
        super().__init__(master, **kwargs)

        title = ctk.CTkLabel(master=self, text="Please insert a pendrive", font=("Didot", 26))
        title.pack(pady=5, padx=10, fill="both", expand=False)

        text = ctk.CTkLabel(master=self, text="Insert a pendrive containing your private key.")
        text.pack(expand=False)

        #back_button = ctk.CTkButton(master=self, text="Cancel", command=lambda: controller.show_frame(HomePage))
        #back_button.pack(pady=10, padx=20)

class InputPin(ctk.CTkFrame):
    def __init__(self, master: any, controller, **kwargs):
        super().__init__(master, **kwargs)

        title = ctk.CTkLabel(master=self, text="Input user's PIN", font=("Didot", 26))
        title.pack(pady=5, padx=10, fill="both", expand=False)

        box = ctk.CTkFrame(master=self)
        box.pack(expand=True)

        pin_label = ctk.CTkLabel(master=box, text="PIN:")
        pin_label.pack(expand=False)
        
        pin_entry = ctk.CTkEntry(master=box, width=400, height=50, justify='center', show="*")
        pin_entry.pack(expand=False)

        ok_button = ctk.CTkButton(master=box, text="Confirm", command=lambda: controller.save_signed(pin_entry.get()))
        ok_button.pack(pady=10, padx=20)

        back_button = ctk.CTkButton(master=self, text="Cancel", command=lambda: controller.show_frame(HomePage))
        back_button.pack(pady=10, padx=20)


class RSADecryptInputPin(ctk.CTkFrame):
    def __init__(self, master: any, controller, **kwargs):
        super().__init__(master, **kwargs)

        title = ctk.CTkLabel(master=self, text="Input user's PIN", font=("Didot", 26))
        title.pack(pady=5, padx=10, fill="both", expand=False)

        box = ctk.CTkFrame(master=self)
        box.pack(expand=True)

        pin_label = ctk.CTkLabel(master=box, text="PIN:")
        pin_label.pack(expand=False)
        
        pin_entry = ctk.CTkEntry(master=box, width=400, height=50, justify='center', show="*")
        pin_entry.pack(expand=False)

        ok_button = ctk.CTkButton(master=box, text="Confirm", command=lambda: controller.rsa_decrypt(pin_entry.get()))
        ok_button.pack(pady=10, padx=20)

        back_button = ctk.CTkButton(master=self, text="Cancel", command=lambda: controller.show_frame(HomePage))
        back_button.pack(pady=10, padx=20)

class AESEncryptInputPin(ctk.CTkFrame):
    def __init__(self, master: any, controller, **kwargs):
        super().__init__(master, **kwargs)

        title = ctk.CTkLabel(master=self, text="Input user's PIN", font=("Didot", 26))
        title.pack(pady=5, padx=10, fill="both", expand=False)

        box = ctk.CTkFrame(master=self)
        box.pack(expand=True)

        pin_label = ctk.CTkLabel(master=box, text="PIN:")
        pin_label.pack(expand=False)
        
        pin_entry = ctk.CTkEntry(master=box, width=400, height=50, justify='center', show="*")
        pin_entry.pack(expand=False)

        ok_button = ctk.CTkButton(master=box, text="Confirm", command=lambda: controller.aes_encrypt(pin_entry.get()))
        ok_button.pack(pady=10, padx=20)

        back_button = ctk.CTkButton(master=self, text="Cancel", command=lambda: controller.show_frame(HomePage))
        back_button.pack(pady=10, padx=20)

class AESDecryptInputPin(ctk.CTkFrame):
    def __init__(self, master: any, controller, **kwargs):
        super().__init__(master, **kwargs)

        title = ctk.CTkLabel(master=self, text="Input user's PIN", font=("Didot", 26))
        title.pack(pady=5, padx=10, fill="both", expand=False)

        box = ctk.CTkFrame(master=self)
        box.pack(expand=True)

        pin_label = ctk.CTkLabel(master=box, text="PIN:")
        pin_label.pack(expand=False)
        
        pin_entry = ctk.CTkEntry(master=box, width=400, height=50, justify='center', show="*")
        pin_entry.pack(expand=False)

        ok_button = ctk.CTkButton(master=box, text="Confirm", command=lambda: controller.aes_decrypt(pin_entry.get()))
        ok_button.pack(pady=10, padx=20)

        back_button = ctk.CTkButton(master=self, text="Cancel", command=lambda: controller.show_frame(HomePage))
        back_button.pack(pady=10, padx=20)


class SignSuccess(ctk.CTkFrame):
    def __init__(self, master: any, controller, **kwargs):
        super().__init__(master, **kwargs)

        title = ctk.CTkLabel(master=self, text="Successfully signed", font=("Didot", 26))
        title.pack(pady=5, padx=10, fill="both", expand=False)

        text = ctk.CTkLabel(master=self, text="Signed file has been saved in the same directory")
        text.pack(expand=False)

        box = ctk.CTkFrame(master=self)
        box.pack(expand=True)

        send_button = ctk.CTkButton(master=box, text="Send to another user", command=lambda: controller.send_signed())
        send_button.pack(pady=10, padx=20)

        back_button = ctk.CTkButton(master=self, text="Home", command=lambda: controller.show_frame(HomePage))
        back_button.pack(pady=10, padx=20)

class Listening(ctk.CTkFrame):
    def __init__(self, master: any, controller, **kwargs):
        super().__init__(master, **kwargs)

        title = ctk.CTkLabel(master=self, text="Listening for files...", font=("Didot", 26))
        title.pack(pady=5, padx=10, fill="both", expand=False)

        text = ctk.CTkLabel(master=self, text="Waiting to receive a file")
        text.pack(expand=False)

class SignatureVerified(ctk.CTkFrame):
    def __init__(self, master: any, controller, **kwargs):
        super().__init__(master, **kwargs)

        title = ctk.CTkLabel(master=self, text="Signature verified", font=("Didot", 26))
        title.pack(pady=5, padx=10, fill="both", expand=False)

        text = ctk.CTkLabel(master=self, text="Received file is signed correctly")
        text.pack(expand=False)

        back_button = ctk.CTkButton(master=self, text="Home", command=lambda: controller.show_frame(HomePage))
        back_button.pack(pady=10, padx=20)



class VerificationFailed(ctk.CTkFrame):
    def __init__(self, master: any, controller, **kwargs):
        super().__init__(master, **kwargs)

        title = ctk.CTkLabel(master=self, text="Verification failed", font=("Didot", 26))
        title.pack(pady=5, padx=10, fill="both", expand=False)

        text = ctk.CTkLabel(master=self, text="Signature doesn't match file and/or the public key")
        text.pack(expand=False)

        back_button = ctk.CTkButton(master=self, text="Home", command=lambda: controller.show_frame(HomePage))
        back_button.pack(pady=10, padx=20)

class RSAEncryptSuccess(ctk.CTkFrame):
    def __init__(self, master: any, controller, **kwargs):
        super().__init__(master, **kwargs)

        title = ctk.CTkLabel(master=self, text="File has been encrypted", font=("Didot", 26))
        title.pack(pady=5, padx=10, fill="both", expand=False)

        text = ctk.CTkLabel(master=self, text="Use the same key if you wish to decrypt it.")
        text.pack(expand=False)


class RSADecryptSuccess(ctk.CTkFrame):
    def __init__(self, master: any, controller, **kwargs):
        super().__init__(master, **kwargs)

        title = ctk.CTkLabel(master=self, text="File has been decrypted", font=("Didot", 26))
        title.pack(pady=5, padx=10, fill="both", expand=False)

        text = ctk.CTkLabel(master=self, text="Your file has been saved to the same location.")
        text.pack(expand=False)

class AESEncryptSuccess(ctk.CTkFrame):
    def __init__(self, master: any, controller, **kwargs):
        super().__init__(master, **kwargs)

        title = ctk.CTkLabel(master=self, text="File has been encrypted", font=("Didot", 26))
        title.pack(pady=5, padx=10, fill="both", expand=False)

        text = ctk.CTkLabel(master=self, text="Use the same key if you wish to decrypt it.")
        text.pack(expand=False)


class AESDecryptSuccess(ctk.CTkFrame):
    def __init__(self, master: any, controller, **kwargs):
        super().__init__(master, **kwargs)

        title = ctk.CTkLabel(master=self, text="File has been decrypted", font=("Didot", 26))
        title.pack(pady=5, padx=10, fill="both", expand=False)

        text = ctk.CTkLabel(master=self, text="Your file has been saved to the same location.")
        text.pack(expand=False)

class Temp(ctk.CTkFrame):
    def __init__(self, master: any, controller, **kwargs):
        super().__init__(master, **kwargs)

        title = ctk.CTkLabel(master=self, text="Temp", font=("Didot", 26))
        title.pack(pady=5, padx=10, fill="both", expand=False)

        text = ctk.CTkLabel(master=self, text="Temp")
        text.pack(expand=False)