from twilio.rest import Client

TWILIO_SID = "AC07bda8701e086496344ea9ef6cd2c66f"
TWILIO_AUTH_TOKEN = "d348a3f43599cec6bfc5e94b6045bbfb"
TWILIO_VIRTUAL_NUMBER = "+18507838237"
TWILIO_VERIFIED_NUMBER = "+19144827441"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
