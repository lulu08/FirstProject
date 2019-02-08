from constance import config
import logging
from twilio.rest import Client
from django_twilio.utils import discover_twilio_credentials

logger = logging.getLogger('communication')

def send_sms(sms_details):
  """
      Reciveing dictionary of objects.
      {
        "message": "Payment link", 
        "number": "TO"
      }
  """

  try:
    account_sid = config.TWILIO_ACCOUNT_SID
    auth_token = config.TWILIO_AUTH_TOKEN
    twilio_phone_number = config.TWILIO_DEFAULT_CALLERID

    # Here we'll build a new Twilio_client with different credentials
    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
      body=sms_details['message'],
      to=sms_details['number'],
      from_=twilio_phone_number,
    )
  
  except Exception as e:
    print (e)
    logger.error("There's a error sending phone verification (reason: %s)" %
                    e.message)
