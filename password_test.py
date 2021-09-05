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

    def test_save_new_password(self):
        """
        Here it will check weather the new password is added in the list
        """
        self.new_password.save_password()
        self.assertEqual(len(Password.password_list), 1)  

    def test_add_generate_password(self):
        """
        This will check if the new password added to the list
        """
        new_password = Password("facebook", "2021", Password.generate_(6))
        new_password.save_password()
        self.assertEqual(len(Password.password))      

if __name__ == "__main__":
    unittest.main()