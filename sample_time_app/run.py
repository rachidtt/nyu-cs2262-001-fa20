from flask import Flask
import datetime
app = Flask(__name__)


@app.route('/')
def hello_world():
	time= datetime.datetime.now().strftime("%I:%M %p , %B %d, %Y")
	
	return time

app.run(host='0.0.0.0',
        port=8080,
        debug=True)