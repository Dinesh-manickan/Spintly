from flask import request, jsonify
from app.actions.access_point.access_point_actions import AccessPointActions
from app.actions.access_point.access_point_permission_actions import AccessPointPermissionActions

class AccessPointController:
    @staticmethod
    def get_accesspoint(siteId):
        token = request.headers.get('Authorization')
        if token is None:
            return jsonify({"error": "Please Add the Authorization Token"})
        return AccessPointActions.get_accesspoint(siteId, token)

    @staticmethod
    def get_accesspoint_permission(orgId, accesspointId):
        token = request.headers.get('Authorization')
        if token is None:
            return jsonify({"error": "Please Add the Authorization Token"})
        return AccessPointPermissionActions.get_accesspoint_permission(orgId, accesspointId, token)
