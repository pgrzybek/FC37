from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/wynik", methods=["POST"])
def wynik():
    imie = request.form["imie"]  # pobiera dane z formularza
    return f"Witaj {imie}, dane dotarły do Pythona!"


if __name__ == "__main__":
    app.run(debug=True)
