from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/home")
def home2():
    return render_template("index.html")
@app.route("/History/")
def history():
    return render_template('history.html')

@app.route("/History/<start>/<end>")
def history(start,end):
    return render_template('history.html', start=start, end=end)

if __name__ == "__main__":
    app.run(debug=True)  #to je