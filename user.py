
class User:
    '''
    The User class will contain user details
    '''

    def __init__(self, login, password):
        '''
         Ensuring the user class has unique properties
        '''
        self.login = login
        self.password = password
