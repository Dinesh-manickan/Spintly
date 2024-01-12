from flask import request, jsonify
from app.actions.accessor.permission_accessor_actions import PermissionOfAccessorActions
from app.actions.accessor.add_accessor_to_organisation_actions import AddAccessorToOrganisationActions
from app.actions.accessor.add_permission_accessor_actions import AddPermissionOfAccessorActions

class AccessorController:
    @staticmethod
    def get_permission_of_accessor(orgId, accessorid):
        token = request.headers.get('Authorization')
        if token is None:
            return jsonify({"error": "Please Add the Authorization Token"})
        return PermissionOfAccessorActions.get_permission_of_accessor(orgId, accessorid, token)

    @staticmethod
    def add_accessor_to_org():
        token = request.headers.get('Authorization')
        if token is None:
            return jsonify({"error": "Please Add the Authorization Token"})
        
        orgId = request.json.get('orgId')
        credentialId = request.json.get('credentialId')
        permissionsToAdd = request.json.get('permissionsToAdd')
        identityInfo = request.json.get('identityInfo')

        return AddAccessorToOrganisationActions.add_accessor_to_org(token,orgId,credentialId,permissionsToAdd,identityInfo)

    @staticmethod
    def patch_permission_accessor_active(orgId, accessorId):
        token = request.headers.get('Authorization')
        if token is None:
            return jsonify({"error": "Please Add the Authorization Token"})
        
        permissionstoAdd = request.json.get('permissionsToAdd', [])
        permissionstoRemove = request.json.get('permissionsToRemove', [])

        return AddPermissionOfAccessorActions.add_permission_to_accessor(orgId, accessorId, token, permissionstoAdd, permissionstoRemove)
