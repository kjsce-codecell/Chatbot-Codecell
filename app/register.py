
def register_Name(req,data):
    res = {"fulfillmentMessages": [
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
                    "First let's start with an easy one \n What's your Name?"
                ]
            }
        }
    ]}
    print(res,'Nameeee')
    return res


def register_Email(req,data):
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
        }
    ]}
    print(res, 'Emaill') 
    return res


def register_Study(req,data):
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
                "image": {
                    "imageUri": 'https://media.giphy.com/media/11J8lEFfvHLipi/giphy.gif',
                    "accessibilityText": 'string'
             }
            },
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
                "quickReplies": {
                    "title": "In the mean time you could try my other features, Just ask me what they are ?",
                    "quickReplies": [
                        'What can you do?',
                        'Nehh you are useless!!'
                    ]
                }
            }
        ] 
        }
    print(res, 'successs')
    return res
