import json
import time
import requests
from twilio.rest import TwilioRestClient

def send_sms(temp):
    """Sends sms via Twilio"""

    # Write your twilio sid here
    ACCOUNT_SID = 'your_sid_key'

    #Write your twilio token here
    AUTH_TOKEN = 'your_token'

    #Write your body message here.
    body = "Temperature is cross threashold .Current temperature is %s " % temp

    #Write the number where you want to send sms. 
    to = 'your_number'

    #Write a from number that you will get from twilio
    from_number = 'number_from_twilio'
    
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body = body,
        to = to,
        from_ = from_number,
        )
    print message.sid
    res = str(message.sid)

    #retunring response of twilio
    return res

while True:
        time.sleep(5)
        # Replace api_key with your api key that you will get from bolt cloud
        # Replace device_name with your original device name
        response = requests.get('http://cloud.boltiot.com/remote/api_key/analogRead?pin=A0&deviceName=device_name')
        data = json.loads(response.text)
        if data['value'] > 10:
                print  "temperature is=", data['value']
                print "sending sms"
                send_sms(data['value'])
        else:
                print  "temperature is=", data['value']
                print "temperature is normal"
