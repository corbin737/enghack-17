from wifi import Cell, Scheme
import requests
import subprocess

if __name__=="__main__":
    results = subprocess.check_output(["netsh", "wlan", "show", "network"])
    results = results.decode("ascii") # needed in python 3
    results = results.replace("\r","")
    ls = results.split("\n")
    ls = ls[4:]
    ssids = []
    x = 0
    while x < len(ls):
        if x % 5 == 0:
            ssids.append(ls[x])
        x += 1
    for ssid in ssids:
            if "goto_" in ssid:
                domain = ssid[14:]
                r = requests.get("http://" + domain + "/get_data")
                print r
                # file = open("Message" + str(count))
                # file.write(r.text)
                # file.close()
                # count = count + 1
