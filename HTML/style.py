#!flask/bin/python
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/steinbeck")
def steinbeck():
    return render_template("steinbeck.html", awl=request.args.get("awl"), asl=request.args.get("asl"),
                           nr=request.args.get("nr"), vr=request.args.get("vr"), avr=request.args.get("avr"),
                           ajr=request.args.get("ajr"))


@app.route("/twain")
def twain():
    return render_template("twain.html", awl=request.args.get("awl"), asl=request.args.get("asl"),
                           nr=request.args.get("nr"), vr=request.args.get("vr"), avr=request.args.get("avr"),
                           ajr=request.args.get("ajr"))


@app.route("/shelley")
def shelley():
    return render_template("shelley.html", awl=request.args.get("awl"), asl=request.args.get("asl"),
                           nr=request.args.get("nr"), vr=request.args.get("vr"), avr=request.args.get("avr"),
                           ajr=request.args.get("ajr"))


@app.route("/austen")
def austen():
    return render_template("austen.html", awl=request.args.get("awl"), asl=request.args.get("asl"),
                           nr=request.args.get("nr"), vr=request.args.get("vr"), avr=request.args.get("avr"),
                           ajr=request.args.get("ajr"))


@app.route("/grimm")
def grimm():
    return render_template("grimm.html", awl=request.args.get("awl"), asl=request.args.get("asl"),
                           nr=request.args.get("nr"), vr=request.args.get("vr"), avr=request.args.get("avr"),
                           ajr=request.args.get("ajr"))


@app.route("/asimov")
def asimov():
    return render_template("asimov.html", awl=request.args.get("awl"), asl=request.args.get("asl"),
                           nr=request.args.get("nr"), vr=request.args.get("vr"), avr=request.args.get("avr"),
                           ajr=request.args.get("ajr"))


@app.route("/lovecraft")
def lovecraft():
    return render_template("lovecraft.html", awl=request.args.get("awl"), asl=request.args.get("asl"),
                           nr=request.args.get("nr"), vr=request.args.get("vr"), avr=request.args.get("avr"),
                           ajr=request.args.get("ajr"))


@app.route("/fitzgerald")
def fitzgerald():
    return render_template("fitzgerald.html", awl=request.args.get("awl"), asl=request.args.get("asl"),
                           nr=request.args.get("nr"), vr=request.args.get("vr"), avr=request.args.get("avr"),
                           ajr=request.args.get("ajr"))


@app.route("/hemingway")
def hemingway():
    return render_template("hemingway.html", awl=request.args.get("awl"), asl=request.args.get("asl"),
                           nr=request.args.get("nr"), vr=request.args.get("vr"), avr=request.args.get("avr"),
                           ajr=request.args.get("ajr"))


@app.route("/poe")
def poe():
    return render_template("poe.html", awl=request.args.get("awl"), asl=request.args.get("asl"),
                           nr=request.args.get("nr"), vr=request.args.get("vr"), avr=request.args.get("avr"),
                           ajr=request.args.get("ajr"))


@app.route("/lewis")
def lewis():
    return render_template("lewis.html", awl=request.args.get("awl"), asl=request.args.get("asl"),
                           nr=request.args.get("nr"), vr=request.args.get("vr"), avr=request.args.get("avr"),
                           ajr=request.args.get("ajr"))


@app.route("/clarke")
def clark():
    return render_template("clarke.html", awl=request.args.get("awl"), asl=request.args.get("asl"),
                           nr=request.args.get("nr"), vr=request.args.get("vr"), avr=request.args.get("avr"),
                           ajr=request.args.get("ajr"))


@app.route("/christie")
def christie():
    return render_template("christie.html", awl=request.args.get("awl"), asl=request.args.get("asl"),
                           nr=request.args.get("nr"), vr=request.args.get("vr"), avr=request.args.get("avr"),
                           ajr=request.args.get("ajr"))


@app.route("/style")
def get_input():
    return render_template('homePage.html')


@app.route("/style", methods=["GET", "POST"])
def result():
    data = request.form.get('text')
    style = [data, "1", "2", "3", "4", "5", "6"]
    if style[0] == "John Steinbeck":
        return redirect(url_for("steinbeck", awl=style[1], asl=style[2], nr=style[3], vr=style[4], avr=style[5],
                                ajr=style[6]))
    elif style[0] == "Mark Twain":
        return redirect(url_for("twain", awl=style[1], asl=style[2], nr=style[3], vr=style[4], avr=style[5],
                                ajr=style[6]))
    elif style[0] == "Mary Shelley":
        return redirect(url_for("shelley", awl=style[1], asl=style[2], nr=style[3], vr=style[4], avr=style[5],
                                ajr=style[6]))
    elif style[0] == "Jane Austen":
        return redirect(url_for("austen", awl=style[1], asl=style[2], nr=style[3], vr=style[4], avr=style[5],
                                ajr=style[6]))
    elif style[0] == "Jacob Grimm and Wilhelm Grimm":
        return redirect(url_for("grimm", awl=style[1], asl=style[2], nr=style[3], vr=style[4], avr=style[5],
                                ajr=style[6]))
    elif style[0] == "Issac Asimov":
        return redirect(url_for("asimov", awl=style[1], asl=style[2], nr=style[3], vr=style[4], avr=style[5],
                                ajr=style[6]))
    elif style[0] == "H.P lovecraft":
        return redirect(url_for("lovecraft", awl=style[1], asl=style[2], nr=style[3], vr=style[4], avr=style[5],
                                ajr=style[6]))
    elif style[0] == "F Scott Fitzgerald":
        return redirect(url_for("fitzgerald", awl=style[1], asl=style[2], nr=style[3], vr=style[4], avr=style[5],
                                ajr=style[6]))
    elif style[0] == "Ernest Hemingway":
        return redirect(url_for("hemingway", awl=style[1], asl=style[2], nr=style[3], vr=style[4], avr=style[5],
                                ajr=style[6]))
    elif style[0] == "Edgar Allan Poe":
        return redirect(url_for("poe", awl=style[1], asl=style[2], nr=style[3], vr=style[4], avr=style[5],
                                ajr=style[6]))
    elif style[0] == "CS Lewis":
        return redirect(url_for("lewis", awl=style[1], asl=style[2], nr=style[3], vr=style[4], avr=style[5],
                                ajr=style[6]))
    elif style[0] == "Arthur C Clark":
        return redirect(url_for("clarke", awl=style[1], asl=style[2], nr=style[3], vr=style[4], avr=style[5],
                                ajr=style[6]))
    elif style[0] == "Agatha Christie":
        return redirect(url_for("christie", awl=style[1], asl=style[2], nr=style[3], vr=style[4], avr=style[5],
                                ajr=style[6]))


if __name__ == '__main__':
    app.run(debug=True)