import youtube_dl
import tkinter as tk

#This file is old! Please see youtube2.py for latest version of this project

class YouTube:
    def __init__(self,master):
        self.__master = master
        self.__master.title("YouTube Downloader")
        self.__master.geometry("800x400")

        '''Labels'''
        self.__label1 = tk.Label(self.__master,text="Enter YouTube URL:",font=('Arial',10))
        self.__label1.grid(column=0,row=0)

        '''Buttons'''
        self.__button1 = tk.Button(text="DOWNLOAD",command=self.download_vid)
        self.__button1.grid(column=0,row=2)

        '''Entry'''
        self.entry1 = tk.Entry()
        self.entry1.grid(column=0,row=1)

    def download_vid(self):
        user_input = self.get_vid()
        yt_dict = {}
        with youtube_dl.YoutubeDL(yt_dict) as yt:
            yt.download([user_input])

    def get_vid(self):
        string = str(self.entry1.get())
        return string


root = tk.Tk()
my_gui = YouTube(root)
root.mainloop()
