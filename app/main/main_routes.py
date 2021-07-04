"""Routes for main pages."""
import json

from flask import Blueprint, render_template, current_app, request, url_for, redirect

from app.api.api_routes import api_bp, api_video_actions, api_video_time_user_id, api_video_times
from app import routes, session_scope
from flask import Flask

main_bp = Blueprint('main_bp', __name__,
                    template_folder='templates',
                    static_folder='static')


@main_bp.before_request
def before_request():
    routes.before_request()

@main_bp.route('/', methods=['GET'])
@main_bp.route("/home", methods=['GET'])
@main_bp.route("/index", methods=['GET'])
@main_bp.route("/login", methods=['GET'])
def home():
    return render_template('welcome.html')


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

@main_bp.route('/get_video_actions', methods=['GET'])
def get_video_actions():
    """
    Renders the video_actions template using the results of the equivalent api call
    Takes three optional request parameters, action, start_time and end_time.

    :param action:
        Can be "start" or "stop". Any other value is ignored and actions of all types are returned
    :param start_time:
        An integer. Defaults to 0
    :param end_time:
        An integer.
    """
    return render_template('video_actions.jinja2',
                           title='Video actions',
                           body="Find users' video actions",
                           results=api_video_actions().get_json())


@main_bp.route('/get_video_times', methods=['GET'])
def get_video_times():
    """
    Renders the video_times template using the results of the equivalent api call
    """
    return render_template('video_times.jinja2',
                           title='Video watch time',
                           body="Find a user's total video time",
                           results=api_video_times().get_json())


@main_bp.route('/get_video_times/<int:user_id>', methods=['GET'])
def get_video_time_user_id(user_id=1):
    """
    Renders the video_times template using the results of the equivalent api call.
    Gets the duration for the given user_id

    :param user_id:
        An integer
    """
    return render_template('video_times.jinja2',
                           title='Video watch time',
                           body="Find a user's total video time",
                           results=[api_video_time_user_id(user_id).get_json()])

########### JINJA FILTERS

def slice_string_filter(s,_from=0,_to=None):
    return s[_from:_to]
current_app.jinja_env.filters['slice_string'] = slice_string_filter


def from_json_filter(x):
    return json.loads(x)
current_app.jinja_env.filters['from_json'] = from_json_filter