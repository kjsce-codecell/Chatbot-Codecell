# views.py

from flask import render_template,make_response,jsonify,request,session

from app import app
import json
import dialogflow_v2beta1 as dialogflow
import os
from .respond import *
import os,pickle 
import uuid
from .respond import handle_song, handle_team
from .database import *

session_id = 'Default'
app.secret_key = 'any random string'
session = {}

# UI Templates / Temporary App so it does session id 
@app.route('/')
def index():
    session['uid'] = uuid.uuid4()
    return render_template("index.html")

@app.route('/chatbot')
def chatbot():
    session['uid'] = uuid.uuid4()
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
        intent = req.get('queryResult').get('intent').get('displayName')
    except AttributeError:
        return 'json error'
    try:
        count()
        print("Counter Called")
        #print("Contexts : ",req['queryResult']['outputContexts'])
        fb_id = req['queryResult']['outputContexts'][0]['parameters'].get("facebook_sender_id")
        #print("FB id :",fb_id)
        user_freq(fb_id)
    except:
        print("FB_ID_NOT found")
    print(get_contexts(req))
    # Add processing for all the queries here according to detected intent 
    print('Action: ' + str(action))
    if intent == 'song':
        return jsonify({"fulfillmentMessages": [{
                    "text": {
                        "text":["jam"],
                    }
                }],
                "followupEventInput": {
                "name": "songin",
                "languageCode": "en-US"
                }
        })
    elif intent == 'songin':
        return handle_song(req)
    elif intent == 'teamevent':
        return handle_team(req)
    elif action == 'input.welcome':
        res = welcome(req)
        return make_response(jsonify(res))
    elif action == 'register':
        res = register(req)
        return make_response(jsonify(res))
    elif action == 'team':
        res = team(req)
        print(res)
        return res
    elif action == 'team_info':
        res = team_info(req)
        print(res)
        return make_response(jsonify(res))
    elif action == 'myfunction':
        res = myfunction(req)
        print(res)
        return make_response(jsonify(res))
    
    else:
        print('WrongggRegister')
        res = 'Kittu' 
    print('Response: ' + res)
    return make_response(jsonify({'fulfillmentText': res}))


 


# Do Not Edit anything after this point -------------

@app.route('/send_message',methods=['POST'])
def send():
    message = request.form['message']
    print("Incoming Message :",message)
    project_id = os.getenv()
    try:
        session_id = session['uid']
    except:
        session_id = 'Default'
        pass
    fulfillment_text = detect_intent_texts(
        project_id, session_id, message, 'en')
    response_text = { "fulfillmentText":  fulfillment_text }
    return jsonify(response_text)

def detect_intent_texts(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    if text:
        text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
        query_input = dialogflow.types.QueryInput(text=text_input)
        response = session_client.detect_intent(
            session=session, query_input=query_input) 
        print(response,'guyguy')
        return response.query_result.fulfillment_text


from flask import send_file

@app.route('/get_image')
def get_image():
    filename = 'static/passes/' + request.args.get('name')
    return send_file(filename, mimetype='image/jpeg')

