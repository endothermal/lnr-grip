"""Routes for main pages."""
import json

from flask import Blueprint, render_template, current_app

from app.api.api_routes import api_bp
from app import routes
from flask import Flask

main_bp = Blueprint('main_bp', __name__,
                    template_folder='templates',
                    static_folder='static')


@main_bp.before_request
def before_request():
    routes.before_request()

@main_bp.route('/', methods=('GET', 'POST'))
@main_bp.route("/home", methods=('GET', 'POST'))
@main_bp.route("/index", methods=('GET', 'POST'))
@main_bp.route("/login", methods=('GET', 'POST'))
def home():
    return render_template('welcome.html',
                           title='Hello World',
                           body="This is where the info will go")


def get_bp_urls(blueprint):
    temp_app = Flask(__name__)
    temp_app.register_blueprint(blueprint)
    return [str(p) for p in temp_app.url_map.iter_rules() if "static" not in str(p)]


@main_bp.route('/api', methods=['GET'])
def api():
    return render_template('api.jinja2',
                           title='API info',
                           body="API information",
                           api_urls=get_bp_urls(api_bp))



########### JINJA FILTERS

def slice_string_filter(s,_from=0,_to=None):
    return s[_from:_to]
current_app.jinja_env.filters['slice_string'] = slice_string_filter


def from_json_filter(x):
    return json.loads(x)
current_app.jinja_env.filters['from_json'] = from_json_filter