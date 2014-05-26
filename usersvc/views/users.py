from pyramid.view import view_config
from usersvc.repos.users import UsersRepo

import json


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
    user_info = json.loads(request.body)

    user = UsersRepo().update_by_id(user_id, user_info)

    data = {'user': None}

    return {'data': data, 'status': 0}


@view_config(route_name='users_create', renderer='json')
def users_create(request):
    user_info = json.loads(request.body)

    result = UsersRepo().create(user_info)

    data = {'user': result}

    return {'data': data, 'status': 0}


@view_config(route_name='users_delete', renderer='json')
def users_delete(request):
    user_id = request.matchdict['user_id']

    result = UsersRepo().delete(user_id)

    data = {'user': result}

    return {'data': data, 'status': 0}
