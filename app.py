from flask import Flask, render_template, request
from datetime import datetime, timedelta

app = Flask(__name__)

titlestring = 'PDT'

@app.route("/")
def hello():
   now = datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M:%S")
   templateData = {
       'title': titlestring,
       'time': timeString
   }
   return render_template('index.html', **templateData)


@app.route("/<action>")
def action(action):
   now = datetime.now()
   if action == 'westCoast':
   	now = now
   	titlestring = 'PDT'
   if action == 'eastCoast':
   	now = now + timedelta(hours = 3)
   	titlestring = 'EDT'
   timeString = now.strftime("%Y-%m-%d %H:%M:%S")
   templateData = {
       'title': titlestring,
       'time': timeString
   }
   return render_template('index.html', **templateData)


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
