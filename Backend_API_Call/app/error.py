from app import app
from flask import jsonify, make_response
from app.constant import httpstatuscode

@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(httpstatuscode.get_http_status_code_info(404)),404)