from app import app
from app.controller.oauth_controller import OAuthController
from app.controller.site_controller import SiteController
from app.controller.access_point_controller import AccessPointController
from app.controller.accessor_controller import AccessorController



@app.route('/IntegrationSupport/login', methods=["POST"])
def get_token():
    return OAuthController.get_token()

@app.route('/getallSites', methods=['GET'])
def get_site():
    return SiteController.get_site()


@app.route('/getaccessitebyid/<int:siteId>', methods=['GET'])
def get_accesspoint(siteId):
    return AccessPointController.get_accesspoint(siteId)


@app.route('/getaccesspointpermsisions/<int:orgId>/<int:accesspointId>', methods=['GET'])
def get_accesspoint_permission(orgId, accesspointId):
    return AccessPointController.get_accesspoint_permission(orgId, accesspointId)


@app.route('/getpermissionofaccessor/<int:orgId>/<int:accessorid>', methods=['GET'])
def get_permission_of_accessor(orgId, accessorid):
    return AccessorController.get_permission_of_accessor(orgId, accessorid)


@app.route('/addpermissiontoaccess/<int:orgId>/<int:accessorId>', methods=['PATCH'])
def add_permissionaccessor(orgId, accessorId):
    return AccessorController.patch_permission_accessor_active(orgId, accessorId)

@app.route('/addaccessortoOrganisation', methods=['POST'])
def add_accessor_org():
    return AccessorController.add_accessor_to_org()
