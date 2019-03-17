import random,re
from .responses import *
from pprint import pprint
from .register import *
import requests
 
def get_contexts(req):
    contexts = {}
    print(req)
    if 'outputContexts' not in req['queryResult']:
        return contexts
    for i in req['queryResult']['outputContexts']:
        name = i['name'].split('/')[-1]
        try:
            contexts[name]
        except:
            contexts[name] = [i]
        else:
            contexts[name].append(i)
    return contexts

def welcome(req):
 
    res = {
        "fulfillmentMessages": [
            {
                "image": {
                    "imageUri": 'http://www.pikabit.net/wp-content/uploads/2012/10/yamato2.gif',
                    "accessibilityText": 'Hey Theree'
                }
            },
            {
                "text": {
                    "text": [
                        random.choice(welcome_greet)
                        # "Nice to meet you ! I'm Korusuke."
                    ]
                }
            },
            {
                "text": {
                    "text": [
                        random.choice(welcome_goal)
                    
                    ]
                }
            },
            {
                "quickReplies": {
                    "title": "(Press the button below ⬇️)",
                    "quickReplies": [
                        'Register 🙌',
                        'About Team'
                    ] 
                }
            }
        ]
    }

    
    return res

def register(req):
    params = ['Name', 'Email','Study','Branch']
    # Get the parameters for the request
    data = []
    
    for i in params:
        data.append([ i , req['queryResult']['parameters'].get(i) ])
   
    for i in data:
        if len(i[1]) <= 0:
            fun = globals()['register_' + i[0]]
            res = fun(req,data)
            return res
    print(data)
    fill_form(data)
    res = registered_success(req,data)
    return res


def team(req):
    data = {}
    data['team'] = req['queryResult']['parameters'].get('team')
    # pprint(req)
    contexts = get_contexts(req)
    # pprint(contexts)
    
    text = ''
    if len(data['team'])==1 and 'team' in data['team']:
        for i in team_members:
            text += i + '<br>' + team_description[i]['phrase'] + '<br>'
            for mem in team_members[i]:
                text += mem[0]+'\n'
            text += '<br>'

    else:
        for i in team_members:
            if i in data['team']:
                text += i + '<br>' + team_description[i]['phrase'] + '<br>'
                for mem in team_members[i]:
                    text +=  mem[0] + '\n'
                text += '<br>'
                break 
        else:
            text = 'No such team in the CodeCell'
    texts = text.split('<br>')[:-1]
    return gen_res(texts) 

def team_info(req):
    info = req['queryResult']['parameters'].get('team_info')
    contexts = get_contexts(req)
    pprint(contexts)
    part = req['queryResult']['parameters'].get('teampart')
    text = ''
    if 'team_part' in contexts:
        for i in contexts['team_part']:
            part.extend(i['parameters']['team'])
    print(part, info)
    if part.count('team')==len(part):
        for j in info: 
            if j in team_description['Council']:
                text = team_description['Council'][j]
    else:
        for i in team_description:
            if i in part:
                for j in info:
                    if j in team_description[i]:
                        text = team_description[i][j]
                break
        else:
            text = "Sorry. I don't know."
    texts = text.split('\n')
    return gen_res(texts)       

def gen_res(li):
    res = {"fulfillmentMessages": [
    ]}
    print(li, len(li))
    print(type(li))
    for i in range(0,len(li),3):
        card = {
            'card' : {
                "title": li[i],
                "subtitle": li[i+1],
                "buttons": [
                    {
                        
                        "text": "Learn More",
                        "postback": "Know more about" + li[i]
                        
                    }
                ]
            }
        }
        res['fulfillmentMessages'].append(card)
    print(res)
    return res




def fill_form(data):

    url = 'https://docs.google.com/forms/d/e/1FAIpQLSdqBWG3rFSRYNvwfzfB9ZYY6MqGwXYnV9QwHiQ6rylSha33Aw/formResponse'
    form_data = {'entry.1109606640': data[0][1],
                 'entry.686652295': data[1][1],
                 'entry.140053970': data[2][1],
                 'entry.2060584350': data[3][1],
                 'draftResponse': [],
                 'pageHistory': 0}
    user_agent = {'Referer': 'https://docs.google.com/forms/d/e/1FAIpQLSdqBWG3rFSRYNvwfzfB9ZYY6MqGwXYnV9QwHiQ6rylSha33Aw/viewform',
                  'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"}
    r = requests.post(url, data=form_data, headers=user_agent)

    print('Done Succesfull')

    return
