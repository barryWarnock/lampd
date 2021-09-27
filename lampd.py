import requests
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/lamp', methods=['GET', 'POST'])
def lamp():
    response = None
    if request.method == 'POST':
        response = requests.get("http://192.168.1.85/cm?cmnd=Power%20TOGGLE")
    else:
        response = requests.get("http://192.168.1.85/cm?cmnd=Power")
    if response.text.find("ON") != -1:
        return 'on'
    else:
        return 'off'

@app.route('/')
def ui():
    return render_template('lamp.html')

if __name__ == '__main__':
    app.run(port=1420)
