
# import flask dependencies
##from flask import Flask
##import os

#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response
from flask import jsonify

import psycopg2
import urllib.parse
import time


from Mixess.process_request import make_simple_message, get_quick_request, get_github_profile #, get_request

# initialize the flask app
app = Flask(__name__)

# default route
@app.route('/')
def index():
    return '-->'

# create a route for webhook
##@app.route('/webhook')
##def hello():
##    return 'Hello World!'

mixess_search_url = "https://mixess.jp/s/"

@app.route('/webhook', methods=['POST'])
def webhook():
    #start time calc
    start = time.time()
    req = request.get_json(silent=True, force=True)

    print("\nStart of everything--> \n\n Request:")
    print(json.dumps(req, indent=4))

    ####res = makeWebhookResult(req)
    #res = "hello" #= req #test April2019
    email, int_name = get_quick_request(req)
    print ("email is: ", email)

    github_account = get_github_profile(str(email))


    speech = "Ok, here it is what I found. For Email: '" + email + "', the Github account is: " + github_account
    rep1 = "yes"
    rep2 = "no"
    replies = [rep1, rep2] 
    res = make_simple_message(speech, replies)
    res = jsonify(res)
    ####res = jsonify(res) #using jsonify
    end = time.time()
    return res

def makeWebhookResult(req):

    # parsing parameters
    # result        = req.get("result")
    # parameters    = result.get("parameters")
    # resolvedQuery = result.get("resolvedQuery")
    # action        = result.get("action")  # "travel.travel-map-move"

    #int_name, attraction, city, the_type, sp_area, name, conindex, conaddress = get_quick_request(req)
    return 

# run the app
if __name__ == '__main__':
   #app.run()
   port = int(os.getenv('PORT', 5000))

   print ("Starting app on port %d" % (port))

   app.run(debug=True, port=port, host='0.0.0.0')

