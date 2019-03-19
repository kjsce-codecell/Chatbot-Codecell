import random
import re
from .responses import *
from pprint import pprint
from .register import *
#from .database import *
import requests
import string
from bs4 import BeautifulSoup
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from flask import jsonify
import os


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
    query = req['queryResult']['queryText']
    if query == 'Get Started':
        # Rushangs Database increase count function which will probably record more stuff also this in try catch pplzz
        try:
            count()
            #print("Contexts : ",req['queryResult']['outputContexts'])
            fb_id = req['queryResult']['outputContexts'][0]['parameters'].get("facebook_sender_id")
            #print("FB id :",fb_id)
            user_freq(fb_id)
        except:
            print("FB_ID_NOT found")
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
                    "text": {
                        "text": [
                            "I can do many things like : \n- Help you get a seat at the Event\n- Tell you about my team\n- Sing Along with you(Hint:Just type Sing / Sing along with me)"

                        ]
                    }
                },
                {
                    "telephonySynthesizeSpeech": {
                        "text": "Hey There Awesome person , you are talking to Korusuke Bot.I can help you register for the codecell events and also tell you some funny and spicy facts about them."
                    }
                }
            ]
        }
    else:
        res = {
            "fulfillmentMessages": [
                {
                    "image": {
                        # Add randomization of gif/images
                        "imageUri": 'http://www.pikabit.net/wp-content/uploads/2012/10/yamato2.gif',
                        "accessibilityText": 'Hey There'
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
                    "telephonySynthesizeSpeech": {
                        "text": "Hey There Amazing person."
                    }
                }
            ]
        }

    return res


def register(req):
    params = ['Name', 'College', 'Year', 'Branch', 'Email']
    # Get the parameters for the request
    data = []

    for i in params:
        data.append([i, req['queryResult']['parameters'].get(i)])

    for i in data:
        if len(i[1]) <= 0:
            fun = globals()['register_' + i[0]]
            res = fun(req, data)
            return res
    print(data)
    participant = {}
    for field in data:
        participant[field[0]] = field[1]
    if add_participant(participant):
        fill_form(data)
        res = registered_success(req, data)
    else:
        res = registered_failed(req, data) #Email id exists
    return res


def team(req):
    if 'What does the ' in req['queryResult']['queryText'] or 'List the Members of ' in req['queryResult']['queryText']:
        handle_team(req) 
    part = req['queryResult']['parameters'].get('teampart')
    contexts = get_contexts(req)
    text = ''
    # print(team_members)
    if "Council" in part:
        for i in team_members:
            text += i + '<br>' + team_description[i]['phrase'] + '<br>'
            for mem in team_members[i]:
                text += mem[0]+'\n'
            text += '<br>'
    else:
        for i in team_members:
            for j in part:
                # print(i, j)
                if i.find(j) != -1:
                    text += i + '<br>' + team_description[i]['phrase'] + '<br>'
                    # print(text)
                    break
        if text == '':
            text = "Sorry. I don't understand"
    print(text, part)
    texts = text.split('<br>')[:-1]
    return gen_res(texts)


def handle_team(req):
    print(req) 
    print('\nnhandle\n')
    print(req['queryResult'])
    querytext = req['queryResult']['queryText']
    print(querytext)
    part = req['queryResult']['parameters'].get('teampart')
    response_text = part+'\n\n'
    if 'List the members of ' in querytext:
        mem=team_members[part][1]
        
        for member in mem:
            response_text = member[0]+'\n'
    else:
        response_text+=team_description[part[1]]
        

    return jsonify({
        "fulfillmentMessages": [{
                    "text": {
                        "text": [response_text],
                    }
        }]
    })

def gen_res(li):
    res = {"fulfillmentMessages": [
    ]}
    print(li, len(li))
    print(type(li))
    for i in range(0, len(li), 3):
        card = {
            'card': {
                "title": li[i],
                "subtitle": li[i+1],
                "buttons": [
                    {
                        "text": "Learn More",
                        "postback": "What does the " + li[i] + " do?"
                    },
                    {
                        "text": "Members",
                        "postback": "List the members of " + li[i]
                    }
                ]
            }
        }

        res['fulfillmentMessages'].append(card)
        # res["followupEventInput"] = {
        #     "name": "teamevent",

        #     "languageCode": "en-US"
        # }

    print(res)
    return res


def fill_form(data):

    url = 'https://docs.google.com/forms/d/e/1FAIpQLSdqBWG3rFSRYNvwfzfB9ZYY6MqGwXYnV9QwHiQ6rylSha33Aw/formResponse'
    form_data = {'entry.1109606640': data[0][1],
                 'entry.686652295': data[1][1],
                 'entry.523789151': data[2][1],
                 'entry.140053970': data[3][1],
                 'entry.2060584350': data[4][1],
                 'draftResponse': [],
                 'pageHistory': 0}
    user_agent = {'Referer': 'https://docs.google.com/forms/d/e/1FAIpQLSdqBWG3rFSRYNvwfzfB9ZYY6MqGwXYnV9QwHiQ6rylSha33Aw/viewform',
                  'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"}
    r = requests.post(url, data=form_data, headers=user_agent)

    print('Done Succesfull')

    return


def get_cosine_sim(*strs):
    vectors = [t for t in get_vectors(*strs)]
    return cosine_similarity(vectors)


def get_vectors(*strs):
    text = [t for t in strs]
    vectorizer = CountVectorizer(text)
    vectorizer.fit(text)
    return vectorizer.transform(text).toarray()


def matches(inp, lines):
    inp = inp.lower()
    inp = inp.translate(str.maketrans('', '', string.punctuation))
    gcls = []
    count = 0
    for line in lines:
        line = line.lower()
        line = line.translate(str.maketrans('', '', string.punctuation))
        gcl = get_cosine_sim(line, inp)[0, 1]
        gcls.append(int(gcl*1000000))
        # print('START', count,' :\n', line, '\n', gcl, end='\n\n')
        count += 1
    print(gcls.index(max(gcls)))
    return gcls.index(max(gcls))


def getsongname(lyrics):

    try:
        # lyrics2 = lyrics+' site:genius.com'
        # r2 = requests.get('https://cse.google.com/cse/element/v1?rsz=filtered_cse&num=1&hl=en&source=gcsc&gss=.com&cx=partner-pub-1936238606905173:8242090140&q='+lyrics2+'&safe=active&cse_tok=AKaTTZgl8Z01gcjfA5uOQop4YH9c:1552906151870&exp=csqr,4231019&callback=google.search.cse.api13080',
        #     headers={'referrer':"https://findmusicbylyrics.com/search?q="+lyrics2,
        #     "credentials":"omit",
        #     'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36'
        # })
        #
        # t2 = r2.text[35:-2]
        # d = eval(t2)
        # url2=d['results'][0]['clicktrackUrl'][29:].split('&')[0]
        r2 = requests.get('https://www.googleapis.com/customsearch/v1?q='+lyrics +
                          '&cx=010037727290940322759%3Alfq5lr9jjek&num=1&key=AIzaSyBE_yhmpb0CwmSHG0d4KPh91YEFrgyvIy4')
        print('here 1,1')
        d = eval(r2.text)
        url2 = d['items'][0]['link']
        print('here 1,2')
        title = d['items'][0]['pagemap']['metatags'][0]['og:title']

        t = requests.get(url2).text
        soup = BeautifulSoup(t)
        song = soup.find_all('div', attrs={'class': 'lyrics'})[
            0].find('p').text
        lines = song.split('\n')
        lines = [i for i in lines if (i != '' and i[0] != '[')]
        lno = matches(lyrics, lines)
        print('here 1,3')
        print(len(lines))
        if lno >= len(lines):
            conti = '...'
        else:
            conti = lines[lno+1]
        # title = soup.find_all('h1', attrs={'class':'header_with_cover_art-primary_info-title'})[0].text.split('(')[0]
        print('1 runs')
    except:
        r = requests.get('https://songsear.ch/q/'+lyrics)
        soup = BeautifulSoup(r.text)
        l = soup.find_all(
            'h2', attrs={'title': 'Click to view just this song'})
        li = soup.find_all('div', attrs={'class': 'fragments'})
        print((l[0].find('a').text.split('(')[0], str(
            li[0].find('p')).split('</mark>')[-1][:-4].replace('\n', '')))
        re = str(li[0].find('p')).split(
            '</mark>')[-1][:-4].replace('\n', '').split('..')[0]
        rer = re[0]
        for e in re[1:]:
            if e in string.ascii_uppercase and e != 'I':
                break
            rer += e
        title = l[0].find('a').text.split('(')[0]
        conti = rer
        print('2 runs')

    print('title', title)
    print('conti', conti)
    return title, conti


def handle_song(req):
    lyr = req['queryResult']['queryText']
    songname, content = getsongname(lyr)
    return jsonify({"fulfillmentMessages": [{
                    "text": {
                        "text": [content],
                    }
                    }, {
        "text": {
            "text": [songname+'! I love this song!'],
        }
    },
        {
        "telephonySynthesizeSpeech": {
            "text": content
        }
    }],
    })


def myfunction(req):
    res = {
        "fulfillmentMessages": [
            {
                "text": {
                    "text": [

                        "I can do a lot of stuff cause I am smart 😎 Here are some cool things to try out"
                    ]
                }
            },
            {
                "text": {
                    "text": [
                        "I would Like to register for the awesome event you guys are hosting"

                    ]
                }
            },
            {
                "text": {
                    "text": [
                        "Sing along with me"

                    ]
                }
            },
            {
                "text": {
                    "text": [
                        "I would like to know more about your team"

                    ]
                }
            },
            {
                "text": {
                    "text": [
                        "Or you could try asking me personal questions about me🤫 but I won't always answer them 🤪"

                    ]
                }
            }

        ]
    }
    return res
