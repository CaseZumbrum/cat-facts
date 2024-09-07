# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
import sys
import random
import time

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)

while(True):
    fileObj = open('facts.txt', "r") #opens the file in read mode
    list = fileObj.read().splitlines() #puts the file into an array
    facts = []
    fileObj.close()
    length = len(list)
    for x in range(0, length, 2):
            facts.append(list[x])

    randFact = random.choice(facts)

    fileObj = open('numbers.txt', "r") #opens the file in read mode
    numbers = fileObj.read().splitlines() #puts the file into an array
    fileObj.close()
    length = len(numbers)
    for x in range(0, length, 2):
        message = client.messages \
                    .create(
                        body=randFact,
                        from_ = '+18886599379',
                        to=numbers[x]
                    )
    time.sleep(86400)
