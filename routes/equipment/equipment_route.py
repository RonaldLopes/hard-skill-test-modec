from flask import Blueprint
from flask import request, jsonify, abort
from flask_cors import  cross_origin
from datetime import datetime

from mongoengine import NotUniqueError
from pytz import timezone
import json

from models.equipment import Equipment
from pymongo import errors
equipment_blueprint = Blueprint('equipments',__name__)

#
@equipment_blueprint.route('/equipments', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])

def create_vessel():
    """
        
    """''

    record = json.loads(request.data)
    name, code, location, status, vessel = (record['name'] if "name" in record.keys() else None), (record['code'] if "code" in record.keys() else None), (record['location'] if "location" in record.keys() else None),(record['status'] if "status" in record.keys() else None), (record['vessel'] if "vessel" in record.keys() else None)
    equipment = Equipment(name=name, code=code,location=location,status= vessel, vessel= vessel)
    equipment.save()
    return jsonify(equipment.to_json()), 201



@equipment_blueprint.route('/equipments/<vessel>', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type','Authorization'])

def index(vessel):
    equipments = Equipment.objects(vessel=vessel)
    print(equipments)
    response = []
    for equipment in equipments:
        response.append(equipment.to_json())
    if not equipments:
        return jsonify({'error': 'data not found'})
    else:
        return jsonify(response)



@equipment_blueprint.route('/equipments/deactivate', methods=['PATCH'])
@cross_origin(origin='*', headers=['Content-Type','Authorization'])

def deactivateEquipment():
    listOfEquipments = json.loads(request.data)

    if not listOfEquipments: return jsonify({'error': 'data not found'}), 404

    for equipment in listOfEquipments:
        equipments_doc = Equipment.objects(code=equipment).first()
        if not equipments_doc:
            return jsonify({'error': 'data not found'}), 404
        else:
            equipments_doc.update(status=False)
        return jsonify(equipments_doc.to_json())


@equipment_blueprint.route('/equipments/<code>', methods=['DELETE'])
@cross_origin(origin='*', headers=['Content-Type','Authorization'])
def deleteVessel(code):
    equipment = Equipment.objects(code=code).first()
    if not equipment:
        return jsonify({'error': 'data not found'}), 404
    else:
        try:
            equipment.delete()
            return jsonify(), 204
        except Exception as e:
            print(e)
    return jsonify(), 204

