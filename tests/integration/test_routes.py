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
def test_users_create(session, wsgiapp):
    response = wsgiapp.post_json('/users/', {'username': 'clm21020'})
    assert response.status == '200 OK'


@pytest.mark.functional
def test_users_update(session, wsgiapp):
    response = wsgiapp.put_json('/users/2', {'user_id': '1', 'username': 'roberth42'})
    assert response.status == '200 OK'


@pytest.mark.functional
def test_users_delete(session, wsgiapp):
    #import pdb;pdb.set_trace()
    #with mock.patch('usersvc.repos.users.UsersRepo.delete') as delete:
        #delete.return_value = {'status': '0', 'data': 'Create User Successful'}
    response = wsgiapp.delete('/users/1')
    #import pdb;pdb.set_trace()
    assert response.status == '200 OK'


@pytest.mark.functional
def test_users_index_2(session, wsgiapp):
    response = wsgiapp.get('/users/')
    assert response.status == '200 OK'


