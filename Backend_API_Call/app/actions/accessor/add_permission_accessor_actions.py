from app.helper import requestHandler

class AddPermissionOfAccessorActions:
    @staticmethod
    def add_permission_to_accessor(orgId, accessorId, token, permissionstoAdd, permissionstoRemove):
        url = "https://test2.acaas.api.spintly.com/permissionManagement/v2/organisations"
        full_url = f"{url}/{orgId}/accessors/{accessorId}/permissions"

        headers = {'Authorization': token, 'Content-Type': 'application/json'}

        data={
            "permissionsToAdd": permissionstoAdd,
            "permissionsToRemove": permissionstoRemove
        }

        response = requestHandler.sendRequest(full_url, headers, method='PATCH',json_data=data)
        return response 