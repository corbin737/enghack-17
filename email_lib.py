"""
Functions:
send_email(to_email, text, (optional subject))
get_all_emails() returns all emails as dictionaries with date_time, subject, from_name, from_address, text and email id
delete_email(email_id)
"""

import smtplib
import time
import imaplib
import email
import datetime
import json

from email_password import getPassword

imap_server = "imap.gmail.com"
smtp_server = 'smtp.gmail.com:587'
address = 'emailbuffer2@gmail.com'
password = getPassword()


def send_email(recipient, text, subject=0):
    try:
        server = smtplib.SMTP(smtp_server)
        server.starttls()
        server.login(address,password)
        print "server logged in"
        message = ""
        try:
            message += "Subject : " + subject + "\n"
        except:
            print "No added subject"

        message += text

        print message
        server.sendmail(address, recipient, message)
        server.quit()
        return True
    except Exception, e:
        print e
        return False


def get_all_emails():
    def parce_email(msg, id):

        message = ""
        for part in msg.walk():
            if part.get_content_type() == 'text/plain':
                message += part.get_payload(decode = True)

        from_line = msg['from'].split(" ")
        from_name = ""
        for word in from_line:
            if word[0] == "<":
                from_address = word[1:-1]
            else:
                from_name += word + " "

        from_name = from_name[:-1]

        date_tuple = email.utils.parsedate_tz(msg['date'])
        if date_tuple:
          local_date = datetime.datetime.fromtimestamp(email.utils.mktime_tz(date_tuple))

        return {"date_time":local_date, "subject": msg['subject'], "from_name": from_name, "from_address":from_address, "text": message, "id":id}

    all_emails = []
    try:
        mail = imaplib.IMAP4_SSL(imap_server)
        mail.login(address,password)
        mail.select('inbox')

        print "Got into the inbox"

        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]

        id_list = mail_ids.split()


        for i in id_list:
            try:
                typ, data = mail.fetch(i, '(RFC822)' )
                for response_part in data:
                    if isinstance(response_part, tuple):
                        msg = email.message_from_string(response_part[1])
                        all_emails.append(parce_email(msg, i))
            except Exception, e:
                print str(e)


    except Exception, e:
        print str(e)

    return all_emails

def delete_email(email_id):
    mail = imaplib.IMAP4_SSL(imap_server)
    mail.login(address,password)
    mail.select('inbox')
    mail.store(str(email_id) , '+FLAGS', '(\Deleted)')
    mail.expunge()
    mail.close()
    mail.logout()

def deliver_emails(file_path):
    input_file = open(file_path)
    input_message = ""
    for line in input_file:
        input_message += line

    emails = json.loads(input_message)
    for email in emails:
        print "recipient: " + email['recipient']
        print "message: " + email['message']
        send_email(email['recipient'], email['message'])

deliver_emails('test_message.txt')
