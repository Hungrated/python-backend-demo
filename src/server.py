from wsgiref.simple_server import make_server

from hello import app

httpd = make_server('', 9090, app)

print('Serving HTTP on port 9090...')
print('http://127.0.0.1:9090')

httpd.serve_forever()
