import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

twilio_sid = os.getenv("TWILIO_SID")
twilio_secret = os.getenv("TWILIO_SECRET")

client = Client(twilio_sid, twilio_secret)

my_number = os.getenv("MY_NUMBER")
other_number = os.getenv("FROM")

body = "Hello Universo, test twilio, Zplit app."

message_twilio = client.messages.create(
    body=body,
    from_=my_number,
    to=other_number
)

print("Msg enviado ...")
