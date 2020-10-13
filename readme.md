# MODEC DnA Hard skill test (Backend)



# The challenge

The main functionalities of this software are:
* Registering a vessel. The vessel data input is its code, which can’t be repeated (return the HTTP code appropriate and an
error message if the user tries to register a existing code). For instance, a valid input of a vessel is: “code”: “MV102”.
* Registering a new equipment in a vessel. The data inputs of each equipment are name, code, location and status. Each
equipment is associated to a given vessel and has a unique code, which can’t be repeated (return the HTTP code appropriate
and an error message if the user tries to register a existing code). For each new equipment registered, the equipment status is
automatically active. For instance, a valid input of a new equipment related to a vessel “MV102” is:
    > { "name": "compressor", "code": "5310B9D7", "location": "Brazil"}
* Setting an equipment’s status to inactive. The input data should be one or a list of equipment code.
* Returning all active equipment of a vessel

# The solution
The API was created with the Python language and the Flask framework, for data storage the MongoDB (NoSQL) database was used.

To register a new vessel, make an HTTP request (POST) for the route /vessels:

    curl --request POST \
      --url http://0.0.0.0:8899/vessels \
      --header 'content-type: application/json' \
      --data '{
        "code": "MV102"
    }'
    
To register a new equipment, make an HTTP request (POST) for the route /equipments, do not forget to pass the vessel ID to which this equipment is related, In this way, each  equipment will be associated with a vessel:

    curl --request POST \
      --url http://0.0.0.0:8899/equipments \
      --header 'content-type: application/json' \
      --data '{
        "name": "compressor",
        "code": "5310B9D7",
        "vessel": "5f85e0e0469aefd749e18cf7",
        "location": "Brazil"
    }'


To set a equipment's status to inactive, make an HTTP request (PATCH) for the route /equipments/deactivate, do not forget to pass the code of the equipment that must be disabled:
    
    curl --request PATCH \
      --url http://0.0.0.0:8899/equipments/deactivate \
      --header 'content-type: application/json' \
      --data '["5310B9D7"]'

To return all equipments of a vessel, make an HTTP request (GET) for the route /equipments/<ID>, do not forget to pass the vessel ID:
    
    curl --request GET --url http://0.0.0.0:8899/equipments/5f84af8e43b074aaba1ff86a
## Install the dependences
First, install the requirements for run this application, use the line below:

    pip install -r requirements.txt


## Run Tests
To run the tests, use the command below:

    python -m unittest discover  Tests/

## Run the code
To run the code, use the command below:

    python3 server.py
    
