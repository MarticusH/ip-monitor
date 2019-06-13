# This script needs to be filled in with variables in send_email() function
# Otherwise, the script writes a file to current directory for its "most recent" public IP value
# Script assumes we're using GMail to send notification emails

import smtplib
import logging
from datetime import datetime
import requests

def send_email(ip):
  # SMTP account credentials
  username = '<user_account>'
  password = '<user_password>'
  from_name = '<from_name_anything_you_want>'
  sender = '<email>@gmail.com'

  # Recipient email address (could be same as from_addr)
  recipient = '<recipient>'

  # Subject line for email
  subject = 'IP Address Changed'

  senddate = datetime.strftime(datetime.now(), '%Y-%m-%d')
  m = "Date: %s\r\nFrom: %s <%s>\r\nTo: %s\r\nSubject: %s\r\nX-Mailer: My-Mail\r\n\r\n" % (
  senddate, from_name, sender, recipient, subject)
  server = smtplib.SMTP('smtp.gmail.com:587')
  server.starttls()
  server.login(username, password)
  server.sendmail(sender, recipient, m + ip)
  server.quit()
  return;

def main():
  f = open('./current_ip','r+')
  currentIP = f.read()
  ipResponse = ((requests.get('https://ifconfig.co/ip')).text).rstrip()
  f.close()
  if currentIP != ipResponse:
#    print('It is different')
    f = open('./current_ip','w')
    send_email(ipResponse)
    f.write(ipResponse)
    f.close()

if __name__ == "__main__":
    main()
