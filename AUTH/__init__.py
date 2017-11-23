from flask import Blueprint

AUTH = Blueprint('AUTH', __name__)

from . import views