import urllib
#import jsonpickle

import json
import os

from flask import Flask
from flask import request
from flask import make_response
from flask import jsonify

import psycopg2
import urllib.parse
import time
import urllib
from urllib.request import urlopen





#API v2
def make_simple_message(speech, replies):
    '''
    return {
        "fulfillmentText": speech,
        "fulfillmentMessages":[
            {
                "type": 2,
                "title": speech,
                "replies": replies
                }
            ]
        }
        '''
    return {

        "fulfillmentText": speech,
        "fulfillmentMessages": [
            {
                "text": {
                    "text": [
                        speech
                    ]
                }
            }
        ],

    }



def get_quick_request(req): #hatem
    #-->#Mar2019#print_OFF#print("-----test__get_quick_request-------")
    # API_2
    # use this link for json file understanding
    result        = req.get("queryResult")  # API2-change
    parameters    = result.get("parameters")
    # resolvedQuery = result.get("resolvedQuery")
    resolvedQuery = result.get("queryText")  # API2-change

    #outputContexts = result.get("outputContexts")
    intent = result.get("intent")

    try: int_name = intent.get("displayName")
    except: int_name = ""

    # required parameters

    email       = parameters.get("email")

    #city       = parameters.get("city")
    #attraction = parameters.get("attraction")
    #the_type   = parameters.get("the_type")
    #sp_area    = parameters.get("sp_area")

    #####################################################
    ## Dec 2018
    #conparametersi = get_conparametersi(outputContexts)
    #####################################################

    #try: name            = outputContexts[0].get("name") ###= conparametersi.get("name") ###= outputContexts[0].get("name")
    #except: name         = ""

    #try: conaddress      = int(conparameters.get("conaddress")) ###= int(conparametersi.get("conaddress")) ###= int(conparameters.get("conaddress"))
    #except: conaddress   = "" # hatem

    #try: conindex        = int(conparameters.get("conindex")) ###= int(conparametersi.get("conindex")) ###= int(conparameters.get("conindex"))
    #except: conindex     = 0 # hatem
    #-->#Mar2019#print_OFF#print("~~~~~~~~~~~~~~ from inside_quick_request outputContexts, name is: " + name + "~~~~~~~~~~~~~~~~~~~~~~~~")
    return email, int_name
    ##################################################




def get_github_profile(email):

        #https://api.github.com/search/users?q=solankiarpit1997@gmail.com

        base_url            = "https://api.github.com/search/users?q="
        #ending_url          = "+in:email&type=Users"
        #email = sys.argv[1] #input from outside
        #email               = "ha_wasfy@yahoo.com"
        result_start_url    = "https://github.com"
        site_url =  base_url + email



        #info_by_user_name = "https://api.github.com/users/hatemwasfy"
        #https://api.github.com/search/users?q=ha_wasfy@yahoo.com

        '''
        print("-------------------------------------------------------")
        print("email is: ", email)
        print("site URL is: ", site_url)
        print("-------------------------------------------------------")
        '''
        try:
                with urlopen(site_url) as url:
                        data = json.loads(url.read().decode())
                        print("data inside try is: ", str(data))
                        #print(data["items"][0]["html_url"]) # "login" is login name only

                        user_github_account = data["items"][0]["html_url"]

                        print("user_account_inside_try: ", user_github_account)
        except:
                        user_github_account = "Not found"

        #print("Github account is: ", user_github_account)

        return user_github_account


