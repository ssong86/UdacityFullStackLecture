from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACbf72433536d4663d4ba971c1d6b73a96"
# Your Auth Token from twilio.com/console
auth_token  = "49088d2af7122a807db39951f1318c05"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+14157456042", # my phone
    from_="+16507310351", # twilio account phone
    body="Hello from Python!")

print(message.sid)
