#!flask/bin/python
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/interactive")
def interactive():
    return render_template('interactive.html')

@app.route('/background_process')
def background_process():
	lang = request.args.get('proglang')
	if str(lang).lower() == 'python':
		return jsonify(result = 'You are wise!')
	else:
		return jsonify(result = 'Try again!')


if __name__ == '__main__':
    app.run(debug=True)