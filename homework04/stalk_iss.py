#Pranjal Adhikari pa8729

from flask import Flask
import requests
import xmltodict
from math import sqrt

r = requests.get('https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml')

iss_data = xmltodict.parse(r.text) #converting xml data to dictionary

app = Flask(__name__)


@app.route('/', methods = ['GET'])
def data_set():
    return iss_data


@app.route('/epochs', methods = ['GET'])
def all_epochs():
    epochs = []
    data = data_set()
    for i in range(len(data['ndm']['oem']['body']['segment']['data']['stateVector'])):
        epochs.append(data['ndm']['oem']['body']['segment']['data']['stateVector'][i]['EPOCH'])
    return epochs


@app.route('/epochs/<epoch>', methods = ['GET'])
def vectors(epoch):
    data = data_set()
    for i in range(len(data['ndm']['oem']['body']['segment']['data']['stateVector'])):
        if (data['ndm']['oem']['body']['segment']['data']['stateVector'][i]['EPOCH'] == epoch):
            state_vectors = []
            state_vectors.append(data['ndm']['oem']['body']['segment']['data']['stateVector'][i])
            return state_vectors
        
@app.route('/epochs/<epoch>/speed', methods = ['GET'])
def epoch_speed(epoch):
    data = vectors(epoch)
    speed = {}
    sumSpeedSquare = pow(float(data[0]['X_DOT']['#text']), 2) + pow(float(data[0]['Y_DOT']['#text']), 2) + pow(float(data[0]['Z_DOT']['#text']), 2)
    speed['Speed of EPOCH'] = (sqrt(sumSpeedSquare))
    return speed

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')
