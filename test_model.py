import unittest
import model.user
class Test_User_model(unittest.TestCase):
    def setUp(self):
        """
                Function to set up the reference data for model.user.user_model()
        """
        self.a = model.user.user_model()
    def test_set_id(self):
        """
                Function to test if the set_id works or not.
        """
        self.a.set_id(12)
        self.assertEqual(12,self.a.get_id())
    def test_set_cd(self):
        """
                Function to test if the set_cd works or not.
        """
        self.a.set_cd("cinderella")
        self.assertEqual("cinderella",self.a.get_cd())
    def test_set_mangaka(self):
        """
                Function to test if the set_mangaka works or not.
        """
        self.a.set_mangaka("big 5")
        self.assertEqual("big 5",self.a.get_mangaka())
    def test_set_qty(self):
        """
                Function to test if the set_qty works or not.
        """
        self.a.set_qty(5)
        self.assertEqual(5,self.a.get_qty())
    def tearDown(self):
        """
                Function to tear down the model.user.user_model() reference
        """
        del self.a

class Test_User_model1(unittest.TestCase):
    def setUp(self):
        """
                Function to set up the reference data for model.user.user_model1()
        """
        self.a = model.user.user_model1()
    def test_set_cid(self):
        """
                Function to test if the set_cid works or not.
        """
        self.a.set_cid(11)
        self.assertEqual(11,self.a.get_cid())
    def test_set_cname(self):
        """
                Function to test if the set_cname works or not.
        """
        self.a.set_cname("milan")
        self.assertEqual("milan",self.a.get_cname())
    def test_set_pno(self):
        """
                Function to test if the set_pno works or not.
        """
        self.a.set_pno(9840293955)
        self.assertEqual(9840293955,self.a.get_pno())
    def tearDown(self):
        del self.a
        """
                Function to tear down the model.user.user_model1() reference
        """

class Test_User_model2(unittest.TestCase):
    def setUp(self):
        """
                Function to set up the reference data for model.user.user_model2()
        """
        self.a = model.user.user_model2()
    def test_set_tid(self):
        """
                Function to test if the set_tid works or not.
        """
        self.a.set_tid(13)
        self.assertEqual(13,self.a.get_tid())
    def test_set_bid(self):
        """
                Function to test if the set_bid works or not.
        """
        self.a.set_bid(14)
        self.assertEqual(14,self.a.get_bid())
    def test_set_cid(self):
        """
                Function to test if the set_cid works or not.
        """
        self.a.set_cid(15)
        self.assertEqual(15,self.a.get_cid())
    def test_set_idate(self):
        """
                Function to test if the set_idate works or not.
        """
        self.a.set_idate("feb 30")
        self.assertEqual("feb 30",self.a.get_idate())
    def test_set_rdate(self):
        """
                Function to test if the set_rdate works or not.
        """
        self.a.set_rdate("feb 25")
        self.assertEqual("feb 25",self.a.get_rdate())
    def tearDown(self):
        """
                Function to tear down the model.user.user_model2() reference
        """
        del self.a
if __name__ == '__main__':
    unittest.main()
