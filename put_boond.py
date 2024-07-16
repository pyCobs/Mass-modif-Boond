from dotenv import load_dotenv
import requests
import os
import time
import jwt

load_dotenv()
# MY_ENV_VAR = os.getenv('MY_ENV_VAR')


def put_contact(ccon, encoded_user_payload):
    url = f"https://ui.boondmanager.com/api/contacts/{ccon}/information"

    # Modifie le pôle pour mettre le 10 qui correspond à OP2
    data = \
        {"data": {
                "id": f"{ccon}",
                "type": "contact",
                "relationships": {
                    "pole": {
                        "data": {
                            "id": "10",
                            "type": "pole"
                        }
                    }
                }
        }}

    put_response = requests.put(url, json=data, headers={
        'Accept': 'application/json',
        'X-Jwt-Client-Boondmanager': encoded_user_payload,
        'Content-Type': 'application/json',
    })

    # Vérifier le statut de la réponse
    if put_response.status_code == 200:
        print(f'Requête réussie pour le contact {ccon}')
    else:
        print(f'Erreur : {put_response.status_code} pour le contact {ccon}')



if __name__ == "__main__":
    user_payload = {
        "userToken": os.getenv('userToken'),
        "clientToken": os.getenv('clientToken'),
        "time": int(time.time()),
        "mode": "god"
    }
    encoded_user_payload = jwt.encode(user_payload, os.getenv('clientKey'), algorithm="HS256")
    ccon = 9579
    put_contact(ccon, encoded_user_payload)

