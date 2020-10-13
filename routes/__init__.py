from flask_mongoengine import MongoEngine
from models.vessel import Vessel
from models.equipment import Equipment
db = MongoEngine()
# db.register_connection()
# from mongoengine. import ValidationError