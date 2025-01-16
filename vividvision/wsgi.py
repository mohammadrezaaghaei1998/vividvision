"""
WSGI config for vividvision project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vividvision.settings')

application = get_wsgi_application()






# In WSGI.py
# def application(environ, start_response):
#     if environ.get('HTTP_HOST') == 'vividvisiongcc.org':
#         start_response('301 Moved Permanently', [('Location', 'https://www.vividvisiongcc.org')])
#         return [b'']

#     from django.core.wsgi import get_wsgi_application
#     _application = get_wsgi_application()
#     return _application(environ, start_response)


