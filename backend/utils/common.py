import json
from flask import jsonify, make_response

def response(data=None, error=None, status=200):
    if error == None:
        success = True
    else:
        success = False
    res = {
        "data": data,
        "success": success,
        "error": error
    }

    return jsonify(res), status

