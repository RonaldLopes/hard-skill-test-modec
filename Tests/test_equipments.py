import unittest


import json

from server import app


class TestEquipmentRoute(unittest.TestCase):

    '''
      Tests to check CRUD operations at the vessel endpoint
    '''
    vesselID=""
    equipmentID=""
    def test_create_equipments(self):
        application = app.test_client()
        # Create a temporary vessel for the tests
        response = application.post('/vessels', data=json.dumps({"code": "MVTEST"}), content_type='application/json')
        self.assertEqual(201, response.status_code, msg=("Error when trying to create a vessel, should be 201 but get "+ str(response.status_code)))

        #Create a new equipment
        response = application.post('/equipments', data=json.dumps({"code": "5310B9D7",	"name": "compressor","vessel": str(self.__class__.vesselID)}), content_type='application/json')
        self.assertEqual(201, response.status_code,msg=("Error when trying to create a equipment, should be 201 but get "+ str(response.status_code)))
        self.__class__.vesselID= json.loads(response.data)["id"]

    def test_get_equipments_by_vessel(self):
        application = app.test_client()
        # Get Equipments
        response = application.get('/equipments/'+str(self.__class__.vesselID))
        self.assertEqual(200, response.status_code, msg=("Error when trying get the equipments, should be 200 but get "+ str(response.status_code)))

    def test_deactivate_equipment(self):
        application = app.test_client()
        response = application.patch('/equipments/deactivate', data=json.dumps(["5310B9D7"]), content_type='application/json')
        #Check if the request is OK
        self.assertEqual(200, response.status_code, msg=("Error when trying to deactivate a equipment, should be 201 but get " + str(response.status_code)))
        #Check if the equipment has been deactivated
        self.assertEqual("False", str(json.loads(response.data)["status"]), msg=("Error when trying check the status, should be False but get " + str(json.loads(response.data)["status"])))

    def test_delete_equipment_and_vessel(self):
        application = app.test_client()
        response = application.delete('/equipments/5310B9D7')
        self.assertEqual(204, response.status_code, msg=("Error when trying to delete the equipment, should be 200 but get "+ str(response.status_code)))
        response = application.delete('/vessels/MVTEST')
        self.assertEqual(204, response.status_code, msg=("Error when trying to delete the vessel, should be 200 but get "+ str(response.status_code)))



if __name__ == '__main__':
    unittest.main()