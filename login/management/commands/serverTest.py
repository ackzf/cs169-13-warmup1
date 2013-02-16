"""
Unit tests for the server.py module.
This is just a sample. You should have more tests for your model (at least 10)
"""

import unittest
import sys

import server


class TestUsers(unittest.TestCase):
    """
    Unittests for the Users model class (a sample, incomplete)
    """
    def setUp(self):
        self.users = server.UsersModel ()
        self.users.reset ()

        
    def testAdd1(self):
        """
        Tests that adding a user works
        """
        self.users.reset()
        self.assertEquals(server.SUCCESS, self.users.add("user1", "password"))

    def testAddExists(self):
        """
        Tests that adding a duplicate user name fails
        """
        self.users.reset()
        self.assertEquals(server.SUCCESS, self.users.add("user1", "password"))
        self.assertEquals(server.ERR_USER_EXISTS, self.users.add("user1", "password"))

    def testAdd2(self):
        """
        Tests that adding two users works
        """
        self.users.reset()
        self.assertEquals(server.SUCCESS, self.users.add("user1", "password"))
        self.assertEquals(server.SUCCESS, self.users.add("user2", "password"))

    def testAddEmptyUsername(self):
        """
        Tests that adding an user with empty username fails
        """
        self.users.reset()
        self.assertEquals(server.ERR_BAD_USERNAME, self.users.add("", "password"))
        
    def testAddLogin(self):
        self.users.reset()
        self.assertEquals(server.SUCCESS, self.users.add("user1", "password"))
        self.assertEquals(2, self.users.login(self, "user1", "password"))
        
    def testAddLongUser(self):
        self.users.reset()
        a = ""
        for i in range(0,127)
            a += "a"
        self.assertEquals(server.SUCCESS, self.users.add(a, "password"))
        aa = a + "aa"
        self.assertEquals(server.ERR_BAD_USERNAME, self.users.add(aa, "password"))
    
    def testAddLongPword(self):
        self.users.reset()
        a = ""
        for i in range(0,127)
            a += "a"
        self.assertEquals(server.SUCCESS, self.users.add("user1", a))
        aa = a + "aa"
        self.assertEquals(server.ERR_BAD_PASSWORD, self.users.add("user2", aa))
    
    def testLongIser:
        self.users.reset()
        a = ""
        for i in range(0,127)
            a += "a"
        self.assertEquals(server.SUCCESS, self.users.add(a, "pass"))
        self.assertEquals(2, self.users.login(self, a, "pass"))
    
    def testLongPword:
        self.users.reset()
        a = ""
        for i in range(0,127)
            a += "a"
        self.assertEquals(server.SUCCESS, self.users.add("user1", a))
        self.assertEquals(2, self.users.login(self, "user1", a))
        

# If this file is invoked as a Python script, run the tests in this module
if __name__ == "__main__":
    # Add a verbose argument
    sys.argv = [sys.argv[0]] + ["-v"] + sys.argv[1:]
    unittest.main()
