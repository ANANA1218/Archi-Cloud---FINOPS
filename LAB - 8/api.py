import requests

subscription_key = "9ccc6700d1b54f519f6e146e776552a6"
endpoint = "https://api.cognitive.microsofttranslator.com/"
path = "/translate?api-version=3.0"
params = "&to=es"  

body = [{
    'text': 'Bonjour, comment ça va ?'
}]


response = requests.post(endpoint + path + params, headers={
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Content-type': 'application/json'
}, json=body, verify=False)


if response.status_code == 200:
    translations = response.json()
    for translation in translations:
        for text in translation['translations']:
            print(f'Translated text: {text["text"]}')
else:
    print(f'Error: {response.status_code}, {response.text}')
