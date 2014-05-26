from pyramid.config import Configurator
from pyramid.httpexceptions import HTTPNotFound

from sqlalchemy import engine_from_config
from .db_tables import DBSession, Base

def user_routes(config):
    config.add_route('users_index', '/', request_method='GET')
    config.add_route('users_show', '/{user_id}', request_method='GET')
    config.add_route('users_update', '/{user_id}', request_method='PUT')

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)

    config = Configurator(settings=settings)
    config.add_route('home', '/')
    config.include(user_routes, route_prefix='/users')
    config.add_notfound_view(HTTPNotFound('Slash not at end, adding one.'), append_slash=True)
    config.scan()
    return config.make_wsgi_app()
