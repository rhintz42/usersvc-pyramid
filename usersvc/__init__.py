from pyramid.config import Configurator
from pyramid.httpexceptions import HTTPNotFound

from sqlalchemy import engine_from_config
from .db_tables import DBSession, Base

def user_routes(config):
    config.add_route('users_index', '/', request_method='GET')
    config.add_route('users_show', '/{user_id}', request_method='GET')
    config.add_route('users_update', '/{user_id}', request_method='PUT')
    config.add_route('users_create', '/', request_method='POST')
    config.add_route('users_delete', '/{user_id}', request_method='DELETE')

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.',
    connect_args={'check_same_thread': False})  # ADDING `check_same_thread` to
                                                # False removes the multiple
                                                # threads error with SQLite
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)

    config.add_static_view('static', 'static', cache_max_age=3600)
    config = Configurator(settings=settings)
    config.add_route('home', '/')
    config.include(user_routes, route_prefix='/users')
    config.add_notfound_view(HTTPNotFound('Slash not at end, adding one.'), append_slash=True)
    config.scan()
    return config.make_wsgi_app()
