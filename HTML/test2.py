#!flask/bin/python
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/style", methods=["GET"])
def get_input():
    return render_template('testWeb2.html')


@app.route("/style", methods=["POST"])
def get_data():
    data = request.form.get('text')
    return "Awesome," + data


if __name__ == '__main__':
    app.run(debug=True)