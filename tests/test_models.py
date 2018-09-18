import unittest
from app.models import User,Profile

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(password = 'banana')

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)
        
    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('banana'))

class ProfileModelTest(unittest.TestCase):

    def setUp(self):

        self.new_profile = Profile(teamname='Coachya', vision='Champions',mission='Tiki-taka is king',members='11')

    def test_instance(self):
        '''
        Test case to check if new_post is an instance of Posts class
        '''
        self.assertTrue( isinstance( self.new_profile, Profile) )

    def test_save_team(self):
        '''
        Test case to check if a post is saved to the database
        '''
        self.new_profile.save_profile()

        self.assertTrue( len(Profile.query.all()) > 0 )


