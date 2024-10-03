import logging
import azure.functions as func
from azure.cosmos import CosmosClient, exceptions
import os
import json

# Configuration de la connexion à Azure Cosmos DB
ENDPOINT = os.environ['COSMOS_DB_ENDPOINT']
KEY = os.environ['COSMOS_DB_KEY']
DATABASE_NAME = os.environ['COSMOS_DB_DATABASE']
CONTAINER_NAME = os.environ['COSMOS_DB_CONTAINER']

client = CosmosClient(ENDPOINT, KEY)
database = client.get_database_client(DATABASE_NAME)
container = database.get_container_client(CONTAINER_NAME)

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing request to CRUD function.')

    try:
        # Vérification de la méthode HTTP
        if req.method == 'GET':
            items = list(container.read_all_items())
            return func.HttpResponse(json.dumps(items), status_code=200)
        
        elif req.method == 'POST':
            item = req.get_json()
            container.create_item(body=item)
            return func.HttpResponse("Item created.", status_code=201)

        elif req.method == 'PUT':
            item = req.get_json()
            container.upsert_item(body=item)
            return func.HttpResponse("Item updated.", status_code=200)

        elif req.method == 'DELETE':
            item_id = req.params.get('id')
            container.delete_item(item=item_id, partition_key=item_id)
            return func.HttpResponse("Item deleted.", status_code=204)

        else:
            return func.HttpResponse("Method not supported!", status_code=400)

    except exceptions.CosmosHttpResponseError as e:
        logging.error(f"Error occurred: {str(e)}")
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)
