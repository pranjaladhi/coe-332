#Pranjal Adhikari pa8729

from flask import Flask, request
import requests
import xmltodict
from math import sqrt

r = requests.get('https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml')
iss_data = xmltodict.parse(r.text)

app = Flask(__name__)


@app.route('/', methods = ['GET'])
def data_set():
    """
    Outputs the entire ISS Trajectory Data found on the NASA website.

    Args:
        none
    Returns:
        iss_data (dictionary): ISS data set
    """
    return iss_data

@app.route('/epochs/<epoch>', methods = ['GET'])
def vectors(epoch: str) -> list:
    """
    Outputs the state vectors for the specified EPOCH from the data set.
    
    Args:
        epoch (str): specified EPOCH time stamp
    Returns:
        state_vectors (list): state vectors of the specified EPOCH
    """
    data = data_set()
    for i in range(len(data['ndm']['oem']['body']['segment']['data']['stateVector'])):
        if (data['ndm']['oem']['body']['segment']['data']['stateVector'][i]['EPOCH'] == epoch):
            state_vectors = []
            state_vectors.append(data['ndm']['oem']['body']['segment']['data']['stateVector'][i])
            return state_vectors

#'localhost:5000/epochs?limit=int&offset=int'
@app.route('/epochs', methods = ['GET'])
def modified_epoch():
    data = data_set()
    num_epochs = request.args.get('limit', len(data['ndm']['oem']['body']['segment']['data']['stateVector']))
    start = request.args.get('offset', 0)
    if num_epochs:
        try:
            num_epochs = int(num_epochs)
        except ValueError:
            return "Limit must be an integer"
    if start:
        try:
            start = int(start)
        except ValueError:
            return "Start must be an integer"
    end = start + num_epochs
    epochs = []
    while start < end:
        epochs.append(data['ndm']['oem']['body']['segment']['data']['stateVector'][start]['EPOCH'])
        start += 1
    return epochs
        
@app.route('/epochs/<epoch>/speed', methods = ['GET'])
def epoch_speed(epoch: str) -> dict:
    """
    Calculates the speed of the ISS in the specified EPOCH utilizing the x, y, and z components of speed.
    
    Args:
        epoch (str): specified EPOCH time stamp
    Returns:
        speed (dict): the speed of the ISS at the specified EPOCH
    """
    data = vectors(epoch)
    speed = {}
    sumSpeedSquare = pow(float(data[0]['X_DOT']['#text']), 2) + pow(float(data[0]['Y_DOT']['#text']), 2) + pow(float(data[0]['Z_DOT']['#text']), 2)
    speed['Speed of EPOCH'] = (sqrt(sumSpeedSquare)) #magnitude of speed utilizing the x, y, and z components of speed
    return speed

@app.route('/delete-data', methods = ['DELETE'])
def del_data():
    global iss_data
    iss_data.clear()
    return 'Deleted ISS data\n'

@app.route('/post-data', methods = ['POST'])
def retrieve_data():
    global iss_data
    r = requests.get('https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml')
    iss_data = xmltodict.parse(r.text)
    return 'Successfully reloaded data\n'

@app.route('/help', methods = ['GET'])
def define_routes():
    return 'Usage:'

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')
