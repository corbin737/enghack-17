from wifi import Cell, Scheme
import requests
import email_lib
import json
import sys

text = "Stuff about safety and whatever else you want to say"

if __name__=="__main__":
    count = 1
    while True:
        wifi_list = Cell.all("wlan0")
        for i in wifi_list:
            if "goto_" in i.ssid():
                scheme = Scheme.for_cell("wlan0","home",i,"")
                scheme.save()
                scheme.activate()
                payload = {"content":[{"message": text}]}
                headers = {'content-type': 'application/json'}
                domain = ssid[14:]
                r = requests.post("http://" + domain + "/get_data", data=json.dumps(payload), headers=headers)
                file = open("Message" + str(count))
                file.write(r.text)
                file.close()
                count = count + 1
            elif "home_network" in i.ssid():
                for filename in os.listdir(directory):
                    input_file = open(filename)
                    input_message = ""
                    for line in input_file:
                    input_message += line
    
                    emails = json.loads(input_message)
                    for email in emails:
                    print "recipient: " + email['recipient']
                    print "message: " + email['message']
                    send_email(email['recipient'], email['message'])

                    deliver_emails('test_message.txt')
