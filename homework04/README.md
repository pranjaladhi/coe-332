# Tracking (Stalking) the International Space Station

### Purpose
One of the goals of this project is to develop a Flask application to query and return information regarding the position and velocity of the International Space Station (ISS) at a given time. The data of the ISS is supplied through the [NASA](https://spotthestation.nasa.gov/trajectory_data.cfm) website and is stored [here](https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml), a XML data set. Taking the data, a Flask application is developed that exposes the data to the user by four different routes with the user's input, all done within the file *stalk_iss.py*. A main objective of this project is to develop skills working with the Python Flask web framework and learn how to setup a REST API with multiple routes (URLs). Furthermore, `curl` will be utilized to learn and test the routes defined in the Flask program, when the local Flask development server is running. Working with the Flask library will allow for the understanding of building web servers and allow for fimiliarization in understanding how they are used.

### Code Scripts
In the *stalk_iss.py* file, lines 15-25 `@app.route('/', methods = ['GET'])...` defines the URL `/` within the application. It takes an argument `methods` which is list of string containing the HTTP method `GET`. When the URL + HTTP combination is requested, the Python function below `def data_set()...` is called which returns the entire ISS data set in the XML file. In lines 27-41 `@app.route('/epochs', methods = ['GET'])...` the URL `/epochs` is requested, from which the function returns a list of all EPOCHs in the data set. In lines 39-40
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
						the x, y, and z components of the ISS is extracted to compute the instantaneous speed at time `<epoch>`.


### Running the Code
First, the source file of *stalk_iss.py* must be placed in a directory. Next, the 'requests' library will need to be installed in the top level directory, which is done by the line:
> pip3 install --user requests

Next, the 'xmltodict' library is needed in the same top level directory, installed by the line:
> pip3 install --user xmltodict

Lastly, the 'flask' library will be needed, installed by the line:
> pip3 install --user flask

After the installations, another terminal will be useful to run the Flask application in one, and test it on the other. In one of the terminals, in the same directory as the *stalk_iss.py* file, run the Flask application with the line:
> flask --app stalk_iss --debug run

This will begin the Flask application and the server will be running. In the other terminal, in the same directory, enter the line:
> curl localhost:5000/

This will make a request to the Flask app, with the route `/`. This will return the entire ISS data set and an example output may look like:
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

Next in the same terminal, run the line:
> curl localhost:5000/epochs

This will return all the EPOCHs data. The output may look like:
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

Furthermore, running the line:
> curl localhost:5000/epochs/<epoch>

with 2023-063T12:00:00.000Z in the place of <epoch> may result in the output of:
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

Lastly, running the line:
> curl localhost:5000/epochs/<epoch>/speed

with 2023-063T12:00:00.000Z in place of <epoch> may output with:
```
{
  "Speed of EPOCH": 7.661757196327827
  }