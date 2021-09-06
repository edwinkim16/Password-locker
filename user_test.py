import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    This class will contain all tests for the user class
    '''
    def setUp(self):
        '''
        This will first create new user before each test
        '''
        self.new_user = User ("edwin","1998")

    def test_init(self):
        '''
        This will validate whether the user is correctly registered
        '''
        self.assertEqual(self.new_user.login,"edwin")
        self.assertEqual(self.new_user.password,"1998")

    
    def test_user_password(self):
        '''
        This will check whether the password exists
        '''
        self.assertTrue(User.user_exist)    

if __name__ == '__main__':
    unittest.main()        