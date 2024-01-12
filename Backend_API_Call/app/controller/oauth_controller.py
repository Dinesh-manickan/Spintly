from flask import request, jsonify
from app.actions.oauth.token_generator_actions import TokenGeneratorActions

class OAuthController:
    @staticmethod
    def get_token():
        client_id = request.json.get('client_id')
        cliend_secret = request.json.get('client_secret')

        if client_id is None:
            return jsonify({"error":"Please add the client_id"})
        
        if cliend_secret is None:
            return jsonify({"error": "Please add the client_Secret"})
        
        return TokenGeneratorActions.get_token(client_id,cliend_secret)