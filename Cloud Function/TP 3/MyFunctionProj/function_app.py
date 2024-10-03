import logging
import azure.functions as func
from azure.storage.blob import BlobServiceClient
import os

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('HTTP trigger function received a request.')
    
    # Configuration pour se connecter au compte de stockage Azure
    connection_string = os.getenv('AzureWebJobsStorage')
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    
    # Récupère le conteneur 'logs-container'
    container_client = blob_service_client.get_container_client("logs-container")
    
    # Génère un log avec l'IP de la requête, la méthode HTTP et l'URL
    log_data = f"{req.remote_addr} - {req.method} - {req.url}\n"
    
    # Écrire les logs dans un blob nommé 'logs.txt'
    blob_client = container_client.get_blob_client("logs.txt")
    blob_client.upload_blob(log_data, overwrite=True)
    
    return func.HttpResponse("Logged request!", status_code=200)
