#!flask/bin/python
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/steinbeck")
def steinbeck():
    error = "Nice"
    return render_template("steinbeck.html", error=error)


@app.route("/twain")
def twain():
    return render_template("twain.html")


@app.route("/shelley")
def shelley():
    return render_template("shelley.html")


@app.route("/austen")
def austen():
    return render_template("austen.html")


@app.route("/grimm")
def grimm():
    return render_template("grimm.html")


@app.route("/asimov")
def asimov():
    return render_template("asimov.html")


@app.route("/lovecraft")
def lovecraft():
    return render_template("lovecraft.html")


@app.route("/fitzgerald")
def fitzgerald():
    return render_template("fitzgerald.html")


@app.route("/hemingway")
def hemingway():
    return render_template("hemingway.html")


@app.route("/poe")
def poe():
    return render_template("poe.html")


@app.route("/lewis")
def lewis():
    return render_template("lewis.html")


@app.route("/clark")
def clark():
    return render_template("clark.html")


@app.route("/christie")
def christie():
    return render_template("christie.html")


@app.route("/style")
def get_input():
    return render_template('homePage.html')


@app.route("/style", methods=["GET", "POST"])
def result():
    data = request.form.get('text')
    if data == "steinbeck":
        return redirect(url_for("steinbeck"))
    elif data == "twain":
        return redirect(url_for("twain"))
    elif data == "shelley":
        return redirect(url_for("shelley"))
    elif data == "austen":
        return redirect(url_for("austen"))
    elif data == "grimm":
        return redirect(url_for("grimm"))
    elif data == "asimov":
        return redirect(url_for("asimov"))
    elif data == "lovecraft":
        return redirect(url_for("lovecraft"))
    elif data == "fitzgerald":
        return redirect(url_for("fitzgerald"))
    elif data == "hemingway":
        return redirect(url_for("hemingway"))
    elif data == "poe":
        return redirect(url_for("poe"))
    elif data == "lewis":
        return redirect(url_for("lewis"))
    elif data == "clark":
        return redirect(url_for("clark"))
    elif data == "christie":
        return redirect(url_for("christie"))


if __name__ == '__main__':
    app.run(debug=True)