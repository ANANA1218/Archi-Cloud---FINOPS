import requests
import time
import random

# URL de la fonction Azure
CLOUD_FUNCTION_ENDPOINT = "https://cloudanna.blob.core.windows.net/logs-container"

# Messages de log simulés
sample_logs = [
    {"level": "INFO", "message": "User logged in"},
    {"level": "DEBUG", "message": "User viewed page"},
    {"level": "ERROR", "message": "Database connection failed"}
]

def send_log_to_cloud_function(log):
    response = requests.post(CLOUD_FUNCTION_ENDPOINT, json=log)
    if response.status_code == 200:
        print(f"Log envoyé : {log}")
    else:
        print(f"Échec d'envoi du log : {log}, statut : {response.status_code}")

def simulate_log_stream():
    while True:
        log = random.choice(sample_logs)
        send_log_to_cloud_function(log)
        time.sleep(random.uniform(1, 3))

if __name__ == "__main__":
    simulate_log_stream()

