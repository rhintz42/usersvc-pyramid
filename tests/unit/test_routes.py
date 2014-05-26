try:
    import unittest2 as unittest
except:
    import unittest

from pyramid.testing import DummyRequest
import pytest
import mock

class TestAnonRoutes(unittest.TestCase):
    
    @pytest.mark.unit
    def test_home(self):
        from usersvc.views.home import home
        
        request = DummyRequest()

        result = home(request)

        assert result['status'] == 0
    
class TestUserRoutes(unittest.TestCase):

    @pytest.mark.unit
    def test_users_index(self):
        from usersvc.views.users import index
        
        request = DummyRequest()

        with mock.patch('usersvc.repos.users.UsersRepo.get_all') as get_all:
            get_all.return_value = []
            result = index(request)

        assert get_all.called_once()
        assert result['status'] == 0

    @pytest.mark.unit
    def test_users_show(self):
        from usersvc.views.users import show
        
        request = DummyRequest()
        request.matchdict = {'user_id': 'z'}

        with mock.patch('usersvc.repos.users.UsersRepo.get_user_by_id') as get_user_by_id:
            get_user_by_id.return_value = None
            result = show(request)

        assert get_user_by_id.called_once()
        assert result['status'] == 0

    """
    def test_users_update(self):
        from usersvc.views.users import update
        
        request = DummyRequest()
        request.matchdict = {'user_id': 'z'}

        with mock.patch('usersvc.models.users.User.udpate_by_id') as update_by_id:
            update_by_id.return_value = None
            result = show(request)

        assert update_by_id.called_once()
        assert result['status'] == 0
    """
