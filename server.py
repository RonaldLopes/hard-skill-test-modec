'''
todo: Implementar medidas de segurança
'''

import os
from flask import Flask, request, jsonify
from flask_cors import CORS

from middlewares.error_handler import error_handlers_blueprint
from routes import db
from routes.equipment.equipment_route import equipment_blueprint
from routes.vessel.vessel_route import vessel_blueprint
import middlewares.error_handler

app = Flask('Python challenge')

app.config['MONGODB_SETTINGS'] = {
    'db': 'challengeDB',
    'host': 'localhost',
    'port': 27017
}
# db = MongoEngine()
db.init_app(app)
CORS(app, expose_headers=["Content-Type", "Authorization", "Access-Control-Allow-Credentials"], supports_credentials=True)
app.config['CORS_HEADERS'] = 'Content-Type'
# app.register_blueprint(time_blueprint)
app.register_blueprint(vessel_blueprint)
app.register_blueprint(equipment_blueprint)
app.register_blueprint(error_handlers_blueprint)

# app.wsgi_app = middleware(app.wsgi_app)

port = int(os.environ.get('PORT', 8899))

if __name__ == '__main__':
    # app.run(threaded=True, host='0.0.0.0', port=port) #,ssl_context='adhoc'
    app.run(threaded=True, host='0.0.0.0',port=port)

