from azure.storage.blob import BlobServiceClient
import azure.functions as func
import os

def main(req: func.HttpRequest) -> func.HttpResponse:
    connection_string = os.getenv("cloudanna")
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container="logs", blob="log.txt")

    log_data = f"{req.method} - {req.url}\n"
    blob_client.upload_blob(log_data, overwrite=True)

    return func.HttpResponse("Logged request!", status_code=200)
