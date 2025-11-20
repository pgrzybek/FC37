from flask import Flask, render_template
from dbInit import db
from KontoEncja import KontoEncja

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///konto.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# Tworzenie bazy na starcie
with app.app_context():
    db.create_all()
    print("OK — baza utworzona, tabele gotowe.")

# @app.route("/")
# def index():
#     return "Aplikacja działa"


@app.route("/")
def pokaz_konto():
    konto = db.session.get(KontoEncja, 1)
    if konto is None:
        konto = KontoEncja(saldo=500)
        db.session.add(konto)
        db.session.commit()

    return render_template("konto.html", konto=konto)

if __name__ == "__main__":
    app.run(debug=True)
