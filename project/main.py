# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from chatbot_model import chatbot_response
from scrape import scrape_data


check_wikipedia1 = ['what', 'is']
check_wikipedia2 = ['who', 'is']
check_wikihow = ['how', 'to']

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_request = request.args.get('msg')  # Fetching input from the user
    user_request = user_request.lower()
    if len(user_request.split(" ")) > 1:
        check_search = user_request.split(" ")[0]
        if check_search == 'google':
            user_request = user_request.replace("google","")
            user_request = user_request.translate ({ord(c): "" for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"})
            check_query = user_request.split(" ")[1]
            check_text = user_request.split(" ")[1:3]
            response = scrape_data(user_request, "")
            print("Here 3i")
        else:
            response = chatbot_response(user_request)
            print("Here 4i")                

    else:
        response = chatbot_response(user_request)
        print("Here -----------------------------------")
    
    return response

if __name__ == "__main__":
    app.run(threaded=False)