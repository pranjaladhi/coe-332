# Human Gene API  

## Purpose
This project develops a local Flask application to query and return information regarding human gene data. The data utilized in this project is supplied through the [HGNC website](https://www.genenames.org/download/archive/) and is stored [here](https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/json/hgnc_complete_set.json). Taking the data, a Flask application is developed that allows users to make requests with five total routes. The Flask application is used in conjunction with the Redis service to create a database, ensuring all gathered data is not lost in the event of the Flask application stopping.

Objectives of this project include developing skills working with the Python Flask web framework and Redis. Both services are powerful tools to set up REST APIs and to be used as a database to store data that the script uses. The project includes combining these two services to learn how they interact and are able to be integrated with one another. Lastly, Docker will be used to learn how to containerize the script with these services, allowing for any user to utilize this script built. In conclusion, these tools are powerful for developing small scale applications, and utilizing them in this project will allow for a better understanding of their functions and abilities.

## File Structure
The API is structured with two essential files *genes.py* and *Dockerfile*. The file *docker-compose.yml*, while not essential, can be utilized to run the program with preset configurations. 

### [genes.py](https://github.com/pranjaladhi/coe-332/blob/main/homework06/genes.py)
Processes all of the HTTP requests made to the API by the user. The functions within each route of the file returns the requested data by the user.

### [Dockerfile](https://github.com/pranjaladhi/coe-332/blob/main/homework06/Dockerfile)
Contains important commands for building the image to run the API within a container. Includes the installation of specific Python libraries that the script utilizes.

### [docker-compose.yml](https://github.com/pranjaladhi/coe-332/blob/main/homework06/docker-compose.yml)
Configures the application containers, which can then be created and ran with the configuration via a single command. Instructions to run the Redis service is also included, thus both Flask and Redis can be started utilizing this file.

## Running the Code

### Flask & Redis Setup
The API utilizes the Flask Python library and Redis NoSQL database to run the application and store the data used in a database. These two tools are required to run the API and can be installed by the line:
> `pip3 install --user flask && pip3 install redis`

The Python requests library is also utilized to fetch the data from the source website. It can be installed with the line:
> `pip3 install --user requests`

### Docker Setup
First, open two terminals. The first terminal will be used for Docker and to begin the services, and the second will be used for requests to the API. In the first terminal, the image for the application is required and can be pulled from Docker with the line:
> `docker pull pranjaladhikari/genes_app:1.0`

The next step is to start the Redis and Flask services, which can be done both manually with user preferences, or launched together automatically. 

#### Manual Setup
The Redis container will first have start. Before however, a `data` directory will have to be created first for the Redis database to store the gathered data. Afterwards, the Redis service can be ran with the line:
> `docker run -d -p 6379:6379 -v /data:/data:rw redis:7 --save 1 1`

The `-d` flag allows the container to run in the background. The `-p` flag is used to bind a port on the container to a port on the machine that is running the script. For example, if the appliation is running on a different port than the machine, the program will not be able to start and communiate with the machine. The `-v` flag mounts the data to the container and the `--save` flag is used to save the Redis database to the directory `data`.

Next, the containerized Flask app will have to start, which can be ran with the line:
> `docker run -it --rm -p <host port>:<container port> pranjaladhikari/genes_app:1.0`

The `-it` flag attaches the terminal inside to container for the user to interact with the container. The `--rm` flag ensures the container is removed after exiting the Flask application. The flag `-p` is the same as the `-p` flag exaplained above. For example, if the Flask application is running on the `<host port>` 5000, but the `<container port>` is not connected to port 5000, the Flask program won't be able to start and communicate with the machine.

* Sidenote: If building a new image from the Dockerfile, both of the files *Dockerfile* and *genes.py* must be in the same directory. Afterwards, the image can be built with the line: `docker build -t <username>/genes_app:<version> .` where `<username>` is your Docker Hub username and `<version>` is the version tag. Then, it can be ran with the line: `docker run -it --rm -p <host port>:<container port> <username>/genes_app:<version>`.

#### Launch Together
After pulling the image from the Docker Hub, the above processes of building and running the Flask and Redis services can be skipped by utilizing *docker-compose.yml*. This will automatically configure all options needed to start the containers. Once the file is in the same directory as *Dockerfile* and *genes.py*, both services can be started with the line:
> `docker-compose up`

With the commands above of building and running the containerized Flask and Redis services, the second terminal can be used for the HTTP requests to the API.

### Requests to the API
With the container running in the other terminal, the second terminal can be used for requests to the API.

#### > `curl -X POST localhost:5000/data`

This request will load the gene data from the source into the Redis database. Here, the `-X POST` is required as the method is a `POST`, and not the default `GET`. After running this request, it will allow the user to the requests below as the gene data has been loaded into the database. The output after running this request will be:
```
Data loaded in
```

#### > `curl -X GET localhost:5000/data`

This request will return all the gene data from the source. The `-X GET` is optional as the default route method is `GET`. The output after running this request will be:
```
.
.
.
{
    "_version_": 1761544681057943553,
    "agr": "HGNC:469",
    "alias_name": [
      "AMPD isoform L"
    ],
    "alias_symbol": [
      "SPG63"
    ],
    "ccds_id": [
      "CCDS804",
      "CCDS58016",
      "CCDS805"
    ],
    "date_approved_reserved": "1990-03-06",
    "date_modified": "2023-03-15",
    "date_name_changed": "2010-02-10",
    "ena": [
      "S47833"
    ],
    "ensembl_gene_id": "ENSG00000116337",
    "entrez_id": "271",
    "enzyme_id": [
      "3.5.4.6"
    ],
    "gencc": "HGNC:469",
    "gene_group": [
      "Adenosine deaminase family"
    ],
    "gene_group_id": [
      1302
    ],
    "hgnc_id": "HGNC:469",
    "location": "1p13.3",
    "location_sortable": "01p13.3",
    "locus_group": "protein-coding gene",
    "locus_type": "gene with protein product",
    "mane_select": [
      "ENST00000528667.7",
      "NM_001368809.2"
    ],
    "mgd_id": [
      "MGI:88016"
    ],
    "name": "adenosine monophosphate deaminase 2",
    "omim_id": [
      "102771"
    ],
    "orphanet": 376557,
    "prev_name": [
      "adenosine monophosphate deaminase 2 (isoform L)"
    ],
    "pubmed_id": [
      1400401,
      24482476
    ],
    "refseq_accession": [
      "NM_001257361"
    ],
    "rgd_id": [
      "RGD:2110"
    ],
    "status": "Approved",
    "symbol": "AMPD2",
    "symbol_report_tag": [
      "Stable symbol"
    ],
    "ucsc_id": "uc001dyc.3",
    "uniprot_ids": [
      "Q01433"
    ],
    "uuid": "fd40f6a5-1525-43d0-ad80-396fb52f9c87",
    "vega_id": "OTTHUMG00000011649"
  }
.
.
.
```

#### > `curl -X DELETE localhost:5000/data`

This will delete the human gene data gathered from the source. The `-X DELETE` is required as the route accepts a `DELETE` method, and not the default `GET` method. After running this request, any other requests made will result in error as the gene data is no longer available in the database. The output of running this request will be:
```
Data deleted
```

If any requests are ran after running this deleted request, a 404 error will return with the message:
```
Error. Data not loaded in
```

#### > `curl localhost:5000/genes`

This will return all hgnc_id data in the database. The output may look like: 
```
[
  "HGNC:5",
  "HGNC:234",
  .
  .
  .
  "HGNC:29027",
  "HGNC:24523"
]
```

#### > `curl localhost:5000/genes/<hgnc_id>`

Lastly, this request will return all data associated with `<hgnc_id>`. With `HGNC:13194` in the place of `<hgnc_id>`, the output will look like:
```
{
  "_version_": 1761544728371789824,
  "agr": "HGNC:13194",
  "alias_symbol": [
    "KNTC1AP"
  ],
  "ccds_id": [
    "CCDS8363"
  ],
  "date_approved_reserved": "1999-05-11",
  "date_modified": "2023-01-20",
  "date_name_changed": "2012-12-13",
  "ena": [
    "U54996"
  ],
  "ensembl_gene_id": "ENSG00000086827",
  "entrez_id": "9183",
  "gene_group": [
    "NRZ tethering complex",
    "RZZ complex"
  ],
  "gene_group_id": [
    1931,
    1933
  ],
  "hgnc_id": "HGNC:13194",
  "location": "11q23.2",
  "location_sortable": "11q23.2",
  "locus_group": "protein-coding gene",
  "locus_type": "gene with protein product",
  "mane_select": [
    "ENST00000200135.8",
    "NM_004724.4"
  ],
  "mgd_id": [
    "MGI:1349478"
  ],
  "name": "zw10 kinetochore protein",
  "omim_id": [
    "603954"
  ],
  "prev_name": [
    "ZW10 (Drosophila) homolog, centromere/kinetochore protein",
    "ZW10, kinetochore associated, homolog (Drosophila)"
  ],
  "pubmed_id": [
    9298984
  ],
  "refseq_accession": [
    "NM_004724"
  ],
  "rgd_id": [
    "RGD:1309197"
  ],
  "status": "Approved",
  "symbol": "ZW10",
  "ucsc_id": "uc001poe.4",
  "uniprot_ids": [
    "O43264"
  ],
  "uuid": "585ad64f-6281-44ea-9c55-df12909f77e5",
  "vega_id": "OTTHUMG00000168190"
}
```

### HGNC Data
The data used for this project is gathered from HGNC. It provides the names, symbols, and the associated data regarding the various types of human genes. This includes the protein products, gene families, and the date the gene name was last changed. The dataset is available for the public and can be found [here](https://www.genenames.org/download/archive/).