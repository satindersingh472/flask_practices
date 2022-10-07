from dbhelpers import conn_exe_close, verify_endpoints, get_display_results
from flask import Flask,request
import json

app = Flask(__name__)

@app.post('/api/user')
def add_user():
    invalid = verify_endpoints(request.json, ['user','password','is_premium'])
    if(invalid != None):
        return invalid
    results_json = get_display_results('call add_user(?,?,?)',[request.json.get('user'),request.json.get('password'),request.json.get('is_premium')])
    return results_json

@app.patch('/api/user')
def update_password():
    invalid = verify_endpoints(request.json, ['user'])

app.run(debug=True)
