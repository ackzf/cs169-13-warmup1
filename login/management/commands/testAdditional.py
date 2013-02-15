"""
Each file that starts with test... in this directory is scanned for subclasses of unittest.TestCase or testLib.RestTestCase
"""

import unittest
import os
import testLib

class TestAddUserError(testLib.RestTestCase):
    """Test adding users"""
    def assertResponse(self, respData, count = 1, errCode = testLib.RestTestCase.SUCCESS):
        """
        Check that the response data dictionary matches the expected values
        """
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)

    def testAddDup(self):
        self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        self.assertResponse(respData, count = None, errorCode = testLib.RestTestCase.ERR_USER_EXISTS)
        
class TestWrongUser(testLib.RestTestCase):
    """Test adding users"""
    def assertResponse(self, respData, count = 1, errCode = testLib.RestTestCase.SUCCESS):
        """
        Check that the response data dictionary matches the expected values
        """
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)

    def testWrongUser(self):
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'random234878374', 'password' : 'password'} )        
        self.assertResponse(respData, count = None, errorCode = testLib.RestTestCase.ERR_BAD_CREDENTIALS)
        
class TestWrongPassWord(testLib.RestTestCase):
    """Test adding users"""
    def assertResponse(self, respData, count = 1, errCode = testLib.RestTestCase.SUCCESS):
        """
        Check that the response data dictionary matches the expected values
        """
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)

    def testWrongPword(self):
        self.makeRequest("/users/add", method="POST", data = { 'user' : 'user22', 'password' : 'password'} )       
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'user22', 'password' : 'password1'} )        
        self.assertResponse(respData, count = None, errorCode = testLib.RestTestCase.ERR_BAD_CREDENTIALS)
        
class TestBadUser(testLib.RestTestCase):
    """Test adding users"""
    def assertResponse(self, respData, count = 1, errCode = testLib.RestTestCase.SUCCESS):
        """
        Check that the response data dictionary matches the expected values
        """
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)

    def testBadUser(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : '', 'password' : 'password'} )                       
        self.assertResponse(respData, count = None, errorCode = testLib.RestTestCase.ERR_BAD_USERNAME)
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890', 'password' : 'password'} )                       
        self.assertResponse(respData, count = None, errorCode = testLib.RestTestCase.ERR_BAD_USERNAME)

    
class TestBadPword(testLib.RestTestCase):
    """Test adding users"""
    def assertResponse(self, respData, count = 1, errCode = testLib.RestTestCase.SUCCESS):
        """
        Check that the response data dictionary matches the expected values
        """
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)

    def testBadPword(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user5', 'password' : '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890'} )                       
        self.assertResponse(respData, count = None, errorCode = testLib.RestTestCase.ERR_BAD_PASSWORD)

class TestLoginCount(testLib.RestTestCase):
    """Test adding users"""
    def assertResponse(self, respData, count = 1, errCode = testLib.RestTestCase.SUCCESS):
        """
        Check that the response data dictionary matches the expected values
        """
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)

    def testLoginCount(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        for i in range(2,10):
            respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
            self.assertResponse(respData, count = i)

    