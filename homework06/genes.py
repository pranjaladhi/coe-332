#Pranjal Adhikari pa8729

from flask import Flask, request
import redis
import requests
import json

app = Flask(__name__)

def get_redis_client():
    return redis.Redis(host='redis-db', port=6379, db=0, decode_responses=True)
rd = get_redis_client()

def get_method() -> dict, str:
    global rd
    try: 
        load_genes_data = json.loads(rd.get('genes_data'))
    except Exception as err:
        return f'Error. Data not loaded in\n', 404
    return load_genes_data
    
@app.route('/data', methods = ['GET', 'POST', 'DELETE'])
def data_requests() -> dict, str:
    global rd
    if request.method == 'GET':
        genes = get_method()
        return genes

    elif request.method == 'POST':
        response = requests.get(url='https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/json/hgnc_complete_set.json')
        all_genes_data = response.json().get('response').get('docs')
        try:
            rd.set('genes_data', json.dumps(all_genes_data))
        except Exception as err:
            return f'Error. Data not loaded in\n', 404
        return f'Data loaded in\n'

    elif request.method == 'DELETE':
        try: 
            rd.flushdb()
        except Exception as err:
            return f'Error. Data not loaded in\n', 404
        return f'Data deleted\n'
            
    else:
        return f'No available method selected. Methods available: GET, POST, DELETE\n', 404    


@app.route('/genes', methods = ['GET'])
def genes() -> list:
    genes_data = get_method()
    genes_id_list = []
    try:
        for item in genes_data:
            genes_id_list.append(item.get('hgnc_id'))
    except Exception as err:
        return f'Error. Data not loaded in\n', 404
    return genes_id_list


@app.route('/genes/<hgnc_id>', methods = ['GET'])
def gene_id(hgnc_id: str) -> dict:
    global rd
    genes_data = get_method()
    try:
        for item in genes_data:
            if item.get('hgnc_id') == hgnc_id:
                return item
        return f'Error. No HGNC ID found\n', 404 
    except Exception as err:
        return f'Error. Data not loaded in\n', 404
            
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

