from flask import Flask, jsonify, request 
import time 
app = Flask(__name__)
app.route("https://flutter-chatbotappmss.herokuapp.com/bot" , method=["POST"])
def response () : 
    query = dict(request.form)['query']
    result = query + "votre message"
    return jsonify({"response" : result})


app.run(host="0.0.0.0",)