from flask import Flask


def create_app():
    app = Flask(__name__)   # za postavitev "Flaska"
    app.config['SECRET_KEY'] = 'skrivnost'   # za enkripcijo seje in piškotkov

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app