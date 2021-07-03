"""Routes for logged-in account pages."""
from flask import Blueprint, make_response, request, jsonify, current_app
from app.models.User import User
from app import routes, session_scope
from app.schemas.UserSchema import user_schema, users_schema

api_bp = Blueprint('api_bp', __name__,
                   template_folder='templates',
                   static_folder='static',
                   url_prefix='/api/v1.0')

headers = {"Content-Type": "application/json"}


@api_bp.route('/users', methods=['GET'])
def api_admin_users():
    """View users of the dashboard"""
    users = User.query.all()
    return make_response(users_schema.jsonify(users, many=True),
                         headers)


@api_bp.route("/users/<int:id>")
def api_admin_users_id(id):
    user = User.query.get(id)
    if user is None:
        return make_response(jsonify({'error': "Could not find user with id: {}".format(id)}), 404)
    return make_response(user_schema.jsonify(user),
                         headers)


