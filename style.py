#!flask/bin/python
from __future__ import division
from flask import Flask, render_template, request, redirect, url_for
import nltk
import pandas as pd
from sklearn.externals import joblib
app = Flask(__name__)

# direct user to author page with user statistics

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
def clarke():
    return render_template("clarke.html", awl=request.args.get("awl"), asl=request.args.get("asl"),
                           nr=request.args.get("nr"), vr=request.args.get("vr"), avr=request.args.get("avr"),
                           ajr=request.args.get("ajr"))


@app.route("/christie")
def christie():
    return render_template("christie.html", awl=request.args.get("awl"), asl=request.args.get("asl"),
                           nr=request.args.get("nr"), vr=request.args.get("vr"), avr=request.args.get("avr"),
                           ajr=request.args.get("ajr"))


# directs to homepage
@app.route("/style")
def get_input():
    return render_template('homePage.html')

# processing text
@app.route("/style", methods=["GET", "POST"])
def result():
    # get text from textbox
    data = request.form.get('text')

    totalwords = []
    totalsent = []
    totaltags = []
    sentcount = 0

    # tokenize into sentences
    sentences = nltk.sent_tokenize(data)

    # tokenize into words and create part of speech tags
    for sentence in sentences:
        totalsent.append(sentence)
        sentcount = sentcount + 1
        words = nltk.word_tokenize(sentence)
        for word in words:
            totalwords.append(word)
        tagged = nltk.pos_tag(words)
        for tag in tagged:
            totaltags.append(tag)
            string = nltk.tuple2str(tag)

    # calculate word and sentence average
    waverage = sum(len(word) for word in totalwords) / len(totalwords)
    wtrunc = '%.3f' % (waverage)
    saverage = len(totalwords) / sentcount
    strunc = '%.3f' % (saverage)

    # add up total number of pos tags
    NNtags = []
    VBDtags = []
    JJtags = []
    RBtags = []
    punctags = []
    for x in totaltags:
        if x[1] == 'NN':
            NNtags.append(x)
        elif x[1] == 'VBD':
            VBDtags.append(x)
        elif x[1] == 'JJ':
            JJtags.append(x)
        elif x[1] == 'RB':
            RBtags.append(x)
        elif x[1] == "." or "," or ";" or "-":
            punctags.append(x)

    # calculate part of speech ratios
    punctratio = len(punctags) / len(totalwords)
    NNratio = len(NNtags) / len(totalwords)
    VBDratio = len(VBDtags) / len(totalwords)
    JJratio = len(JJtags) / len(totalwords)
    RBratio = len(RBtags) / len(totalwords)

    # truncate to 3 decimal places and add %
    NNratio = NNratio * 100
    ntrunc = '%.3f' % (NNratio)
    VBDratio = VBDratio * 100
    vtrunc = '%.3f' % (VBDratio)
    JJratio = JJratio * 100
    jtrunc = '%.3f' % (JJratio)
    RBratio = RBratio * 100
    rtrunc = '%.3f' % (RBratio)

    # create csv for machine learning model
    open('user.csv', 'w').close()  # erase file
    download_dir = "user.csv"
    csv = open(download_dir, "a")
    columnTitleRow = "author,avgword,avgsent,punctratio,nnratio,vbdratio,rbratio,jjratio\n"
    csv.write(columnTitleRow)
    row = "user," + str(waverage) + "," + str(saverage) + "," + str(punctratio) + "," + str(NNratio) + "," + str(VBDratio) + "," + str(
        RBratio) + "," + str(JJratio) + "\n"
    csv.write(row)
    csv.close()

    # use already generated pickle file to predict author
    test_file = "user.csv"
    df1 = pd.read_csv(test_file, header=0)
    test_data = df1.iloc[:, 1:]
    model2 = joblib.load("file.pkl")
    preds2 = model2.predict(test_data)

    # put author guess and stats into an array
    response = []
    response.append(preds2[0])
    response.append(str(wtrunc))
    response.append(str(strunc))
    response.append(str(ntrunc) + "%")
    response.append(str(vtrunc) + "%")
    response.append(str(rtrunc) + "%")
    response.append(str(jtrunc) + "%")

    # redirecting to appropriate author function with the user stats
    if response[0] == "John Steinbeck":
        return redirect(url_for("steinbeck", awl=response[1], asl=response[2], nr=response[3], vr=response[4], avr=response[5],
                                ajr=response[6]))
    elif response[0] == "Mark Twain":
        return redirect(url_for("twain", awl=response[1], asl=response[2], nr=response[3], vr=response[4], avr=response[5],
                                ajr=response[6]))
    elif response[0] == "Mary Shelley":
        return redirect(url_for("shelley", awl=response[1], asl=response[2], nr=response[3], vr=response[4], avr=response[5],
                                ajr=response[6]))
    elif response[0] == "Jane Austen":
        return redirect(url_for("austen", awl=response[1], asl=response[2], nr=response[3], vr=response[4], avr=response[5],
                                ajr=response[6]))
    elif response[0] == "Jacob Grimm and Wilhelm Grimm":
        return redirect(url_for("grimm", awl=response[1], asl=response[2], nr=response[3], vr=response[4], avr=response[5],
                                ajr=response[6]))
    elif response[0] == "Issac Asimov":
        return redirect(url_for("asimov", awl=response[1], asl=response[2], nr=response[3], vr=response[4], avr=response[5],
                                ajr=response[6]))
    elif response[0] == "H.P lovecraft":
        return redirect(url_for("lovecraft", awl=response[1], asl=response[2], nr=response[3], vr=response[4], avr=response[5],
                                ajr=response[6]))
    elif response[0] == "F Scott Fitzgerald":
        return redirect(url_for("fitzgerald", awl=response[1], asl=response[2], nr=response[3], vr=response[4], avr=response[5],
                                ajr=response[6]))
    elif response[0] == "Ernest Hemingway":
        return redirect(url_for("hemingway", awl=response[1], asl=response[2], nr=response[3], vr=response[4], avr=response[5],
                                ajr=response[6]))
    elif response[0] == "Edgar Allan Poe":
        return redirect(url_for("poe", awl=response[1], asl=response[2], nr=response[3], vr=response[4], avr=response[5],
                                ajr=response[6]))
    elif response[0] == "CS Lewis":
        return redirect(url_for("lewis", awl=response[1], asl=response[2], nr=response[3], vr=response[4], avr=response[5],
                                ajr=response[6]))
    elif response[0] == "Arthur C Clark":
        return redirect(url_for("clarke", awl=response[1], asl=response[2], nr=response[3], vr=response[4], avr=response[5],
                                ajr=response[6]))
    elif response[0] == "Agatha Christie":
        return redirect(url_for("christie", awl=response[1], asl=response[2], nr=response[3], vr=response[4], avr=response[5],
                                ajr=response[6]))
    return (response)


if __name__ == '__main__':
    app.run(debug=True)
