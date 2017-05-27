#!/bin/bash

networksetup -setairportnetwork en1 goto_http://10.20.7.49:5000
sleep 20
curl -X GET http://169.254.109.1:5000/get_data > data.json
curl -H "Content-Type: application/text" POST -d "Hello everyone, this is the Red Cross. We are sending you this message to inform you that we will be saving your butts within the next hour so just hold on and try not to scream too much when a drone comes to pick up your message" http://169.254.109.1:5000/post_data
