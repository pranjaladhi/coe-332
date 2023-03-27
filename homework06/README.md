# Human Gene API  

## Purpose
This project develops a local Flask application to query and return information regarding human gene data. The data utilized in this project is supplied through the [HGNC website](https://www.genenames.org/download/archive/) and is stored [here](https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/json/hgnc_complete_set.json). Taking the data, a Flask application is developed that allows the user to make requests with five total routes.

A main objective of this project is to develop skills working with the Python Flask web framework and learn how to set up a REST API with multiple routes. Additionally, another object is to learn how to containerize the script with Docker for any user to utilize the script. Working with the Flask library will allow for the understanding of building web servers in a small scale and allow for familiarization in understanding how they are used.

## File Structure
The API is structured with two essential files *iss_tracker.py* and *Dockerfile*. The file *docker-compose.yml*, while not essential, can be utilized to run the program with preset configurations. 

### [genes.py](https://github.com/pranjaladhi/coe-332/blob/main/homework06/genes.py)
Processes all of the HTTP requests made to the API by the user. The functions within each route of the file return the requested data.

### [Dockerfile](https://github.com/pranjaladhi/coe-332/blob/main/homework06/Dockerfile)
Contains important commands for building the image to run the API within a container.

### [docker-compose.yml](https://github.com/pranjaladhi/coe-332/blob/main/homework06/docker-compose.yml)
Configures the application containers, which can then be created and ran with the configuration via a single command. 

## Running the Code

### Docker Setup
First, open two terminals. The first terminal will be used to utilize the image from Docker Hub, which will be pulled with the line:
> `docker pull pranjaladhikari/genes:1.0`

Next, to run the containerized Flask app, run the line:
> `docker run -it --rm -p <host port>:<container port> pranjaladhikari/genes:1.0`

The flag `-p` is used to bind a port on the container to a port on the machine that is running the script. For example, if the Flask application is running on the `<host port>` 5000, but the `<container port>` is not connected to port 5000, the Flask program won't be able to start and communicate with the machine.

If building a new image from the Dockerfile, both of the files *Dockerfile* and *iss_tracker.py* must be in the same directory. Afterward, the image can be built with the line:
> `docker build -t <username>/genes:<version> .`

where `<username>` is your Docker Hub username and `<version>` is the version tag. Then, it can be ran with the line:
> `docker run -it --rm -p <host port>:<container port> <username>/iss_tracker:<version>`

After pulling the image from the Docker Hub, the above processes of building and running can be simplified utilizing *docker-compose.yml*. This will automatically configure all options needed to start the container in a single file. Once the file is in the same directory as *Dockerfile* and *iss_tracker.py*, the container can be started with the line:
> `docker-compose up --build`

With the commands above of building and running the containerized Flask app, the server will be running. Now, the second terminal will be used for the HTTP requests to the API.

### Requests to the API
With the container running in the other terminal, the second terminal can be used for requests to the API. To start, run the line:
#### > `curl -X POST localhost:5000/data`

This request will restore/reload the gene data from the source (reverse of the route above). Here, the `-X POST` is required as the route accepts a `POST` method, and not the default `GET` method. This route will allow the user to run previous routes above as the ISS data has been reloaded. The output after running this request will be:
```
Data loaded in 
```


#### > `curl -X GET localhost:5000/data`

This request will restore/reload the gene data from the source (reverse of the route above). Here, the `-X POST` is required as the route accepts a `POST` method, and not the default `GET` method. This route will allow the user to run previous routes above as the ISS data has been reloaded. The output after running this request will be:
```
Successfully reloaded ISS data 
```

#### > `curl -X DELETE localhost:5000/data`

This will delete the human gene data gathered from the source. The `-X DELETE` is required as the route accepts a `DELETE` method, and not the default `GET` method. After running this request, the previous requests will result in error as the ISS data is no longer available for usage. The output of running this request will be:
```
Deleted ISS data
```

If any of the requests above are ran after running this deleted request, a 404 error will return with the message:
```
Data not loaded in
```

#### > `curl localhost:5000/genes`

This will return all hgnc_id data in the database. The output may look like: 
```
```

### > `curl localhost:5000/genes/<hgnc_id>`

Lastly, this request will return all data associated with `<hgnc_id>`. With `HGNC:xx` in the source....

