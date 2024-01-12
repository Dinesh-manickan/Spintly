from app.helper import requestHandler

class SiteActions:
    @staticmethod
    def get_site(token):
        url = "https://test2.acaas.api.spintly.com/permissionManagement/v3/sites"
        headers = {'Authorization': token}

        response = requestHandler.sendRequest(url, headers, method='GET')
        return response