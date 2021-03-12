import unittest
import frontend.workboard

class Test_binary_search(unittest.TestCase):
    def setUp(self):
        """
                Function to set up the reference data for frontend.workboard.binary_search()
        """
        self.a = frontend.workboard.binary_search()
    def test_mergesort(self):
        """
                Function to test if the mergesort works or not.
        """
        v_id = [1,5,6,3,2,9,8]
        self.assertEqual([1,2,3,5,6,8,9],self.a.mergesort(v_id))
    def test_binary_primary(self):
        """
                Function to test if the binary_primary works or not.
        """
        v_id = [1,2,3,4,5,6,7,8,9]
        self.assertEqual(1,self.a.binary_primary(v_id,2))
    def tearDown(self):
        """
                Function to tear down the frontend.workboard.binary_search() reference
        """
        del self.a
if __name__ == '__main__':
    unittest.main()
