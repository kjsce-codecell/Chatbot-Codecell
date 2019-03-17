# views.py

from flask import render_template,make_response,jsonify,request

from app import app
import json
import dialogflow
import os
from .respond import *

# UI Templates
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')


# Backend


@app.route('/webhook', methods=['POST'])
def webhook():
    """This method handles the http requests for the Dialogflow webhook
    This is meant to be used in conjunction with the weather Dialogflow agent
    """
    req = request.get_json(silent=True, force=True)
    try:
        action = req.get('queryResult').get('action')
    except AttributeError:
        return 'json error'

    print(req)
    # Add processing for all the queries here according to detected intent 
    if action == 'input.welcome':
        res = welcome(req)
    elif action == 'register':
        res = register(req)
    else:
        print('WrongggRegister')
        res = 'Kittu'

    print('Action: ' + action)
    print('Response: ' + res)
    return make_response(jsonify({'fulfillmentText': res}))





# Do Not Edit anything after this point -------------

@app.route('/send_message',methods=['POST'])
def send():
    message = request.form['message']
    print(message)
    project_id = os.getenv('DIALOGFLOW_PROJECT_ID')
    fulfillment_text = detect_intent_texts(project_id, "unasasique", message, 'en')
    response_text = { "fulfillmentText":  fulfillment_text }
    return jsonify(response_text)

def detect_intent_texts(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    if text:
        text_input = dialogflow.types.TextInput(
            text=text, language_code=language_code)
        query_input = dialogflow.types.QueryInput(text=text_input)
        response = session_client.detect_intent(
            session=session, query_input=query_input)
        return response.query_result.fulfillment_text
