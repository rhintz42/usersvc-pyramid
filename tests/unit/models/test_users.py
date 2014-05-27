try:
    import unittest2 as unittest
except:
    import unittest

import pytest
import mock
import bcrypt

class TestUsersModel(unittest.TestCase):
    
    @pytest.mark.unit
    def test_verify_password__True(self):
        from usersvc.models.users import User
        user = User(None, None)
        user.password_digest = 'test'
        
        with mock.patch('usersvc.models.users.verify_password') as verify_password:
            verify_password.return_value = True
            result = user.verify_password('hello')

        assert verify_password.called_once()
        assert result == True
    
    @pytest.mark.unit
    def test_verify_password__False(self):
        from usersvc.models.users import User
        user = User(None, None)
        user.password_digest = 'test'
        
        with mock.patch('usersvc.models.users.verify_password') as verify_password:
            verify_password.return_value = False
            result = user.verify_password('hello')

        assert verify_password.called_once()
        assert result == False
