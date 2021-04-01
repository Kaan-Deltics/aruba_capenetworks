#!/usr/bin/python2
import json
import sys
import getopt
import urllib
import requests

#def help():
#    print ("Display help!!!")

full_cmd_arguments = sys.argv
argument_list = full_cmd_arguments[1:]

short_options = "n:i:k:u:vh"
long_options = ["node=", "appid=", "appkey=", "url=", "verbose", "help"]

try:
    arguments, values = getopt.getopt(argument_list, short_options, long_options)
except getopt.error as err:
    # Output error, and return with an error code
    print (str(err))
    sys.exit(2)

# Evaluate given options
for current_argument, current_value in arguments:
    if current_argument in ("-v", "--verbose"):
        print ("Enabling verbose mode")
    elif current_argument in ("-h", "--help"):
        print ("Displaying help")
    elif current_argument in ("-n", "--node"):
        node = (current_value)
#        if(len(node) == 0):
#           print ("Yes")
#        else :
#           help()
    elif current_argument in ("-i", "--appid"):
        appids = (current_value)
    elif current_argument in ("-k", "--appkey"):
        appkey = (current_value)
    elif current_argument in ("-u", "--url"):
        url = (current_value)


url = "https://api.capenetworks.com/v1/nodes/"
url2 = url+node
headers = {'accept': 'application/json', 'X-API-KEY': appkey, 'X-APP-ID': appids}
t = requests.get(url2, headers=headers)
r_dictionary= t.json()

for p in r_dictionary['payload']['state_summary']['sensors']:
        name = p['name']
        state = p['state']
        if state == "good":
#            print("OK:" + str(name), "status is:", + str(state))
            print "OK: " + str(name), " status is: " + str(state)
        else:
            print "CRITICAL: " + str(name), "status is " + str(state)
