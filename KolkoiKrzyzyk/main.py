from flask import Flask, render_template, request
from datetime import datetime


app = Flask(__name__)

@app.route("/")
def home():
    state1=""
    state2=""
    state3=""
    state4=""
    state5=""
    state6=""
    state7=""
    state8=""
    state9=""
    return render_template("index.html", state1=state1, state2=state2, state3=state3, state4=state4, state5=state5, state6=state6, state7=state7, state8=state8, state9=state9 )

@app.route("/wynik", methods=["POST"])
def wynik():
    pass

if __name__ == "__main__":
    app.run(debug=True)  #to jest uruchamianie lokalnie
    #from waitress import serve
    #serve(app, host='0.0.0.0', port=8080)# http://127.0.0.1:8080/ lokalny port uruchomiony