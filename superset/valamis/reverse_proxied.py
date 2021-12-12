from flask import Flask
from typing import Dict, Any, Callable


# source: https://github.com/apache/incubator-superset/pull/1866#issuecomment-347310860
class ReverseProxied(object):

    def __init__(self, app: Flask):
        self.app = app

    def __call__(
            self, environ: Dict[str, Any], start_response: Callable[..., Any]
    ) -> Any:
        script_name = '/analytics'
        environ['SCRIPT_NAME'] = script_name
        path_info = environ['PATH_INFO']
        if path_info.startswith(script_name):
            environ['PATH_INFO'] = path_info[len(script_name):]
        host = environ.get('HTTP_X_FORWARDED_HOST', '')
        if host:
            environ['HTTP_HOST'] = host
        scheme = environ.get('HTTP_X_SCHEME', '')
        if scheme:
            environ['wsgi.url_scheme'] = scheme
        return self.app(environ, start_response)
