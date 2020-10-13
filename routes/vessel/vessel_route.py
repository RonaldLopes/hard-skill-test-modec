from flask import Blueprint
from flask import request, jsonify
from flask_cors import  cross_origin
from datetime import datetime
from pytz import timezone
import json

from models.vessel import Vessel

vessel_blueprint = Blueprint('vessels',__name__)

#
@vessel_blueprint.route('/vessels', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])

def create_vessel():
    """
        
    """''


    record = json.loads(request.data)
    print(request.args.get('name'))
    vessel = Vessel(code=record['code'])
    vessel.save()
    return jsonify(vessel.to_json()), 201


@vessel_blueprint.route('/vessels/<code>', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type','Authorization'])

def indexByCode(code):
    vessel = Vessel.objects(code=code).first()
    # print(vessel.id)
    if not vessel:
        return jsonify({'error': 'data not found'})
    else:
        return jsonify(vessel.to_json())


@vessel_blueprint.route('/vessels', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type','Authorization'])

def index():
    vessels =Vessel.objects()

    print(vessels)
    response = []
    for vessel in vessels:
        response.append(vessel.to_json())
    if not vessels:
        return jsonify({'error': 'data not found'})
    else:
        return jsonify(response)


@vessel_blueprint.route('/vessels/<code>', methods=['DELETE'])
@cross_origin(origin='*', headers=['Content-Type','Authorization'])
def deleteVessel(code):
    vessel = Vessel.objects(code=code).first()
    if not vessel:
        return jsonify({'error': 'data not found'}), 404
    else:
        try:
            vessel.delete()
            return jsonify(), 204
        except Exception as e:
            print(e)
    return jsonify(), 204

