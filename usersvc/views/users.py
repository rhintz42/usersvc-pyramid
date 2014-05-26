from pyramid.view import view_config
from usersvc.repos.users import UsersRepo


@view_config(route_name='users_index', renderer='json')
def index(request):
    users = UsersRepo().get_all()
    return {'data': {'users': [u.__dict__ for u in users]}, 'status': 0}


@view_config(route_name='users_show', renderer='json')
def show(request):
    user_id = request.matchdict['user_id']
    user = UsersRepo().get_user_by_id(user_id)

    if user:
        data = {'user': user.__dict__}
    else:
        data = {'user': None}

    return {'data': data, 'status': 0}


@view_config(route_name='users_update', renderer='json')
def users_update(request):
    user_id = request.matchdict['user_id']
    """
    # Create a repo for the User and have that return the model
    user_model = User(None, None)
    user = user_model.get_user_by_id(user_id)

    if user:
        data = {'user': user.username}
    else:
        data = {'user': None}

    return {'data': data, 'status': 0}
    """
    return {'data': None, 'status': 0}
