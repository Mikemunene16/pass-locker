import unittest
from passlocker import User
from passlocker import Credentials

class TestClass(unittest.TestCase):
    """
    A test case that defines test cases for User Class behaviours
    """
    def setUp(self):
        """
        Method that runs before each individual test method run.
        """
        self.new_user = User("Mike1622","michael")

    def test_init(self):
        """
        test case to check if the object has been initialized correctly
        """
        self.assertEqual(self.new_user.username, "Mike1622")
        self.assertEqual(self.new_user.password, "michael")

    def test_save_user(self):
        """
        test case to test if new user instance has been saved to the User list
        """

        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)


class TestCredentials(unittest.TestCase):
    """
    A test class that defines test cases for class Credentials.
    """

    def setUp(self):
        """
        Method that runs before each individual credentials test method run.
        """

        self.new_credential = Credentials("Instagram", "mikey", "09876")

    def test_init(self):
        """
        Test case to check if new Credentials has been initialized correctly
        """

        self.assertEqual(self.new_credential.account , "Instagram") 
        self.assertEqual(self.new_credential.userName, "mikey") 
        self.assertEqual(self.new_credential.password, "09876")

    def save_credential_test(self):
        """
        test case to see if whether user new credential has been saved in the credential list.
        """ 

        self.new_credential.save_details()   
        self.assertEqual(len(Credentials.credential_list),1)

    
    def tearDown(self):
        '''
        method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []


    def test_save_many_accounts(self):
        '''
        test to check if we can save multiple credentials objects to our credentials list
        '''
        self.new_credential.save_details()
        test_credential = Credentials("Twitter","munene","mmmm") 
        test_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list),2)


    def test_delete_credential(self):
        """
        test method to test whether one can delete a credentials account from credentials list.
        """

        self.new_credential.save_details()
        test_credential = Credentials("Twitter","munene","mmmm")
        test_credential.save_details()

        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
   
    
    def test_find_credential(self):
        """
        test to check if we can find a credential entry by account name and display details of the credential
        """

        self.new_credential.save_details()
        test_credential = Credentials("Twitter", "munene", "mmmm")
        test_credential.save_details()

        the_credential = Credentials.find_credentials("Twitter")

        self.assertEqual(the_credential.account,test_credential.account)

    
    def test_credential_exist(self):
        """
        test to check if we can return a true or false based on whether we find or can't find the credential.
        """
        self.new_credential.save_details()
        the_credential = Credentials("Twitter", "munene", "mmmm")  
        the_credential.save_details()
        credential_is_found = Credentials.if_credential_exist("Twitter")
        self.assertTrue(credential_is_found)


    def test_display_all_saved_credentials(self):
        '''
        method that displays all the credentials that has been saved by the user
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

    

if __name__ == '__main__':
    unittest.main()
