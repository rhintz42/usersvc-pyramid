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
    assert response.status == '200 OK'

@pytest.mark.functional
def test_users_index_no_trailing_slash(session, wsgiapp):
    response = wsgiapp.get('/users')
    assert response.status == '302 Found'



@pytest.mark.functional
def test_users_show(session, wsgiapp):
    response = wsgiapp.get('/users/1')
    assert response.status == '200 OK'


@pytest.mark.functional
def test_users_update(session, wsgiapp):
    response = wsgiapp.put_json('/users/1', {'user_id': '1', 'username': 'roberth42'})
    assert response.status == '200 OK'
