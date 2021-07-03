"""Route declaration."""
from flask import current_app as app, request, render_template
from datetime import timedelta
from flask_session import Session
from app import session_scope


@app.before_request
def before_request():
    session = Session()
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=int(app.config["SESSION_TIMEOUT"]))

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html',error=error), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html',error=error), 500