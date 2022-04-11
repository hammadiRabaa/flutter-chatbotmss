from flask import Flask, jsonify, request 
import time 
app = Flask(__name__)
app.route("/bot" , method=["POST"])
def response () : 
    query = dict(request.form)['query']
    result = query
    return jsonify({"response" : result})
    