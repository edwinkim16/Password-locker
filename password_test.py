import unittest  # importing unittest module
from Password_Locker import Password

class TestPassword(unittest.TestCase):
    """
    Here is where we will perfome all our test
    """

    def setUp(self):
        """
        This function will create a new instance password before each test
        """
        self.new_password = Password("twitter", "edwin", "2021")

    def tearDown(self):
        """
        Here will be clearing password after every test to avoid confusion
        """
        Password.password = []   

    def test_new_pass(self):
        """
        Here will test if a new password is initiated correctly
        """
        self.assertEqual(self.new_password.account, "twitter")
        self.assertEqual(self.new_password.username, "edwin")
        self.assertEqual(self.new_password.password, "2021") 

if __name__ == "__main__":
    unittest.main()