# Tracking the International Space Station 

### Purpose
One of the goals of this project is to develop a Flask application to query and return information regarding the position and velocity of the International Space Station (ISS) at a given time. The data of the ISS is supplied through the [NASA](https://spotthestation.nasa.gov/trajectory_data.cfm) website and is stored [here](https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml), a XML data set. Taking the data, a Flask application is developed that exposes the data to the user by eight different routes with the user's input, all done within the file *iss_tracker.py*. A main objective of this project is to develop skills working with the Python Flask web framework and learn how to setup a REST API with multiple routes (URLs). Additionally, another object is to learn how to containerize the script with Docker for any user to utilize the script. Working with the Flask library will allow for the understanding of building web servers and allow for fimiliarization in understanding how they are used. Furthermore, learning how to containerize will allow for the sharing of programs to other users.

### Code Scripts
In the *iss_tracker.py* file, lines 15-25 `@app.route('/', methods = ['GET'])...` defines the URL `/` within the application. It takes an argument `methods` which is list of string containing the HTTP method `GET`. When the URL + HTTP combination is requested, the Python function below `def data_set()...` is called which returns the entire ISS data set in the XML file. In lines 27-41 `@app.route('/epochs', methods = ['GET'])...` the URL `/epochs` is requested, from which the function returns a list of all EPOCHs in the data set. In lines 39-40
```
for i in range(len(data['ndm']['oem']['body']['segment']['data']['stateVector'])):
        epochs.append(data['ndm']['oem']['body']['segment']['data']['stateVector'][i]['EPOCH'])
```
the loop iterates through the `stateVector` list and extracts all values with the key `EPOCH`. Next, in lines 43-58 `@app.route('/epochs/<epoch>', methods = ['GET'])...` the URL `/epochs/<epoch>` is requested, with `<epoch>` being input by the user. This will call the function `def vectors(epoch: str) -> list:...` and return the state vectors for the specific `<epoch>`. This is performed in lines 55-58
```
if (data['ndm']['oem']['body']['segment']['data']['stateVector'][i]['EPOCH'] == epoch):
            state_vectors = []
            state_vectors.append(data['ndm']['oem']['body']['segment']['data']['stateVector'][i])
            return state_vectors
```
where the `if (data['ndm']...` function will gather and return the state vector data if the iterated `['EPOCH']` matches the user input of `<epoch>`. Lastly from lines 60-74, `@app.route('/epochs/<epoch>/speed', methods = ['GET'])...` the speed of the ISS is returned with the user input of `<epoch>`. In line 70
```
data = vectors(epoch)
```
the function will first call the `def vectors(epoch: str) -> list:...` function (in line 44) to gather the state vector in the specified `<epoch>`. Then, in lines 72-73
```
sumSpeedSquare = pow(float(data[0]['X_DOT']['#text']), 2) + pow(float(data[0]['Y_DOT']['#text']), 2) + pow(float(data[0]['Z_DOT']['#text']), 2)
    speed['Speed of EPOCH'] = (sqrt(sumSpeedSquare))
```
the x, y, and z components of the ISS is extracted to compute the instantaneous speed at time `<epoch>`. In lines 99-103 `@app.route('/delete-data', methods = ['DELETE'])...` route will delete the ISS data stored in the global `iss_data` dictionary. This will result in the previous routes not working as the data is not available anymore. However, the data can be restored with the route in lines 106-111 `@app.route('/post-data', methods = ['POST'])...`, which will allow for the previous routes to function properly again.

### Running the Code
First, open two terminals. The first terminal will be used to utilize the the image from Docker Hub, which will be pulled with the line:
> `docker pull pranjaladhikari/iss_tracker:hw05`

Next, to run the containerized Flask app, run the line:
> `docker run -it --rm -p <host port>:<container port> pranjaladhikari/iss_tracker:hw05`

The flag `-p` is used to bind a port on the container to a port on the machine that is running the script. For example, if the Flask application is running on the port 5000, if the <container port> is not connected to port 5000 as well, then the Flask program won't be able to communicate with the machine.

If building a new image from the Dockerfile, both of the files *Dockerfile* and *iss_tracker.py* will need to be in the same directory. Afterwards, the image can be built with the line:
> `docker build -t <username>/iss_tracker:<version> .`

where <username> is your Docker Hub username. Afterwards, it can be ran with the line:
> `docker run -it --rm -p <host port>:<container port> <username>/iss_tracker:<version>`

After building and running the containerized Flask app in the first terminal, the server will be running. Now, the second terminal will be used for the API query commands. To start, run the line:
> `curl localhost:5000/help'

This will output brief descriptions of all the available routes in the API. An example may look like:
```
Usage: curl 'localhost:5000[OPTIONS]'                                                                                                                      Options:                                                                                                                                                           1. /                                   returns entire ISS data set                                                                                         2. /epochs                             returns list of all EPOCHs                                                                                         3. /epochs?limit=<int>&offset=<int>    returns modified list of EPOCHs given query parameters of limit and offset                                         4. /epochs/<epoch>                     returns state vectors for a specified EPOCH                                                                         5. /epochs/<epoch>/speed               returns instantaneous speed for specified EPOCH                                                                     6. /delete-data                        deletes all data stored in the ISS data set dictionary                                                             7. /post-data                          reloads the ISS data set from the web into the dictionary object
```

The first route will make a request to the Flask app to return the entire ISS data set. It can be ran with the line:
> `curl localhost:5000/`

An example output may look like:
```
.
.
.

                },
                "Z": {
                  "#text": "1652.0698653803699",
                  "@units": "km"
                },
                "Z_DOT": {
                  "#text": "-5.7191913150960803",
                  "@units": "km/s"
                }
              }
            ]
          },
          "metadata": {
            "CENTER_NAME": "EARTH",
            "OBJECT_ID": "1998-067-A",
            "OBJECT_NAME": "ISS",
            "REF_FRAME": "EME2000",
            "START_TIME": "2023-048T12:00:00.000Z",
            "STOP_TIME": "2023-063T12:00:00.000Z",
            "TIME_SYSTEM": "UTC"
          }
        }
      },
      "header": {
        "CREATION_DATE": "2023-049T01:38:49.191Z",
        "ORIGINATOR": "JSC"
      }
    }
  }
}
```

Next, the second route will return all the EPOCHs data, and can be ran with the line:
> `curl localhost:5000/epochs`

The output may look like: 
```
.
.
.
  "2023-063T11:51:00.000Z",
  "2023-063T11:55:00.000Z",
  "2023-063T11:59:00.000Z",
  "2023-063T12:00:00.000Z"
]
```

Furthermore, the user has the ability to input query parameters for how many and which EPOCHs to return. It can be ran with the line:
> `curl 'localhost:5000/epochs?limit=<int>&offset=<int>'`

The user can input values in place of `<int>`. An example output for `limit=2&offset=4` may look like:
```
[
 "2023-058T12:16:00.000Z",
 "2023-058T12:20:00.000Z"
]   

Furthermore, running the line:
> `curl localhost:5000/epochs/<epoch>`

with '2023-063T12:00:00.000Z' in the place of `<epoch>` may result in the output of:
```
[
  {
    "EPOCH": "2023-063T12:00:00.000Z",
    "X": {
      "#text": "2820.04422055639",
      "@units": "km"
    },
    "X_DOT": {
      "#text": "5.0375825820999403",
      "@units": "km/s"
    },
    "Y": {
      "#text": "-5957.89709645725",
      "@units": "km"
    },
    "Y_DOT": {
      "#text": "0.78494316057540003",
      "@units": "km/s"
    },
    "Z": {
      "#text": "1652.0698653803699",
      "@units": "km"
    },
    "Z_DOT": {
      "#text": "-5.7191913150960803",
      "@units": "km/s"
    }
  }
]
```

The user also has the ability to output the speed of a specific EPOCH with the line:
> `curl localhost:5000/epochs/<epoch>/speed`

With '2023-063T12:00:00.000Z' in place of `<epoch>`, the output may be:
```
{
  "Speed of EPOCH": 7.661757196327827
}

If the user wanted to delete all ISS data gathered from the source, they can do so with the line:
> `curl -X DELETE localhost:5000/delete-data`

The `-X DELETE` is required as the route accepts a `DELETE` method, and not the default `GET` method. After running this route, the previous routes will result in error as the ISS data is no longer available for usage. 

Lastly, if the user wanted to restore/reload the ISS data (reverse of the route above), it can be done so with the line:
> `curl -X POST localhost:5000/post-data`

Here, the `-X POST` is required as the route accepts a `POST` method, and not the default `GET` method. This route will allow the user to run previous routes above as the ISS data has been reloaded.
