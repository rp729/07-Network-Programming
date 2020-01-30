from tkinter import ttk
import tkinter as tk
from netconnect import *
import glob
import datetime
import socket
import sys
import threading
import time
import client_server
from subprocess import call

class GUI:
    def __init__(self,master):
        self.__master = master
        self.__master.title("Client")
        self.__master.geometry("800x600")


        '''Labels'''
        self.__label1 = tk.Label(self.__master,text="Enter IP Address:",font=('Arial',18))
        self.__label2 = tk.Label(self.__master, text="Enter Port: (4000-6552)", font=('Arial', 18))
        self.__label3 = tk.Label(self.__master,text="Returned Message: ",font=('Arial',18))
        self.__label4 = tk.Label(self.__master, text="OPTIONS", font=('Arial', 18))

        '''Entry'''
        self.__entry1 = tk.Entry(bd=5)
        self.__entry2 = tk.Entry(bd=5)

        '''Buttons'''
        self.__button1 = tk.Button(text="Connect",command=self.connect,bd=5)
        self.__button2 = tk.Button(text="Export to Text File", command=self.export, bd=5)
        self.__button3 = tk.Button(text="RUN", command=self.run, bd=5)

        '''Text Field'''
        self.__text1 = tk.Text(master=self.__master,height=10,width=90,bd=5)

        '''Combo Box'''
        self.__cb1 = ttk.Combobox(self.__master,values=self.combo_box_function())
        self.__cb1.set('--Select--')

        '''Pack Order'''
        self.__label1.pack()
        self.__entry1.pack(ipadx=100, ipady=5)
        self.__label2.pack()
        self.__entry2.pack(ipadx=100, ipady=5)
        self.__button1.pack()
        self.__label3.pack()
        self.__text1.pack()
        self.__button2.pack()
        self.__label4.pack()
        self.__cb1.pack()
        self.__button3.pack()


    def combo_box_function(self):
        toolkit = glob.glob('toolkit/*')
        files = []
        for i in toolkit:
            files.append(i[8:])
        return files

    def get_ip(self):
        string = str(self.__entry1.get())
        return string

    def get_port(self):
        string = str(self.__entry2.get())
        return string

    '''BUTTON FUNCTIONS'''
    def connect(self):
        host = self.get_ip()
        port = self.get_port()
        connect = NetConnect(host, port)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        t1 = threading.Thread(target=client_server)
        t1.start()
        '''#connect.client()
        #connect.client_server()
        t1 = threading.Thread(target=connect.client)
        t2 = threading.Thread(target=connect.client_server)
        t1.daemon = True
        t2.daemon = True
        t1.start()
        t2.start()'''

        orig_stdout = sys.stdout
        file = open("../UDP_Connection/test.txt", "w")
        sys.stdout = file
        connect.send_message(s, "CONNECTED".encode(), host, int(port))
        time.sleep(0.1)
        file.close()
        sys.stdout = orig_stdout
        file = open('../UDP_Connection/test.txt')
        file_read = file.read()
        self.__text1.insert(tk.END, file_read)


    def export(self):
        name = f'{datetime.datetime.now()}.txt'
        file = open(name,'w')
        text = open('../UDP_Connection/text.txt')
        file.write(text.read())
        file.close()

    def run(self):
        host = self.get_ip()
        port = self.get_port()
        connect = NetConnect(host, port)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #connect.client()
        t1 = threading.Thread(target=connect.client)
        t2 = threading.Thread(target=connect.client_server)
        t1.daemon = True
        t2.daemon = True
        t1.start()
        t2.start()

        '''message = self.__cb1.get().encode()
        name = self.get_ip()
        port = int(self.get_port())
        connect = NetConnect(name,port)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        connect.send_message(sock, message, name, port)'''

        message = self.__cb1.get()
        orig_stdout = sys.stdout
        file = open("../UDP_Connection/text.txt", "w")
        sys.stdout = file
        connect.send_message(s, message.encode(), host, int(port))
        time.sleep(0.1)
        file.close()
        sys.stdout = orig_stdout
        file = open('../UDP_Connection/text.txt')
        file_read = file.read()
        self.__text1.insert(tk.END, file_read)



    def receive_message(self):
        ephemeral = int(f'{self.get_port()}1')
        host = 'localhost'
        port = ephemeral
        connect = NetConnect(host, port)

