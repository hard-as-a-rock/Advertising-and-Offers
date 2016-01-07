SQLALCHEMY_DATABASE_URI = \
    "postgresql://role:role@localhost/role"

try:
    from local_settings import *
except ImportError:
    pass