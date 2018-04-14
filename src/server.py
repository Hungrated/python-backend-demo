from wsgiref.simple_server import make_server

from hello import application

httpd = make_server('', 9090, application)

print('Serving HTTP on port 9090...')
print('http://127.0.0.1:9090')
