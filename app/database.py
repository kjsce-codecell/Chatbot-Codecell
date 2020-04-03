from pymongo import MongoClient
import os
mongodb_url = str(os.environ["MONGODB"])


def connect():
    client = MongoClient(mongodb_url)
    db = client.codecell_chatbot
    return db


def check_email(email):
    db = connect().chatbot_workshop
    if db.find_one({'Email': email}):
        print("Already Present")
        return 1
    return 0


def add_participant(participant):
    db = connect().chatbot_workshop
    if check_email(participant['Email']):
        return 0
    participant['Payment'] = False
    db.insert(participant)
    return 1


def user_freq(user_id):
    db = connect().logs
    user = {'fb_id': user_id}
    if db.find_one(user):
        print("User found")
        try:
            db.update(user, {"$inc": {"messages": 1}})
            print("Messages Updated")
        except:
            print("Update Error")
    else:
        print("Adding User")
        user['messages'] = 1
        db.insert(user)
    return 1


def count():
    db = connect().logs
    print("Counter")
    try:
        db.update({"counter": True}, {"$inc": {"messages": 1}})
        print("Update successful")
    except:
        print("Update error")
    return 1


def test():
    participant = {
        "Name": "Team Probably",
        "Email": "teamprobably@gmail.com",
        "College": "KJSCE",
        "Branch": "Comps",
        "Year": "SY",
        "Payment": False
    }
    return 1
