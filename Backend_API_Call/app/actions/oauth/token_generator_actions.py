from flask import jsonify
import requests

class TokenGeneratorActions:
    @staticmethod
    def get_token(client_id,cliend_secret):
        url = "https://test2.iot.api.spintly.com/identityManagement/v2/oauth/token"

        response = requests.post(url, json={
            "client_id": client_id,
            "client_secret": cliend_secret,
            "grant_type": "urn:ietf:params:oauth:grant-type:client-credentials"
        })

        if response.status_code == 200:
            data = response.json()
            access_token = data.get('access_token')

            return jsonify({
                "type": "Succes",
                "message":{
                    "accessToken": access_token
                }
            })
        else:
            return jsonify({
                "type" : "ERROR",
                "message":{
                    "errorCode": response.status_code,
                    "errorMessage": "Failed"
                }
            }),response.status_code