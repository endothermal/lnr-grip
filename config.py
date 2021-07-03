
from dotenv import load_dotenv
from pathlib import Path  # python3 only

"""App configuration."""
from os import environ
from dotenv import load_dotenv
from pathlib import Path  # python3 only
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)



class Config:
    """Set Flask configuration vars from .env file."""

    #General config
    WHEREAMI  = environ.get('WHEREAMI')
    FLASK_APP  = environ.get('FLASK_APP')
    FLASK_ENV  = environ.get('FLASK_ENV')
    SESSION_TIMEOUT = environ.get('SESSION_TIMEOUT')
    TUNNEL_TIMEOUT = environ.get('TUNNEL_TIMEOUT')
    SSH_TIMEOUT = environ.get('SSH_TIMEOUT')
    LOG_SOURCE = environ.get('LOG_SOURCE')

    # Database
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_RECYCLE = 3600 #just has to be smaller than datateam's which is 8 hrs (28800)
    DB_USE_SSL = environ.get("DB_USE_SSL")

    # Static Assets
    STATIC_FOLDER     = environ.get("STATIC_FOLDER")
    TEMPLATES_FOLDER  = environ.get("TEMPLATES_FOLDER")
    # Flask-Assets
    LESS_BIN          = environ.get("LESS_BIN")
    ASSETS_DEBUG      = False
    ASSETS_AUTO_BUILD = environ.get("ASSETS_AUTO_BUILD")

    DEBUG = True
    TESTING = True
    DASHBOARD_ENVIRONMENT=environ.get('DASHBOARD_ENVIRONMENT')
    SECRET_KEY = environ.get('SECRET_KEY')
    #DB connection variables
    SQL_HOSTNAME       = environ.get("SQL_HOSTNAME")
    SQL_USERNAME       = environ.get("SQL_USERNAME")
    SQL_PASSWORD       = environ.get("SQL_PASSWORD")
    SQL_DATABASE       = environ.get("SQL_DATABASE")
    SQL_PORT           = environ.get("SQL_PORT")
    SSH_HOST           = environ.get("SSH_HOST")
    SSH_USER           = environ.get("SSH_USER")
    SSH_PASSWORD       = environ.get("SSH_PASSWORD")
    SSH_PORT           = environ.get("SSH_PORT")
    SQL_IP             = environ.get("SQL_IP")
    # Database
    SQLALCHEMY_DATABASE_URI  = environ.get("SQLALCHEMY_DATABASE_URI")


