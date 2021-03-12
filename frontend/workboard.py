from tkinter import *
from tkinter import messagebox
import backend.dbconnection as db
import model.user as u
from PIL import ImageTk

class Bg_pic:
    def Bg_pic(self):
        """
                        Function to insert pic
        """
        self.image = ImageTk.PhotoImage(file="narutoimg2.png")
        self.canvas = Canvas(self.root, width=700, height=400)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.image, anchor=NW)
class Add_AnimeCD(Bg_pic):
    def E_check(self):
        """
        Checking For Empty Fields
        """
        AnimeId = self.e1.get()
        AnimeName = self.e2.get()
        AnimeMangaka = self.e3.get()
        AnimeQty = self.e4.get()
        if AnimeId == '' or AnimeName == '' or AnimeMangaka == '' or AnimeQty == '':
            messagebox.showerror('Error', 'Please Fill The Boxes')

    def Add_Animecd(self, id, cd, mangaka, qty):
        """
                        Function To insert Data into the Table
        """
        self.E_check()
        usr = u.user_model(id, cd, mangaka, qty)
        query = "insert into cds values(%s, %s, %s, %s)"
        values = (usr.get_id(), usr.get_cd(), usr.get_mangaka(), usr.get_qty())
        db.DBConnect().insert(query, values)

    def __init__(self,root):
        """
                        Function To Configure Root Window
        """
        self.root = root
        self.root.geometry("900x650+0+0")
        self.root.title("Add Anime CD")
        self.Bg_pic()
        main_frame = Frame(self.canvas, bd=10, bg='#000000', relief=SUNKEN)
        main_frame.place(x=80, y=60, width=700, height=400)
        self.l1 = Label(main_frame, text="Anime ID", font="arial 20 bold", bg="#000000", fg="#ffffff")
        self.e1 = Entry(main_frame, width=30)
        self.l2 = Label(main_frame, text="Anime Name", font="arial 20 bold", bg="#000000", fg="#ffffff")
        self.e2 = Entry(main_frame, width=30)
        self.l3 = Label(main_frame, text="Anime Mangaka", font="arial 20 bold", bg="#000000", fg="#ffffff")
        self.e3 = Entry(main_frame, width=30)
        self.l4 = Label(main_frame, text="Anime CD Quantity", font="arial 20 bold", bg="#000000", fg="#ffffff")
        self.e4 = Entry(main_frame, width=30)
        self.b1 = Button(main_frame, text="Add Anime CD", font="arial 20 bold", command=lambda: self.Add_Animecd(self.e1.get(), self.e2.get(), self.e3.get(), self.e4.get()), bg="#ffffff", fg="#000000")
        self.l1.place(x=20, y=30)
        self.e1.place(x=300, y=40)
        self.l2.place(x=20, y=80)
        self.e2.place(x=300, y=90)
        self.l3.place(x=20, y=130)
        self.e3.place(x=300, y=140)
        self.l4.place(x=20, y=180)
        self.e4.place(x=300, y=190)
        self.b1.place(x=20, y=250)


class Delete_CD(Bg_pic):
    def E_check(self):
        """
        checking id is given or not
        """
        CD_id = self.e1.get()
        if CD_id == '':
            messagebox.showerror('Error', 'please fill all the box')
    def Delete_CD(self, id):
        """
                        Function to delete cd from cds table
        """
        self.E_check()
        usr = u.user_model(id=id)
        query = "delete from cds where id=%s"
        values = (usr.get_id(),)
        db.DBConnect().delete(query, values)
    def __init__(self,root):
        """
                        Function to configure root window
        """
        self.root = root
        self.root.geometry("900x650+0+0")
        self.root.title("Delete Anime CD")
        self.Bg_pic()
        main_frame = Frame(self.canvas, bd=10, bg='#000000', relief=SUNKEN)
        main_frame.place(x=80, y=60, width=700, height=400)
        self.l1 = Label(main_frame, text="CD ID", font="arial 20 bold",bg="#000000", fg="#ffffff")
        self.e1 = Entry(main_frame, width=30)
        self.b1 = Button(main_frame, text="Delete CD", font="arial 20 bold", command=lambda: self.Delete_CD(self.e1.get()),bg="#ffffff", fg="#000000")
        self.l1.place(x=20, y=30)
        self.b1.place(x=20, y=230)
        self.e1.place(x=220, y=30)

class Add_Buyer(Bg_pic):
    def E_check(self):
        """
        checking all values are given or not
        """
        cid = self.e1.get()
        cname = self.e2.get()
        cpno = self.e3.get()
        if cid == '' or cname == '' or cpno == '':
            messagebox.showerror('Error', 'please fill all the box')
    def add_cdbuyer(self, cid, cname, pno):
        """
                        Function to insert in cdbuyers table
        """
        self.E_check()
        usr = u.user_model1(cid, cname, pno)
        query = "insert into cdbuyers values(%s, %s, %s)"
        values = (usr.get_cid(), usr.get_cname(), usr.get_pno())
        db.DBConnect().insert(query, values)
    def __init__(self,root):
        """
                        Function to configure root window
        """
        self.root = root
        self.root.geometry("900x650+0+0")
        self.root.title("Add CD Buyer")
        self.Bg_pic()
        main_frame = Frame(self.canvas, bd=10, bg='#000000', relief=SUNKEN)
        main_frame.place(x=80, y=60, width=700, height=400)
        self.l1 = Label(main_frame, text="Anime CD Buyer ID", font="arial 20 bold", bg="#000000",fg="#ffffff")
        self.e1 = Entry(main_frame, width=30)
        self.l2 = Label(main_frame, text="Anime CD Buyer Name", font="arial 20 bold", bg="#000000",fg="#ffffff")
        self.e2 = Entry(main_frame, width=30)
        self.l3 = Label(main_frame, text="Anime CD Buyer Phone", font="arial 20 bold", bg="#000000",fg="#ffffff")
        self.e3 = Entry(main_frame, width=30)
        self.b1 = Button(main_frame, text="Add Anime CD Buyer", font="arial 20 bold", command=lambda: self.add_cdbuyer(self.e1.get(), self.e2.get(), self.e3.get()), bg="#ffffff",fg="#000000")

        self.l1.place(x=20, y=30)
        self.e1.place(x=400, y=40)
        self.l2.place(x=20, y=80)
        self.e2.place(x=400, y=90)
        self.l3.place(x=20, y=130)
        self.e3.place(x=400, y=140)
        self.b1.place(x=20, y=250)




class Delete_Buyer(Bg_pic):
    def E_check(self):
        """
        check cdbuyers id is given or not
        """
        cid = self.e1.get()
        if cid == '':
            messagebox.showerror('Error', 'please fill all the box')
    def delete_cdbuyer(self, id):
        """
                        Function to delete cdbuyers from cdbuyers table
        """
        self.E_check()
        usr = u.user_model1(cid=id)
        query = "delete from cdbuyers where cid=%s"
        values = (usr.get_cid(),)
        db.DBConnect().delete(query, values)
    def __init__(self,root):
        """
                        Function to configure root window
        """
        self.root = root
        self.root.geometry("900x650+0+0")
        self.root.title("Delete Anime CD Buyer(Otaku)")
        self.Bg_pic()
        main_frame = Frame(self.canvas, bd=10, bg='#000000', relief=SUNKEN)
        main_frame.place(x=80, y=60, width=700, height=400)
        self.l1 = Label(main_frame, text="Anime Cd Buyer ID", font="arial 20 bold",bg="#000000", fg="#ffffff")
        self.e1 = Entry(main_frame, width=30)
        self.b1 = Button(main_frame, text="Delete Anime CD Buyer", font="arial 20 bold", command=lambda: self.delete_cdbuyer(self.e1.get()))
        self.l1.place(x=20, y=30)
        self.b1.place(x=20, y=230)
        self.e1.place(x=300, y=39)


class buyorrentcd(Bg_pic):
    def E_check(self):
        """
        checking all the fields are filled or not
        """
        tid = self.e1.get()
        bid = self.e2.get()
        cid = self.e3.get()
        idate = self.e4.get()
        rdate = self.e5.get()
        if tid == '' or bid == '' or cid == '' or idate == '' or rdate == '':
            messagebox.showerror('Error', 'please fill all the box')
    def check(self):
        dbase = db.DBConnect()
        query = "select * from cds where id=%s"
        values = (self.e2.get(),)
        rows = dbase.view(query, values)
        query1 = "select * from cdbuyers where cid=%s"
        values1 = (self.e3.get(),)
        rows1 = dbase.view(query1, values1)
        if len(rows) == 0 or len(rows1) == 0:
            return False
    def updateqty(self, id):
        self.db = db.DBConnect()
        query = "update cds set Quantity=Quantity-1 where id=%s"
        values = (int(self.e2.get()),)
        self.db.update(query, values)
    def insert_trans(self, tid, bid, cid, idate, rdate):
        """
                        Function to insert in trans table
        """
        self.E_check()
        if self.check() == False:
            messagebox.showerror("Lol", "You Are Not Otaku Bye")
            return
        usr = u.user_model2(tid, bid, cid, idate, rdate)
        query = "insert into trans values(%s, %s, %s, %s, %s)"
        values = (usr.get_tid(), usr.get_bid(), usr.get_cid(), usr.get_idate(), usr.get_rdate())
        db.DBConnect().insert(query, values)
        self.updateqty(self.e2.get())
    def __init__(self,root):
        """
                        Function to configure root window
        """
        self.root = root
        self.root.geometry("900x650+0+0")
        self.root.title("Buy Anime CD")
        self.Bg_pic()
        main_frame = Frame(self.canvas, bd=10, bg='#000000', relief=SUNKEN)
        main_frame.place(x=80, y=60, width=700, height=400)
        self.l1 = Label(main_frame, text="Transaction ID", font="arial 20 bold", bg="#000000",fg="#ffffff")
        self.e1 = Entry(main_frame, width=30)
        self.l2 = Label(main_frame, text="Anime CD Id", font="arial 20 bold", bg="#000000",fg="#ffffff")
        self.e2 = Entry(main_frame, width=30)
        self.l3 = Label(main_frame, text="CD Buyer ID", font="arial 20 bold", bg="#000000",fg="#ffffff")
        self.e3 = Entry(main_frame, width=30)
        self.l4 = Label(main_frame, text="CD Issue Date", font="arial 20 bold", bg="#000000",fg="#ffffff")
        self.e4 = Entry(main_frame, width=30)
        self.l5 = Label(main_frame, text="CD Return Date", font="arial 20 bold", bg="#000000",fg="#ffffff")
        self.e5 = Entry(main_frame, width=30)
        self.b1 = Button(main_frame, text="Buy CD", font="arial 20 bold", command=lambda: self.insert_trans(self.e1.get(),self.e2.get(),self.e3.get(),self.e4.get(),self.e5.get()), bg="#ffffff",fg="#000000")

        self.l1.place(x=20, y=30)
        self.e1.place(x=300, y=40)
        self.l2.place(x=20, y=80)
        self.e2.place(x=300, y=90)
        self.l3.place(x=20, y=130)
        self.e3.place(x=300, y=140)
        self.l4.place(x=20, y=180)
        self.e4.place(x=300, y=190)
        self.l5.place(x=20, y=230)
        self.e5.place(x=300, y=240)
        self.b1.place(x=20, y=300)



class Return_AnimeCD(Bg_pic):
    def E_check(self):
        """
        checks all the values are given or not
        """
        tid = self.e1.get()
        rdate = self.e2.get()
        if tid == '' or rdate == '':
            messagebox.showerror('Error', 'please fill all the box')
    def updateqty(self, id):
        dbase = db.DBConnect()
        query = "select bid from trans where tid=%s"
        values = (self.e1.get(),)
        bid = dbase.view(query, values)
        query1 = "update cds set Quantity=Quantity+1 where id=%s"
        values1 = (bid[0][0],)
        dbase.update(query1, values1)
    def checktid(self, id):
        dbase = db.DBConnect()
        query = "select * from trans where tid=%s"
        values = (self.e1.get(),)
        rows = dbase.view(query, values)
        if len(rows) == 0:
            return False
    def update_trans(self, rdate, tid):
        """
                        Function to update from trans table
        """
        self.E_check()
        if self.checktid(self.e1.get()) == False:
            messagebox.showerror("you have not taken CD", "Baka")
            return
        usr = u.user_model2(rdate=rdate, tid=tid)
        query = "update trans set recd = %s where tid = %s"
        values = (usr.get_rdate(), usr.get_tid())
        db.DBConnect().update(query, values)
        self.updateqty(self.e1.get())

    def __init__(self,root):
        """
                        Function to configure root window
        """
        self.root = root
        self.root.geometry("900x650+0+0")
        self.root.title("Return Anime CD")
        self.Bg_pic()
        main_frame = Frame(self.canvas, bd=10, bg='#000000', relief=SUNKEN)
        main_frame.place(x=80, y=60, width=700, height=400)
        self.l1 = Label(main_frame, text="Transaction ID", font="arial 20 bold", bg="#000000",fg="#ffffff")
        self.e1 = Entry(main_frame, width=30)
        self.l2 = Label(main_frame, text="Bought Date", font="arial 20 bold", bg="#000000",fg="#ffffff")
        self.e2 = Entry(main_frame, width=30)
        self.b1 = Button(main_frame, text="Return CD", font="arial 20 bold", command=lambda: self.update_trans(self.e2.get(),self.e1.get()), bg="#ffffff",fg="#000000")
        self.l1.place(x=20, y=30)
        self.e1.place(x=400, y=40)
        self.l2.place(x=20, y=80)
        self.e2.place(x=400, y=90)
        self.b1.place(x=20, y=230)

class binary_search:
    def mergesort(self, alist):
        """
                Function to perform merge sort:
                :param alist:list of CDid
                :type alist:list
                :return: alist
                :rtype: list
        """
        if len(alist) > 1:
            mid = len(alist) // 2
            lefthalf = alist[:mid]
            righthalf = alist[mid:]

            self.mergesort(lefthalf)
            self.mergesort(righthalf)

            i = 0
            j = 0
            k = 0

            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    alist[k] = lefthalf[i]
                    i = i + 1



                else:
                    alist[k] = righthalf[j]
                    j += 1
                k += 1

            while i < len(lefthalf):
                alist[k] = lefthalf[i]
                i += 1
                k += 1
            while j < len(righthalf):
                alist[k] = righthalf[j]
                j += 1
                k += 1
        return alist

    def binary_primary(self, list, item):
        """
                Function to perform binary search:
                :param list:list of cds id
                :type list:list
                :param item:specification of cds id
                :type item:int
                :return: True
                :return: False
                :rtype: bool
        """
        if list == []:
            return ValueError
        self.list = list
        self.item = item
        max = len(list) - 1
        min = 0
        while min <= max:
            mid = (min + max) // 2
            if self.list[mid] == self.item:
                return mid
            elif self.list[mid] > self.item:
                max = mid - 1
            else:
                min = mid + 1
        return False

    def search(self, rows, sorted, item):
        self.data = self.binary_primary(sorted, item)
        self.w.delete(0, END)
        self.w.insert(0, rows[self.data])

class binary_search_window(binary_search,Bg_pic):

    def __init__(self,root):
        """
                        Function to configure root window
        """
        self.root = root
        self.root.geometry("700x400+0+0")
        self.root.title("CD List")
        self.Bg_pic()
        self.query = "SELECT * FROM cds"
        self.w = Listbox(self.canvas, width=35, height=14,bg='#000000', fg="#ffffff")
        self.w.pack()
        rows = db.DBConnect().view(self.query)
        empt_list = []
        for row in rows:
            empt_list.append(row[0])
        self.sorted = self.mergesort(empt_list)
        print(self.sorted)
        i = 0
        for i in self.sorted:
            for row in rows:
                if i == row[0]:
                    self.w.insert(i, row)
                    i += 1
        self.b1 = Button(self.root, text=" Search", font="arial 20 bold", command=lambda: self.search(rows, self.sorted, int(self.e1.get())),bg='#ffffff', fg="#000000")
        self.e1 = Entry(self.root, width=30)
        self.b1.place(x=285, y=320)
        self.e1.place(x=255, y=280)

class cdbuyerlist(binary_search,Bg_pic):

    def __init__(self,root):
        """
                        Function to configure root window
        """
        self.root = root
        self.root.geometry("700x400+0+0")
        self.root.title("cdbuyers List")
        self.Bg_pic()
        self.query = "SELECT * FROM cdbuyers"
        self.w = Listbox(self.canvas, width=35, height=14,bg='#000000', fg="#ffffff")
        self.w.pack()
        rows = db.DBConnect().view(self.query)
        empt_list = []
        for row in rows:
            empt_list.append(row[0])
        self.sorted = self.mergesort(empt_list)
        print(self.sorted)
        i = 0
        for i in self.sorted:
            for row in rows:
                if i == row[0]:
                    self.w.insert(i, row)
                    i += 1
        self.b1 = Button(self.root, text="Search", font="arial 20 bold", command=lambda: self.search(rows, self.sorted, int(self.e1.get())),bg="#ffffff",fg="#000000")
        self.e1 = Entry(self.root, width=30)
        self.b1.place(x=285, y=320)
        self.e1.place(x=255, y=280)

class boughtcdlist(binary_search,Bg_pic):

    def __init__(self,root):
        """
                        Function to configure root window
        """
        self.root = root
        self.root.geometry("700x400+0+0")
        self.root.title("Bought CD List")
        self.Bg_pic()
        self.query = "SELECT * FROM trans"
        self.w = Listbox(self.canvas, width=35, height=14,bg='#000000', fg="#ffffff")
        self.w.pack()
        rows = db.DBConnect().view(self.query)
        empt_list = []
        for row in rows:
            empt_list.append(row[0])
        self.sorted = self.mergesort(empt_list)
        print(self.sorted)
        i = 0
        for i in self.sorted:
            for row in rows:
                if i == row[0]:
                    self.w.insert(i, row)
                    i += 1
        self.b1 = Button(self.root, text="Search", font="arial 20 bold", command=lambda: self.search(rows, self.sorted, int(self.e1.get())),bg="#ffffff",fg="#000000")
        self.e1 = Entry(self.root, width=30)
        self.b1.place(x=285, y=320)
        self.e1.place(x=255, y=280)
