from server import app


import unittest
import json

class TestVesselRoute(unittest.TestCase):

    '''
      Tests to check CRUD operations at the vessel endpoint
    '''


    def test_get_all(self):
        application = app.test_client()
        response = application.get('/vessels')
        self.assertEqual(200, response.status_code, msg=("Error when trying to list all Vessels, should be 200 but get " + str(response.status_code)))

    def test_response_content_type(self):
        # print(self.response.content_type)
        application = app.test_client()
        response = application.get('/vessels')
        self.assertEqual("application/json", response.content_type)

    def test_create_vessel(self):
        application = app.test_client()
        response = application.post('/vessels', data=json.dumps({"code": "MVTEST"}),content_type='application/json')
        self.assertEqual(201, response.status_code,msg=("Error when trying to create a Vessel, should be 201 but get " + str(response.status_code)))

    def test_delete_vessel(self):
        application = app.test_client()
        response = application.delete('/vessels/MVTEST')
        self.assertEqual(204, response.status_code,msg=("Error when trying to delete a Vessel, should be 204 but get " + str(response.status_code)))



if __name__ == '__main__':
    unittest.main()