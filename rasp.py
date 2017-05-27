from wifi import Cell, Scheme
import requests

if __name__=="__main__":
    count = 1
    while True:
        wifi_list = Cell.all('wlan0')
        for i in wifi_list:
            if "goto_" in i.ssid():
                scheme = Scheme.for_cell("wlan0","home",i,"")
                scheme.save()
                scheme.activate()
                domain = i.replace("goto_", "")
                r = requests.get("http://" + domain)
                file = open("Message" + str(count))
                file.write(r.text)
                file.close()
                count = count + 1
