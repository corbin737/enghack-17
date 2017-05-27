from wifi import Cell, Scheme
import requests
import email_lib
import json
import sys
import os

text = "Stuff about safety and whatever else you want to say"

if __name__=="__main__":

    for filename in os.listdir('./'):
        if '.json' in filename:
            email_lib.deliver_emails(filename)
            print('success')
