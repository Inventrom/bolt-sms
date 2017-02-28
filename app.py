from flask import (json)
import time
import requests
from twilio.rest import TwilioRestClient

def send_sms(temp):
    """Sends sms via Twilio"""
    sid='your_sid_key'
    token='your_token'
    body= "Temperature is cross threashold .Current temperature is %s " % temp
    to= 'your_number'
    from_number= 'number_from_twilio'
    ACCOUNT_SID = sid
    AUTH_TOKEN = token
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body=body,
        to=to,
        from_=from_number,
        )
    print message.sid
    res = str(message.sid)
    return res

while True:
        time.sleep(5)
        response = requests.get('http://cloud.boltiot.com/remote/768d64d5-05b2-463b-95bc-98eedfc5abe7/analogRead?pin=A0&deviceName=BOLT291064')
        data = json.loads(response.text)
        if data['value'] > 10:
                print  "temperature is=", data['value']
                print "sending sms"
                send_sms(data['value'])
        else:
                print  "temperature is=", data['value']
                print "temperature is normal"
