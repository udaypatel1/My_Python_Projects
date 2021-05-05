my_cell = ''

my_twilio = ''
account_sid = ''
auth_token = ''


from twilio.rest import Client


client = Client(account_sid, auth_token)

my_msg = "Hey"

message = client.messages.create(to=my_cell, from_=my_twilio, body=my_msg)



