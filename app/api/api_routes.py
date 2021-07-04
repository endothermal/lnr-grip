from flask import Blueprint, make_response, request, jsonify

from app.models.UsersVideoDuration import UsersVideoDuration
from app.models.VideoAction import VideoAction
from app.models.User import User
from app.schemas.UserSchema import user_schema, users_schema
from app.schemas.UsersVideoDuration import users_video_duration_schema, users_video_durations_schema
from app.schemas.VideoActionSchema import video_actions_schema

api_bp = Blueprint('api_bp', __name__,
                   template_folder='templates',
                   static_folder='static',
                   url_prefix='/api/v1.0')

headers = {"Content-Type": "application/json"}


@api_bp.route('/users', methods=['GET'])
def api_users():
    """View users"""
    users = User.query.all()
    return make_response(users_schema.jsonify(users, many=True),
                         headers)


@api_bp.route("/users/<int:id>", methods=['GET'])
def api_users_id(id):
    user = User.query.get(id)
    if user is None:
        return make_response(jsonify({'error': "Could not find user with id: {}".format(id)}), 404)
    return make_response(user_schema.jsonify(user),
                         headers)


@api_bp.route("/video_actions", methods=['GET'])
def api_video_actions():
    """
    Gets the video actions from the DB and pops them into a json response.
    Takes three optional request parameters, action, start_time and end_time.

    :param action:
        Can be "start" or "stop". Any other value is ignored and actions of all types are returned
    :param start_time:
        An integer. Defaults to 0
    :param end_time:
        An integer.
    """
    start_time = request.args.get('start_time', default=0, type=int)
    end_time = request.args.get('end_time', default=None, type=int)
    action = request.args.get('action', default=None, type=str)
    q = VideoAction.query.filter(VideoAction.date_actioned >= start_time)
    if action is not None:
        if action.lower() in ["start","stop"]:
            q = q.filter_by(action=action.lower())
    if end_time is not None:
        q = q.filter(VideoAction.date_actioned < end_time)
    video_actions = q.all()
    return make_response(video_actions_schema.jsonify(video_actions, many=True),
                         headers)


@api_bp.route('/video_times', methods=['GET'])
def api_video_times():
    """
    Returns all users video durations as a json response
    """
    durations = UsersVideoDuration.query.all()
    return make_response(users_video_durations_schema.jsonify(durations, many=True),
                         headers)


@api_bp.route("/video_times/<int:user_id>", methods=['GET'])
def api_video_time_user_id(user_id):
    """
    Returns the video durations for the given user_id as a json response

    :param user_id:
        An integer.
    """
    duration = UsersVideoDuration.query.get(user_id)
    if duration is None:
        return make_response(jsonify({'error': "Could not find user video duration with user id: {}".format(user_id)}), 404)
    return make_response(users_video_duration_schema.jsonify(duration),
                         headers)

def get_dicts():
    """
    Returns the dicts as per the question sheet
    """
    apps = [{"app_id": 1}, {"app_id": 2}, {"app_id": 3}, {"app_id": 126}]
    app_features = [{"app_id": 1, "features_available": [1, 2, 3]},
                    {"app_id": 2, "features_available": [3, 4, 5, 7]},
                    {"app_id": 3, "features_available": [3, 12]}]
    user_features = [{"user_id": 1, "features_allowed": [1, 2, 5]},
                     {"user_id": 2, "features_allowed": [1, 2, 3, 4,]},
                     {"user_id": 3, "features_allowed": []}]
    return apps, app_features, user_features

def parse_dicts(user_id):
    """
    Returns a dict of the features per app that a user has permissions for

    :param user_id:
        An integer.
    """
    apps, app_features, user_features = get_dicts()
    result={"user_id":user_id,
            "application_permissions":[]}
    #1. Fill in the gaps. Make sure app_features includes all apps
    for a in apps:
        if a["app_id"] not in [af["app_id"] for af in app_features]:
            app_features.append({"app_id": a["app_id"], "features_available": []})

    #2. Get the user's allowed features
    user_allowed_features=set()
    for uf in user_features:
        if uf["user_id"] == user_id:
            user_allowed_features = set(uf["features_allowed"])

    #3. Find all the common features
    for af in app_features:
        features_allowed=list(user_allowed_features.intersection(af["features_available"]))
        result["application_permissions"].append({"app_id":af["app_id"],
                                             "features_allowed":features_allowed})

    return result


@api_bp.route("/user_app_permissions/<int:user_id>", methods=['GET'])
def api_user_app_permissions(user_id):
    """
    Checks the user exists then returns their permitted features per-app as a json response

    :param user_id:
        An integer.
    """
    perms = parse_dicts(user_id)
    user = User.query.get(user_id)
    if user is None:
        return make_response(jsonify({'error': "Could not find user with id: {}".format(user_id)}), 404)
    if perms is None:
        return make_response(jsonify({'error': "Could not find user app permissions for user id: {}".format(user_id)}), 404)
    return make_response(jsonify(perms), headers)