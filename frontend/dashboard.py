from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import frontend.workboard

class mainlibrary:
    def insert_pic(self):
        """
                        Function To Insert Picture
        """
        self.canvas = Canvas(self.root, width=2000, height=1000)
        self.canvas.pack()
        self.image = PhotoImage(file="narutoimg.png")
        self.canvas.create_image(0, 0, image=self.image, anchor=NW)
    def __init__(self, root):
        """
                        Function to configure root window
        """
        self.root = root
        self.root.title("Welcome To Sarga Anime CD Shop")
        self.root.geometry("900x680+0+0")
        self.insert_pic()
        self.b1 = Button(text="Add Anime CD",font="arial 20 bold", bg="#000000", fg="#ffffff", command=self.add_anime)
        self.b2 = Button(text="Add Anime CD Buyer", font="arial 20 bold", bg="#000000", fg="#ffffff",  command=self.add_cdbuyer)
        self.b3 = Button(text="Buy Or Rent Anime CD  ", font="arial 20 bold", bg="#000000", fg="#ffffff",  command=self.buycd)
        self.b4 = Button(text="Return Anime CD", font="arial 20 bold", bg="#000000", fg="#ffffff",  command=self.returncd)
        self.b5 = Button(text="Delete Anime CD", font="arial 20 bold", bg="#000000", fg="#ffffff",  command=self.deletecd)
        self.b6 = Button(text="Delete Anime CD Buyer", font="arial 20 bold", bg="#000000", fg="#ffffff",  command=self.deletebuyer)
        self.b7 = Button(text="Anime CD List", font="arial 20 bold", bg="#000000", fg="#ffffff",  command=self.animecdlist)
        self.b8 = Button(text="Anime CD Buyer List", font="arial 20 bold", bg="#000000", fg="#ffffff",  command=self.cdbuyerlist)
        self.b9 = Button(text="Bought Or Rented Anime CD List", font="arial 20 bold", bg="#000000", fg="#ffffff",  command=self.boughtcdlist)
        self.b1.place(x=30, y=50)
        self.b2.place(x=30, y=120)
        self.b3.place(x=30, y=190)
        self.b4.place(x=30, y=260)
        self.b5.place(x=30, y=330)
        self.b6.place(x=30, y=400)
        self.b7.place(x=30, y=470)
        self.b8.place(x=30, y=540)
        self.b9.place(x=30, y=610)
    def add_anime(self):
        """
                        Function to open a new window after pressing Add Anime Button
        """
        tk = Toplevel()
        obj = frontend.workboard.Add_AnimeCD(tk)
    def add_cdbuyer(self):
        """
                                Function to open a new window after pressing Add customer Button
        """
        tk = Toplevel()
        obj = frontend.workboard.Add_Buyer(tk)
    def buycd(self):
        """
                                Function to open a new window after pressing buycd Anime Button
        """
        tk = Toplevel()
        obj = frontend.workboard.buyorrentcd(tk)
    def returncd(self):
        """
                                Function to open a new window after pressing Return Anime Button
        """
        tk = Toplevel()
        obj = frontend.workboard.Return_AnimeCD(tk)
    def deletecd(self):
        """
                                Function to open a new window after pressing Delete Anime Button
        """
        tk = Toplevel()
        obj = frontend.workboard.Delete_CD(tk)
    def deletebuyer(self):
        """
                                Function to open a new window after pressing Delete customer Button
        """
        tk = Toplevel()
        obj = frontend.workboard.Delete_Buyer(tk)
    def animecdlist(self):
        """
                                Function to open a new window after pressing Anime list Button
        """
        tk = Toplevel()
        obj = frontend.workboard.binary_search_window(tk)
    def cdbuyerlist(self):
        """
                                        Function to open a new window after pressing Anime list Button
                """
        tk = Toplevel()
        obj = frontend.workboard.cdbuyerlist(tk)
    def boughtcdlist(self):
        """
                                                Function to open a new window after pressing Anime lenders Button
                        """
        tk = Toplevel()
        obj = frontend.workboard.boughtcdlist(tk)
