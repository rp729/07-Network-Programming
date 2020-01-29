from tkinter import ttk
import tkinter as tk
from ascratch_fullduplex import *
import sys
import glob
import datetime

class GUI:
    def __init__(self,master):
        self.__master = master
        self.__master.title("Client")
        self.__master.geometry("800x600")


        '''Labels'''
        self.__label1 = tk.Label(self.__master,text="Enter IP Address:",font=('Arial',18))
        self.__label2 = tk.Label(self.__master, text="Enter Port:", font=('Arial', 18))
        self.__label3 = tk.Label(self.__master,text="Returned Message: ",font=('Arial',18))
        self.__label4 = tk.Label(self.__master, text="OPTIONS", font=('Arial', 18))

        '''Entry'''
        self.__entry1 = tk.Entry(bd=5)
        self.__entry2 = tk.Entry(bd=5)

        '''Buttons'''
        self.__button1 = tk.Button(text="Connect",command=self.connect,bd=5)
        self.__button2 = tk.Button(text="Export to Text File", command=self.export, bd=5)
        self.__button3 = tk.Button(text="RUN", command=self.run, bd=5)

        '''Label Field'''
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

    #NEEDS SUM STUFF
    def run(self):
        message = self.__cb1.get()
        sock = NetConnect.get_sock
        NetConnect.send_message(sock,message)

    def combo_box_function(self):
        toolkit = glob.glob('../UDP_Connection/toolkit/*')
        files = []
        for i in toolkit:
            files.append(i[8:])
        return files


    def packet_build(self):
        ip = self.get_ip()
        port = self.get_port()
        port = self.input_validation(port)
        pkt = NetConnect(ip,port)
        pkt.set_message = 'Connection Established'
        pkt.net_client()

    def get_ip(self):
        string = str(self.__entry1.get())
        return string

    def get_port(self):
        string = str(self.__entry2.get())
        return string

    def connect(self):
        file = open('text.txt', 'w')
        sys.stdout = file
        self.packet_build()
        sys.stdout = sys.__stdout__
        file.close()
        file = open('text.txt')
        file_read = file.read()
        self.__text1.insert(tk.END, file_read)

    def communicate(self):
        self.receive(pkt)
        self.send(pkt)

    def receive(self,sock):
        return sock.recv(1024).decode()

    def send(self,sock):
        new_message = input("Enter message: ")
        sock.send(new_message.encode())

    def input_validation(self,num):
        while str.isnumeric(num) == False:
            num = input("ERROR! Enter a number: ")
        return int(num)

    def export(self):
        name = f'{datetime.datetime.now()}.txt'
        file = open(name,'w')
        text = open('text.txt')
        file.write(text.read())
        file.close()