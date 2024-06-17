import tkinter as tk
import customtkinter as ctk
from tkdnd import TkinterDnD
import views 
from PIL import Image, ImageTk
import os
import socket
import sys
import threading
import xml.etree.ElementTree as et

import user_management
import pendrive_recognition
import signature
import communication
import verification

from communication_config import HOST, PORT_A, PORT_B, FILE_SIZE_LIMIT

class AppController(ctk.CTk, TkinterDnD.DnDWrapper):
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 500
    drive_name = None
    username = None
    latest_file_path = None
    port = None
    dest_port = None

    files = []
    signatures = []
    file_extensions = []

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

        self.latest_file_path = file_path

        self.show_frame(views.SignSuccess)

    
    def send_signed(self):
        file_path = self.latest_file_path
        xml_path = os.path.splitext(file_path)[0] + "_signature.xml"
        file_type = os.path.splitext(file_path)[1][1:]

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, self.dest_port))
            with open(file_path, 'rb') as f:
                with open(xml_path, 'rb') as xml:
                    data = f.read()
                    xml_data = xml.read()
                    if len(data) > FILE_SIZE_LIMIT or len(xml_data) > FILE_SIZE_LIMIT:
                        raise Exception('File too large')
                    file_size = communication.prepare_file_size(len(data))
                    xml_size = communication.prepare_file_size(len(xml_data))
                    if file_type == 'txt':
                        s.sendall(b't' + file_size.encode() + data + xml_size.encode() + xml_data)
                    else:
                        s.sendall(b'b' + file_size.encode() + data + xml_size.encode() + xml_data)
                    print("Package sent")

    
    def receive_file(self, conn):
        with conn:
            while True:
                data = conn.recv(FILE_SIZE_LIMIT)
                if not data:
                    break
                data_decoded = data.decode()
                if data_decoded[0] == 't':
                    filename = '.txt'
                else:
                    filename = ''
                limit_str = len(str(FILE_SIZE_LIMIT))
                iterator_start = 1
                iterator_end = limit_str
                file_size = int(data_decoded[iterator_start:iterator_end].strip())
                iterator_start = iterator_end + 1
                iterator_end = iterator_start + file_size
                file = data_decoded[iterator_start:iterator_end]
                print("File received")
                iterator_start = iterator_end
                iterator_end = iterator_start + limit_str
                xml_size = int(data_decoded[iterator_start:iterator_end].strip())
                iterator_start = iterator_end
                iterator_end = iterator_start + xml_size
                xml = data_decoded[iterator_start:iterator_end]
                self.files.append(file)
                self.signatures.append(xml)
                self.file_extensions.append(filename)
                print("Signature received")
                return
    
    
    def verify_signature(self):
        key_valid = False
        
        while not key_valid:
            key_path = ctk.filedialog.askopenfilename(initialdir="/", title="Select a public key file", filetypes=[("Public key", ".pem")])
            if os.path.isfile(key_path):
                key_valid = True

        self.show_frame(views.Listening)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, self.port))
            s.listen()
            print("Listening on port: ", self.port)
            while True:
                conn, addr = s.accept()
                print('Connected with: ', addr)
                receive_thread = threading.Thread(target=self.receive_file, args=(conn,))
                receive_thread.start()

                receive_thread.join()

                if len(self.files) > 0 and len(self.signatures) > 0:
                    break
            
        if verification.verify_signature(et.ElementTree(et.fromstring(self.signatures[0])), key_path, self.files[0].encode()):
            self.show_frame(views.SignatureVerified)
        else:
            self.show_frame(views.VerificationFailed)

        self.signatures = []
        self.files = []
        self.file_extensions = []

        
        

    def temp(self):
        pass
    
    def login(self, username, password):
        if user_management.login(username, password):
            self.username = username
            if username == 'user1':
                self.port = PORT_A
                self.dest_port = PORT_B
            else:
                self.port = PORT_B
                self.dest_port = PORT_A
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
                  views.Temp, views.InputPin, views.SignSuccess,
                  views.Listening, views.SignatureVerified, views.VerificationFailed):
            frame = F(master=self, controller=self)
            self.frames[F] = frame
        self.current_frame = self.frames[views.MainMenu]
        self.show_frame(views.MainMenu)