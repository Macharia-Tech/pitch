from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail
from flask_simplemde import SimpleMDE


db = SQLAlchemy()
photos = UploadSet('photos',IMAGES)

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

mail = Mail()
bootstrap = Bootstrap()

simple = SimpleMDE()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # # configure UploadSet
    # configure_uploads(app,photos)

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    simple.init_app(app)
    
    return app
# from flask import Flask
# from flask_bootstrap import Bootstrap
# from config import config_options
# from flask_sqlalchemy import SQLAlchemy

# bootstrap = Bootstrap()
# db = SQLAlchemy()

# login_manager = LoginManager()
# # login_manager.session_protection = 'strong'
# # login_manager.login_view = 'auth.login'

# def create_app(config_name):

#     app = Flask(__name__)

#     # Creating the app configurations
#     app.config.from_object(config_options[config_name])

#     # Initializing flask extensions
#     bootstrap.init_app(app)

#     # Will add the views and forms

#     return app