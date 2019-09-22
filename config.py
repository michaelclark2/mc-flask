import os

base_dir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(base_dir, 'app.db')
  SQLALCHEMY_TRACK_MODIFICATION = False

  SECRET_KEY = os.environ.get('SECRET_KEY')
  ADMIN_PASSWORD = 'pbkdf2:sha256:150000$xqAx4226$f53be26c5350503a02863e81a925d439c899694db1692c59fe828c96f628cf3f'
