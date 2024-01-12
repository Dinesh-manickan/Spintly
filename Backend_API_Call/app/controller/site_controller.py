from flask import request, jsonify
from app.actions.site.site_actions import SiteActions

class SiteController:
    @staticmethod
    def get_site():
        token = request.headers.get('Authorization')
        if token is None:
            return jsonify({"error": "Please Add the Authorization Token"})
        return SiteActions.get_site(token)
