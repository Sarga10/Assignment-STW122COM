import backend.dbconnection
import unittest
class Test_DBconnect(unittest.TestCase):
    def setUp(self):
        """
                Function to set up the reference data for backend.dbconnection.DBConnect()
        """
        self.a = backend.dbconnection.DBConnect()
    def test_insert(self):
        """
                Function to test if the insert() works or not.
        """
        query = "insert into cds values(%s,%s,%s,%s)"
        values = (109876,"cinderella","big 5",5)
        self.a.insert(query,values)
        query1 = "select * from cds where id=109876"

    def test_update(self):
        """
                Function to test if the update works or not.
        """
        query = "insert into cds values(%s,%s,%s,%s)"
        values = (156098,"haha","haha 5",2)
        self.a.insert(query, values)
        query1 = "update cds set Quantity=%s where id=%s"
        values1 = (5, 156098)
        self.a.update(query1, values1)
        query2 = "select * from cds where id=156609"

    def tearDown(self):
        """
                Function to tear down the backend.dbconnection.DBConnect() reference
        """
        del self.a


if __name__ == '__main__':
    unittest.main()
