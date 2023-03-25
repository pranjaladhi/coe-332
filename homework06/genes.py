from flask import Flask, request
import redis
import requests

app = Flask(__name__)
def get_redis_client():
    return redis.Redis(host='redis-db', port=6379, db=0, decode_responses=True)
rd = get_redis_client()


@app.route('/data', methods = ['GET', 'POST', 'DELETE'])
def data_requests():
    global rd
    if request.method == 'GET':
        all_gene_data = rd.hgetall('genes_data')
        #all_gene_data = []
        #    all_gene_data.append(rd.hgetall(item))
        return all_gene_data

    elif request.method == 'POST':
        response = requests.get(url='https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/json/hgnc_complete_set.json').json()
        
        return 'Data loaded in\n'

    elif request.method == 'DELETE':
        rd.flushdb()
        return f'Data deleted, there are {len(rd.keys())} keys in the db\n'
            
    else:
        return 'No method selected. Methods available: GET, POST, DELETE\n'    


@app.route('/genes', methods = ['GET'])
def genes():
    genes_data = [] 
    return genes_data


@app.route('/genes/<hgnc_id>', methods = ['GET'])
def gene_id():
    genes_id = []
    #if item == hgnc_id
    return genes_id

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

