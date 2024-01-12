from app.helper import requestHandler

class PermissionOfAccessorActions:
    @staticmethod
    def get_permission_of_accessor(orgId,accessorid,token):
        url = "https://test2.acaas.api.spintly.com/permissionManagement/v2/organisations"
        full_url = f"{url}/{orgId}/accessors/{accessorid}/permissions"
        headers = {'Authorization': token}
        
        response = requestHandler.sendRequest(full_url, headers, method='GET')
        return response 