import json
import requests

from flask import Flask, render_template
from flask import request
from engine.chatbot import engine
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return render_template("index2.html")

@app.route("/chatbot/", methods=["GET", "POST"])
def index():
    # parsing = engine.parse("How are you?")
    # print(parsing['intent'])
    if request.method == "POST":
        print(request.form)
        # print("behwbehwehwjvdewvewjvh")
        # user_query = request.form["user_query"]
        # parsing = engine.parse(user_query)
        # print(parsing.intent)
        # json_response = json.dumps(parsing, indent=2)
        # url = ""
        # requests.post(url, json_response)
        # return json_response
        return "5"
    else:
        return "<h1>CHATBOT RUNNING....</h1>"

if __name__=="__main__":
    app.run(debug=True)