from dbhelpers import conn_exe_close
from apihelpers import get_display_results, verify_endpoints_info
from flask import Flask,request,make_response, jsonify

app = Flask(__name__)

@app.post('/api/user')
def add_user():
    invalid = verify_endpoints_info(request.json, ['user','password','is_premium'])
    if(invalid != None):
        return make_response(jsonify(invalid),400)
    results_json = get_display_results('call add_user(?,?,?)',[request.json.get('user'),request.json.get('password'),request.json.get('is_premium')])
    return results_json

@app.patch('/api/user')
def update_password():
    invalid = verify_endpoints_info(request.json, ['user'])

app.run(debug=True)
