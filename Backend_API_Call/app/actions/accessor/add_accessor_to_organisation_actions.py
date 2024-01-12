from app.helper import requestHandler

class AddAccessorToOrganisationActions:
    @staticmethod
    def add_accessor_to_org(token,orgId,credentialId,permissionsToAdd,identityInfo):
        url = "https://test2.acaas.api.spintly.com/permissionManagement/v6/accessors"
        headers = {'Authorization': token}  

        data={
            "orgId": orgId,
            "credentialId": credentialId,
            "permissionsToAdd": permissionsToAdd,
            "identityInfo": identityInfo
        }

        response = requestHandler.sendRequest(url, headers, method='POST',json_data=data)
        return response 