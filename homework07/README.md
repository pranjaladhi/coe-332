# Human Gene API with Kubernetes  

## Purpose
This project builds upon [homework06](https://github.com/pranjaladhi/coe-332/tree/main/homework06), but the application now has the ability to be deployed utilizing a Kubernetes (K8) cluster. The data utilized in this project is supplied through the [HGNC website](https://www.genenames.org/download/archive/) and is stored [here](https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/json/hgnc_complete_set.json). Taking the data, the application is developed utilizing the same cocepts as the previous assignment, but applying Kubernetes allows for the data to be saved periodically in the case the application stops in any way.

A main objective of this project is to learn how to implement Kubernetes with Flask and Redis. Utilizing Kubernetes is important as it allows for the continuation of a container running, even if it fails or stops suddenly. Working with tools such as Kubernetes will allow for a better understanding of its functions and abilities to be incorporated alongside other tools. 

## File Structure
The API is structured with two essential files *genes.py* and *Dockerfile*. The file *docker-compose.yml*, while not essential, can be utilized to run the program with preset configurations. 

### [genes.py](https://github.com/pranjaladhi/coe-332/blob/main/homework06/genes.py)
Processes all of the HTTP requests made to the API by the user. The functions within each route of the file returns the requested data by the user.

### [Dockerfile](https://github.com/pranjaladhi/coe-332/blob/main/homework06/Dockerfile)
Contains important commands for building the image to run the API within a container. Includes the installation of specific Python libraries that the script utilizes.

### [docker-compose.yml](https://github.com/pranjaladhi/coe-332/blob/main/homework06/docker-compose.yml)
Configures the application containers, which can then be created and ran with the configuration via a single command. Instructions to run the Redis service is also included, thus both Flask and Redis can be started utilizing this file.

### [gene-flask-deployment.yml](https://github.com/pranjaladhi/coe-332/blob/main/homework07/gene-flask-deployment.yml)
Contains two pods which includes the Docker container needed for the Flask app.

### [gene-flask-service.yml](https://github.com/pranjaladhi/coe-332/blob/main/homework07/gene-flask-service.yml)
Routes the HTTPS requests made to the API with the route 5000.

### [gene-redis-pvc.yml](https://github.com/pranjaladhi/coe-332/blob/main/homework07/gene-redis-pvc.yml)
Contains the setup of a PVC (persistent volume claim) which periodically saves data in the Redis database.

### [gene-redis-deployment.yml](https://github.com/pranjaladhi/coe-332/blob/main/homework07/gene-redis-deployment.yml)
Allows the pod to run the Redis database continuously without interruptions.

### [gene-redis-service.yml](https://github.com/pranjaladhi/coe-332/blob/main/homework07/gene-redis-service.yml)
Communicates via port 6379 to create a bridge between the Flask application and the Kubernetes pods that runs the Redis database.

## Running the Code
Instructions to run the API utilizing Flask & Redis along with Docker can be found [here](https://github.com/pranjaladhi/coe-332/tree/main/homework06#running-the-code). As this project utilizes Kubernetes, kubectl must be installed which can be done [here](https://kubernetes.io/docs/tasks/tools/). After installation, the application can then be deployed. 

### Deploying Kubernetes Cluster
With the `.yml` files all within the same directory, the application can be deployed with the lines:
```
kubectl apply -f gene-flask-deployment.yml
kubectl apply -f gene-flask-service.yml
kubectl apply -f gene-redis-pvc.yml
kubectl apply -f gene-redis-deployment.yml
kubectl apply -f gene-redis-service.yml
```

### Requests to the API
With the deployment of the application, the user can start making requests with the options below.

#### > `curl -X POST pa8729-test-flask-service:5000/data`

This request will load the gene data from the source into the Redis database. Here, the `-X POST` is required as the method is a `POST`, and not the default `GET`. After running this request, it will allow the user to the requests below as the gene data has been loaded into the database. The output after running this request will be:
```
Data loaded in
```

#### > `curl -X GET pa8729-test-flask-service:5000/data`

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

#### > `curl -X DELETE pa8729-test-flask-service:5000/data`

This will delete the human gene data gathered from the source. The `-X DELETE` is required as the route accepts a `DELETE` method, and not the default `GET` method. After running this request, any other requests made will result in error as the gene data is no longer available in the database. The output of running this request will be:
```
Data deleted
```

If any requests are ran after running this `DELETE` request, a 404 error will return with the message:
```
Error. Data not loaded in
```

#### > `curl pa8729-test-flask-service:5000/genes/<hgnc_id>`

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

## HGNC Data
The data used for this project is gathered from HGNC. It provides the names, symbols, and the associated data regarding the various types of human genes. This includes the protein products, gene families, and the date the gene name was last changed. The dataset is available for the public and can be found [here](https://www.genenames.org/download/archive/).
