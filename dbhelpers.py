import json
import mariadb
import dbcreds

def connect_db():
    conn = mariadb.connect(user=dbcreds.user,host=dbcreds.host, password=dbcreds.password,port=dbcreds.port,database=dbcreds.database)
    cursor = conn.cursor()
    return cursor

def execute_statement(cursor,statement,list=[]):
    cursor.execute(statement,list)
    result = cursor.fetchall()
    return result

def close_connection(cursor):
    conn = cursor.connection
    cursor.close()
    conn.close()

def conn_exe_close(statement,list):
    cursor = connect_db()
    result = execute_statement(cursor,statement,list)
    close_connection(cursor)
    return result

def get_display_results(statement,args_list):
    results = conn_exe_close(statement,args_list)
    if(type(results) == list):
        results_json = json.dumps(results,default=str)
        return results_json
    elif(type(results) == str):
        return results
    else:
        return "something went wrong"

def verify_endpoints(sent_data,required_args):
    for data in required_args:
        if(sent_data.get(data) == None):
            return f"The {data} argument is required"