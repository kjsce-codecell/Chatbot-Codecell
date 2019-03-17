import random
from .responses import *

def welcome(req):
    arr = welcome_responses

    res = random.choice(arr)
    return res
