class User:
    def __init__(self,uname,passw,add,gen):
        self.__username=uname
        self.__password=passw
        self.__address=add
        self.__gen=gen

    def set_username(self,uname):
        self.__username=uname

    def get_username(self):
        return self.__username

    def set_password(self, passw):
        self.__password = passw

    def get_password(self):
        return self.__password

    def set_address(self, add):
        self.__address = add

    def get_address(self):
        return self.__address

    def set_gender(self, gen):
        self.__gen = gen

    def get_gender(self):
        return self.__gen
    

class user_model:
    def __init__(self, id="", cd="", mangaka="", qty=""):
        self.__id = id
        self.__cd = cd
        self.__mangaka = mangaka
        self.__qty = qty
    def set_id(self, id):
        """
                Function to set value for id.
                :param id:set_id
                :type id:int
        """
        self.__id = id
    def get_id(self):
        return self.__id

    def set_cd(self, cd):
        """
                Function to set value for cd.
                :param cd:set_cd
                :type cd:str
        """
        self.__cd = cd
    def get_cd(self):
        return self.__cd

    def set_mangaka(self, mangaka):
        """
                Function to set value for mangaka.
                :param mangaka:set_mangaka
                :type mangaka:str
        """
        self.__mangaka = mangaka
    def get_mangaka(self):
        return self.__mangaka

    def set_qty(self, qty):
        """
                Function to set value for qty.
                :param qty:set_qty
                :type qty:int
        """
        self.__qty = qty
    def get_qty(self):
        return self.__qty

class user_model1:
    def __init__(self, cid="", cname="", pno=""):
        self.__cid = cid
        self.__cname = cname
        self.__pno = pno
    def set_cid(self, cid):
        """
                 Function to set value for cid.
                 :param cid:set_cid
                 :type cid:int
        """
        self.__cid = cid
    def get_cid(self):
        return self.__cid

    def set_cname(self, cname):
        """
                 Function to set value for cname.
                 :param cname:set_cname
                 :type cname:str
        """
        self.__cname = cname
    def get_cname(self):
        return self.__cname

    def set_pno(self, pno):
        """
                         Function to set value for pno.
                         :param pno:set_pno
                         :type pno:int
        """
        self.__pno = pno
    def get_pno(self):
        return self.__pno

class user_model2:
    def __init__(self, tid="", bid="", cid="", idate="", rdate="" ):
        self.__tid = tid
        self.__bid = bid
        self.__cid = cid
        self.__idate = idate
        self.__rdate = rdate
    def set_tid(self, tid):
        """
                         Function to set value for tid.
                         :param tid:set_tid
                         :type tid:int
        """
        self.__tid = tid
    def get_tid(self):
        return self.__tid

    def set_bid(self, bid):
        """
                         Function to set value for bid.
                         :param bid:set_bid
                         :type bid:int
        """
        self.__bid = bid
    def get_bid(self):
        return self.__bid

    def set_cid(self, cid):
        """
                         Function to set value for cid.
                         :param cid:set_cid
                         :type cid:int
        """
        self.__cid = cid
    def get_cid(self):
        return self.__cid

    def set_idate(self, idate):
        """
                         Function to set value for idate.
                         :param idate:set_idate
                         :type idate:str
        """
        self.__idate = idate
    def get_idate(self):
        return self.__idate

    def set_rdate(self, rdate):
        """
                         Function to set value for rdate.
                         :param rdate:set_rdate
                         :type rdate:str
        """
        self.__rdate = rdate
    def get_rdate(self):
        return self.__rdate
