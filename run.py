#!flask/bin/python
from app import app

import threading, webbrowser
threading.Timer(1.25, lambda: webbrowser.open('http://127.0.0.1:5000')).start()

app.run(debug=True)
