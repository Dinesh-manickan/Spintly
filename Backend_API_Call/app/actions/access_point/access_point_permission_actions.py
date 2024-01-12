from app.helper import requestHandler

class AccessPointPermissionActions:
    @staticmethod
    def get_accesspoint_permission(orgId,accesspointId,token):
        url = "https://test2.acaas.api.spintly.com/permissionManagement/v2/organisations"
        full_url = f"{url}/{orgId}/accessPoints/{accesspointId}/permissions"
        headers = {'Authorization': token}

        response = requestHandler.sendRequest(full_url, headers, method='GET')
        return response 