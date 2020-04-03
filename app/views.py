# views.py

from flask import send_file
from flask import render_template, make_response, jsonify, request, session

from app import app
import json
from .respond import *
import os
import pickle
from .respond import handle_song, handle_team
from .database import *


# Backend

@app.route('/webhook', methods=['POST'])
def webhook():
    """This method handles the http requests for the Dialogflow webhook
    This is meant to be used in conjunction with the weather Dialogflow agent
    """
    req = request.get_json(silent=True, force=True)
    try:
        # extract action and intent
        action = req.get('queryResult').get('action')
        intent = req.get('queryResult').get('intent').get('displayName')
    except AttributeError:
        return 'json error'

    # insert into database
    try:
        count()
        fb_id = req['queryResult']['outputContexts'][0]['parameters'].get(
            "facebook_sender_id")
        user_freq(fb_id)
    except:
        print("FB_ID_NOT found")

    # Add processing for all the queries here according to detected intent
    print('Action: ' + str(action))
    if intent == 'song':
        return jsonify({"fulfillmentMessages": [{
            "text": {
                        "text": ["jam"],
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
        return res
    elif action == 'myfunction':
        res = myfunction(req)
        return make_response(jsonify(res))
    else:
        res = 'Kittu'
    print('Response: ' + res)
    return make_response(jsonify({'fulfillmentText': res}))


# for hosting image for autosending


@app.route('/get_image')
def get_image():
    filename = 'static/passes/' + request.args.get('name')
    return send_file(filename, mimetype='image/jpeg')
