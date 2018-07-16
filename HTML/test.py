from flask import Flask
from flask import request
app = Flask(__name__)
 
@app.route("https://people.ucsc.edu/~krschuma/test.py", method = {"POST"})
def text():
	if request.method == "POST":
		data = request.jason['text']
	return data