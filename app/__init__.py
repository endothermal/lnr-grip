from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_assets import Environment
from flask_session import Session
from flask_marshmallow import Marshmallow
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from flask_fontawesome import FontAwesome


# Globally accessible libraries
db = SQLAlchemy()
Session = sessionmaker()
ma = Marshmallow()
fa = FontAwesome()


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    assets = Environment()
    # Anything else?
    app.secret_key = app.config["SECRET_KEY"]
    app.config['SESSION_TYPE'] = 'filesystem' #change to redis when you have one of those set up

    db_url = None
    if app.config['WHEREAMI']=="LOCAL":
        sql_hostname = app.config['SQL_HOSTNAME']
        print("Connecting (init) to " + sql_hostname + "...")

        sql_port = int(app.config['SQL_PORT'])
        app.config['SQLALCHEMY_DATABASE_URI'] = app.config['SQLALCHEMY_DATABASE_URI'].format(sql_port)
        db_url = app.config['SQLALCHEMY_DATABASE_URI']
    elif app.config['WHEREAMI']=="HEROKU":
        db_url = app.config['CLEARDB_DATABASE_URL']
        print("Connecting to {}...".format(db_url))
    else:
        print("ARE YOUR ENVIRONMENT VARIABLES SET UP CORRECTLY?")

    engine = create_engine(db_url, pool_recycle=60, pool_pre_ping=True)
    Session.configure(bind=engine)

    # Initialize Plugins
    db.init_app(app)
    assets.init_app(app)
    ma.init_app(app)
    fa.init_app(app)

    with app.app_context():

        # Create DB models
        db.create_all()

        # Import parts of our application
        from .api import api_routes
        from .main import main_routes
        from .assets import compile_static_assets
        # Register Blueprints
        app.register_blueprint(api_routes.api_bp)
        app.register_blueprint(main_routes.main_bp)

        # Compile static assets
        if app.config['FLASK_ENV'] == 'development':
        #if 1 == 1:
            compile_static_assets(assets)

        return app

@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()