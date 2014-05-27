try:
    import unittest2 as unittest
except:
    import unittest

import pytest
import mock
import bcrypt

class TestUsersLib(unittest.TestCase):
    
    @pytest.mark.unit
    def test_encrypt_password(self):
        from usersvc.lib.users import encrypt_password
        password_digest = '$2a$10$AhRiWLpCq0BRzo8an56ysuzqc/sgd00vsaNk/A/m0MxlvFGqBBAQy'
        
        result = encrypt_password('hello')

        assert bcrypt.hashpw('hello', password_digest) == password_digest

    
    @pytest.mark.unit
    def test_verify_password(self):
        from usersvc.lib.users import verify_password
        password_digest = '$2a$10$AhRiWLpCq0BRzo8an56ysuzqc/sgd00vsaNk/A/m0MxlvFGqBBAQy'
        
        result = verify_password('hello', password_digest)

        assert result == True
        

    @pytest.mark.unit
    def test_verify_password__False1(self):
        from usersvc.lib.users import verify_password
        password_digest = '$2a$10$AhRiWLpCq0BRzo8an56ysuzqc/sgd00vsaNk/A/m0MxlvFGqBBAQy'
        
        result = verify_password('helli', password_digest)

        assert result == False
        

    @pytest.mark.unit
    def test_verify_password__False2(self):
        from usersvc.lib.users import verify_password
        password_digest = '$2a$10$AhRiWLpCq0BRzo8an56ysuzqc/sgd00vsaNk/A/m0MxlvFGqBBAQy'
        
        result = verify_password('hello2', password_digest)

        assert result == False
