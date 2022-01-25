import unittest
from passlocker import User
# from passlocker import Credentials

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

    


if __name__ == '__main__':
    unittest.main()
