ENABLE_PROXY_FIX = True

# SQLALCHEMY_DATABASE_URI = 'sqlite:////app/superset_home/superset.db'

from reverse_proxied import ReverseProxied
ADDITIONAL_MIDDLEWARE = [ReverseProxied, ]
