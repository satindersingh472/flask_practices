from dbhelpers import conn_exe_close
from flask import make_response, jsonify

def get_display_results(statement,args_list):
    results = conn_exe_close(statement,args_list)
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    elif(type(results) == str):
        return make_response(jsonify(results), 400)
    else:
        return make_response(jsonify(results) , 500)

    

def verify_endpoints_info(sent_data,required_args):
    for data in required_args:
        if(sent_data.get(data) == None):
            return f"The {data} argument is required"