import requests
from flask import jsonify,make_response

from app.constant import httpstatuscode

def sendRequest(full_url, headers, method, json_data=None):
    match method:
        case 'POST': response = requests.post(full_url, headers=headers, json=json_data)
        case 'GET' : response = requests.get(full_url, headers=headers)
        case 'PATCH': response = requests.patch(full_url, headers=headers, json=json_data)


       
    # if response:
    if response.status_code == 200:
        data = response.json()
        return make_response(jsonify(httpstatuscode.get_http_status_code_info(response.status_code),data),response.status_code )
    else:
        return make_response(jsonify(httpstatuscode.get_http_status_code_info(response.status_code)),response.status_code )
    # else:
    #     return make_response(jsonify(httpstatuscode.get_http_status_code_info(500)),500)
