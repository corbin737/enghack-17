#!/bin/bash

networksetup -setairportnetwork en1 goto_http://169.254.165.146:5000
sleep 20
curl -X GET http://169.254.109.1:5000/get_data > data.json

