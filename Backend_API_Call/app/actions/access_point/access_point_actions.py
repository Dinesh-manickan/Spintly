from app.helper import requestHandler


class AccessPointActions:
    @staticmethod
    def get_accesspoint(siteId, token):
        url = "https://test2.acaas.api.spintly.com/permissionManagement/v3/sites"
        full_url = f"{url}/{siteId}/accessPoints"
        headers = {'Authorization': token}
        response = requestHandler.sendRequest(full_url, headers, method='GET')
        return response