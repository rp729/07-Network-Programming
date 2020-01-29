from netconnect import *
from gui import *

if __name__ == '__main__':
    root = tk.Tk()
    my_gui = GUI(root)
    root.mainloop()

'''if __name__ == '__main__':
    host = input("Enter ip :")
    port = input(("Enter port :"))
    connect = NetConnect(host,port)
    connect.client()'''