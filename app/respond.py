import random
from .responses import *

def welcome(req):
    arr = welcome_responses

    res = random.choice(arr)
    return res

def register(req):
    params = ['Name','Email']
    # Get the parameters for the request
    data = []
    
    for i in params:
        data.append([ i , req['queryResult']['parameters'].get(i) ])
   
    for i in data:
        if len(i[1]) <= 0:
            res = 'Give me ' + str(i[0])
            return res
    
    res = 'All Done'
    return res
