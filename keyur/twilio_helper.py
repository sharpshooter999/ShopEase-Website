# from twilio.rest import Client

# # Replace with your actual credentials
# account_sid = "your_account_sid"
# auth_token = "your_auth_token"

# client = Client(account_sid, auth_token)

# def send_sms(to, message):
#     message = client.messages.create(
#         body=message,
#         from_="your_registered_sender_id",  # Must be pre-approved in DLT
#         to=to  # Recipient's phone number
#     )
#     return message.sid

# # Test sending SMS
# send_sms("+91XXXXXXXXXX", "Your OTP is 123456")

