#app.py
import json
import sqlite as db
import helper

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to application"

@app.route("/setup")
def setup():
  helper.save_model()
  body = {
    "message": "Setup Successfull"
  }
  response = {
    "statusCode": 200,
    "body": json.dumps(body)
  }
  return response

@app.route("/search",methods = ['POST', 'GET'])
def search():
  search_st = request.form.get('searched')
  print(search_st)
  result = helper.get_similar_documents(search_st)
  print(result)
  return render_template('result.html', results = result) 
