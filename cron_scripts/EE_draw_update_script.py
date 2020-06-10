import requests
import json

# NOTIFYR CONFIG
send_mail_url = 'http://localhost:8001/send_email'
subject = "Express Entry Page Update"
body = "Express Entry Update<br> Please check the following link<br><a href='https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/express-entry/submit-profile/rounds-invitations.html'>https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/express-entry/submit-profile/rounds-invitations.html</a>"
mail_to = ["email@gmail.com"]
cc_to = []


URL = 'https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/express-entry/submit-profile/rounds-invitations.html'
page = requests.get(URL)

new_content = str(page.content)
start_text = 'Results: Rounds of invitations'
end_text = 'See previous rounds'
new_content_updated = new_content[new_content.index(start_text):new_content.index(end_text)]


f = open("EE/old_file_content.txt", "r")
old_file_content = f.read()


if old_file_content != new_content_updated:
	
	payload = { "subject": subject, "body": body, "to": mail_to, "cc": cc_to }
	r = requests.post(send_mail_url, json = payload)
	print(r.text, "mail sent")

	f = open("EE/old_file_content.txt", "w")
	f.write(new_content_updated)
	f.close()
else:
	print("no updates")
