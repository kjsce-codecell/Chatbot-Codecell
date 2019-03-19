
def register_Name(req,data):
    res = {"fulfillmentMessages": [
        {
            "image": {
                "imageUri": 'https://wow.olympus.eu/webfile/img/1632/x=1024/oly_testwow_stage.jpg', #Replace with current poster
                "accessibilityText": 'Event Poster'
            }
        },
        {
            "text": {
                "text": [
                    "Lets get you registered Quickly!!"
                ]
            }
        },
        {
            "text": {
                "text": [
                    "I just need to ask you a few questions first"
                ]
            }
        },
        {
            "text": {
                "text": [
                    "First let's start with an easy one \nWhat's your Name?"
                ]
            }
        }, 
        {
            "telephonySynthesizeSpeech": {
                "text": "To get you registered i would like to know some details.First of all please tell me your good name."
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
                    "Hey there " + str(data[0][1])
                ]
            }
        },
        {
            "text": {
                "text": [
                    "Oh I also need your Email ID" 
                ]
            }
        },
        {
            "telephonySynthesizeSpeech": {
                "text": "Ok so hey " + str(data[0][1]) + "Now moving on what's your email id"
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
                    "title": 'Which school/college do you study in?',
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
                    "title": 'Btw which year do you study in?',
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
                    "text": "Ok superb , which year do you study in?"
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
                    "title": 'Accha so u in ' + str(data[3][1]) + 'but in which Branch ?',
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
                    "text": "And one last thing which department are you in?"
                }
            }
        ]
    }
    print(res, 'Branchh')
    return res

def registered_success(req,data):
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
                        "See you at the workshop!!"
                    ]
                }
            },
            {
                "image": {
                    "imageUri": 'https://media.giphy.com/media/11J8lEFfvHLipi/giphy.gif', #Aditya Wala Image
                    "accessibilityText": 'string'
                }
            },
            {
                "text": {
                    "text": [
                        "Pass has been sent to your Registered Email ID with futher Instructions!!"
                    ]
                }
            },
            {
                "telephonySynthesizeSpeech": {
                    "text": "Awesome so i'll just fill in the form for you quickly.And its done , you have successfully registered for the event , meet you there!"
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
