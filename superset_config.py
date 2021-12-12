ENABLE_PROXY_FIX = True

SQLALCHEMY_DATABASE_URI = \
    'postgresql+psycopg2://superset:superset@postgres:5432/superset'

from reverse_proxied import ReverseProxied
ADDITIONAL_MIDDLEWARE = [ReverseProxied, ]
