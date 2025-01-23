from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def hello_pyramid(request):
    return Response('Hello Pyramid - pierwsza <b>aplikacja www</b>')

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('home','/')
        config.add_view(hello_pyramid,route_name='home')
        app = config.make_wsgi_app()

    server = make_server('127.0.0.1',6543,app)
    print("Serving on http://127.0.0.1:6543")
    server.serve_forever()
