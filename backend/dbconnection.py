import mysql.connector as ms
from mysql.connector import errors
class DBConnect:

    def __init__(self):
        try:
            self.con=ms.connect(host='localhost',user='root',password='root',database='sys')
            self.cur=self.con.cursor()
            
            self.cur.execute("CREATE TABLE IF NOT EXISTS user_tbl (username VARCHAR(20), password VARCHAR(64), Gender VARCHAR(6), Address VARCHAR(64))")

            self.cur.execute("CREATE TABLE IF NOT EXISTS cds(id int primary key not null, \
            CDName varchar(30) not null, Mangaka varchar(30) not null, Quantity int not null)")
            self.cur.execute("CREATE TABLE IF NOT EXISTS cdbuyers(cid int primary key not null, \
                CDbuyerName varchar(30) not null, Phone bigint(10) not null)")
            self.cur.execute("CREATE TABLE IF NOT EXISTS trans(tid int primary key,bid int,cid int,\
            issue varchar(30),recd varchar(50))")
        except errors.Error as e:
            print("The mysql error occured is: ", e)

    def insert(self,query,values):
        self.cur.execute(query,values)
        self.con.commit()
    def select(self,query,values):
        self.cur.execute(query,values)
        records=self.cur.fetchall()
        return records
    def insert(self, query, values):
        """
                Function to do insert in a database.
                :param query:
                :type query:
                :param values:
                :type values:
        """
        self.query = query
        self.values = values
        self.cur.execute(self.query, self.values)
        self.con.commit()
    def view(self, query, values=""):
        """
                Function to fetch data.
                :param query:
                :type query:
                :param values:
                :type values:
                :rtype: list:
        """
        self.query = query
        self.values = values
        self.cur.execute(self.query, self.values)
        return self.cur.fetchall()
    def update(self, query, values):
        """
                Function to do update in a database.
                :param query:
                :type query:
                :param values:
                :type values:
        """
        self.query = query
        self.values = values
        self.cur.execute(self.query, self.values)
        self.con.commit()
    def delete(self, query, values):
        """
                Function to do delete in a database.
                :param query:
                :type query:
                :param values:
                :type values:
        """
        self.query = query
        self.values = values
        self.cur.execute(self.query, self.values)
        self.con.commit()


