
def register_Name(req,data):
    res = {"fulfillmentMessages": [
        {
            "image": {
                "imageUri": 'http://sov.surge.sh/Sources%20of%20vitamins_files/Chatbot_Poster.jpeg', #Replace with current poster
                "accessibilityText": 'Event Poster'
            }
        },
        {
            "text": {
                "text": [
                    "Lets get you registered quickly!!"
                ]
            }
        },
        {
            "text": {
                "text": [
                    "You just need to answer a few questions first😇"
                ]
            }
        },
        {
            "text": {
                "text": [
                    "Let's start with something simple \nWhat's your Name - the one written on your birth certificate?"
                ]
            }
        }, 
        {
            "telephonySynthesizeSpeech": {
                "text": "To get you registered, we need some details.Give us your name - the one on your birth certificate."
            }
        }
    ]}
    print(res,'Nameeee')
    return res


def register_Email(req, data):
    
    res = {
        "fulfillmentMessages": [
        {
            "text": {
                "text": [
                    "Hello there " + str(data[0][1]) + " \nIts nice to know your name, now I can stalk you🙃"
                ]
            }
        },
        {
            "text": {
                "text": [
                    "Oh I also need your Email ID, for better stalking purposes \n _wink wink_" 
                ]
            }
        },
        {
            "telephonySynthesizeSpeech": {
                "text": "So " + str(data[0][1]) + "I hope I pronounced your name correctly, we need your email id"
            }
        }
    ]}
    print(res, 'Emaill') 
    return res


def register_College(req, data):
    res = {
        "fulfillmentMessages": [
            {
                "quickReplies": {
                    "title": 'Please name the institution you are forced go to everyday, we mean your school/college name',
                    "quickReplies": [
                        'KJSCE'
                    ]
                }
            },
        ]}
    print(res, 'Collegee')
    return res


def register_Year(req,data):
    res = {
        "fulfillmentMessages": [
            {
                "quickReplies": {
                    "title": 'How far have you managed to reach with regards to your education thus far? I.e. your year of study',
                    "quickReplies": [
                        'FY',
                        'SY',
                        'TY',
                        'LY'
                    ]
                }
            },
            {
                "telephonySynthesizeSpeech": {
                    "text": "Please state your year of study"
                }
            }
        ]
        }
    print(res, 'Studyyy')
    return res


def register_Branch(req,data):
    res = {
        "fulfillmentMessages": [
            {
                "quickReplies": {
                    "title": 'Great, so you\'re in ' + str(data[2][1]) + ',but..uhm...in which Branch?',
                    "quickReplies": [
                        'Comps',
                        'IT',
                        'EXTC',
                        'ETRX',
                        'Mech'
                    ]
                }
            },
            {
                "telephonySynthesizeSpeech": {
                    "text": "Last thing, helps me add more filters to my search parameters while stalking, your department/branch of study?"
                }
            }
        ]
    }
    print(res, 'Branchh')
    return res

def registered_success(req,data,img_url):
    # res = {
    #     "fulfillmentMessages": [
    #         {
                
    #             "text": {
    #                 "text": [
    #                     "Yayy!! you are successfully registered"
    #                 ]
    #             },
    #             "text": {
    #                 "text": [
    #                     "See you at the workshop!!"
    #                 ]
    #             },
    #             "quickReplies": {
    #                 "title": "In the mean time you could try my other features, Just ask me what the are ?",
    #                 "quickReplies": [
    #                     'What can you do?',
    #                     'Nehh you are useless!!'
    #                 ]
    #             }
    #         }
    #     ]
    # }

    res = {
        "fulfillmentMessages": [
            {
                "text": {
                    "text": [
                        "Yayy!! you are successfully registered"
                    ]
                }
            },
            {
                "text": {
                    "text": [
                        "See you at the workshop!!(I don't mean me, my council members will, after all, I'm just a bot😔"
                    ]
                }
            },
            {
                "image": {
                    "imageUri": img_url, #Aditya Wala Image
                    "accessibilityText": 'string'
                }
            },
            {
                "text": {
                    "text": [
                        "Your pass will be sent to your registered Email ID with futher instructions!!"
                    ]
                }
            },
            {
                "telephonySynthesizeSpeech": {
                    "text": "Awesome, so I'll just fill in the form for you quickly. Aaaaaaaand.....its done , you have been successfully registered for the event! \n Be there or be square◾ \n😊"
                }
            } 
        ] 
        }
    print(res, 'successs')
    return res


def registered_failed(req, data):
    res = {
        "fulfillmentMessages": [
            {
                "text": {
                    "text": [
                        "😓Registration Failed! Email ID already exists🤯"
                    ]
                }
            },
            
        ]
    }
    return res
