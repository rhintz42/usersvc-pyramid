try:
    import unittest2 as unittest
except:
    import unittest

from pyramid.testing import DummyRequest
import pytest
import mock
import requests


#class TestUserRoutes(unittest.TestCase):

@pytest.mark.functional
def test_users_index(session, wsgiapp):
    response = wsgiapp.get('/users/')
    a = 10
    pass
