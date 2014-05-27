import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyramid',
    'pyramid_chameleon',
    'pyramid_debugtoolbar',
    'waitress',
    'pytest',
    'mock',
    'sqlalchemy',
    'zope.sqlalchemy',
    'webtest',
    'requests',
    'bcrypt',
    ]

setup(name='usersvc',
      version='0.0',
      description='usersvc',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="usersvc",
      entry_points="""\
      [paste.app_factory]
      main = usersvc:main
      [console_scripts]
      initialize_usersvc_db = scripts.initializedb:main
      """,
      )
