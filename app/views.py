# views.py

from flask import render_template,make_response,jsonify,request

from app import app
import json
import dialogflow
import os,pickle

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/send_message',methods=['POST'])
def send():
    message = request.form['message']
    print(message)
    project_id = os.getenv('DIALOGFLOW_PROJECT')
    fulfillment_text = detect_intent_texts(project_id, "unique", message, 'en')
    message = fulfillment_text
    if message == 'Team Members':
        team = get_team()
        message = team
    response_text = { "fulfillmentText":  message }
    print(response_text)
    return jsonify(response_text)

def get_team():
    text = ''
    with open('app/data/team.pkl', 'rb') as f:
        Team = pickle.load(f)
    for i in Team:
        text += i + ' :\n'
        for mem in Team[i]:
            text += mem[0] + '(' + mem[1] + ')\n'
    return text

def detect_intent_texts(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    if text:
        text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
        query_input = dialogflow.types.QueryInput(text=text_input)
        response = session_client.detect_intent(
            session=session, query_input=query_input)
        return response.query_result.fulfillment_text