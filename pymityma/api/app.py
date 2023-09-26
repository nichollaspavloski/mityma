import json

from flask import Flask, g
from flask_cors import CORS

from api.database import get_db

class PrefixMiddleware(object):
    def __init__(self, app, prefix=''):
        self.app = app
        self.prefix = prefix

    def __call__(self, environ, start_response):

        if environ['PATH_INFO'].startswith(self.prefix):
            environ['PATH_INFO'] = environ['PATH_INFO'][len(self.prefix):]
            environ['SCRIPT_NAME'] = self.prefix
            return self.app(environ, start_response)
        else:
            start_response('404', [('Content-Type', 'text/plain')])
            return ["This url does not belong to the app.".encode()]


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")
    app.secret_key = 'N2VQskXT5ToCLYue6G4JzW7BZyquvuhy'
    app.wsgi_app = PrefixMiddleware(app.wsgi_app, prefix='/api')
    CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    from .server import db, ma, migrate
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    from .route.producer import producer_api
    from .route.green import green_api
    app.register_blueprint(producer_api, url_prefix='/producer')
    app.register_blueprint(green_api, url_prefix='/green')

    @app.before_request
    def before_callback():
        if 'db' not in g:
            g.db = get_db()

    @app.after_request
    def after_callback(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', '*')
        response.headers.add('Access-Control-Allow-Methods', '*')
        data = response.get_data()

        if data is not None:
            content = json.loads(data)
        else:
            return response

        success = content['success'] == 1

        db_obj = g.get('db')
        if success:
             db_obj.commit()
        else:
            db_obj.rollback()

        return response

    return app
