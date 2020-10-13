import flask
from flask import jsonify
from mongoengine import NotUniqueError
import json
error_handlers_blueprint = flask.Blueprint('error_handlers', __name__)

# @error_handlers_blueprint.app_errorhandler(500)
# def handle404(e):
#     return jsonify("The requested URL was not found on the server."), 404


@error_handlers_blueprint.app_errorhandler(404)
def handle404(e):
    return jsonify("The requested URL was not found on the server."), 404


@error_handlers_blueprint.app_errorhandler(Exception)
def handleException(e):
    if type(e) == NotUniqueError:
        return jsonify((e.args)), 409
    print(e)
    return jsonify("Internal server error 2"), 500
