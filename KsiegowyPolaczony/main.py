from flask import Flask, render_template, request
from Manager import Manager
from dbInit import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db.init_app(app)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/home")
def home2():
    return render_template("index.html")

@app.route("/history/")
def history():
    operacje=m.execute("p","","","")

    return render_template('history.html',operacje=operacje)
#
@app.route("/history/<start>/<end>")
def historyDetail(start,end):
    result = m.execute("p", "", start, end)
    return render_template('history.html',data=result, start=start, end=end)

@app.route("/zakup", methods=['POST'])
def zakup():
    nazwa = request.form['nazwa']
    ilosc = request.form['ilosc']
    cena = request.form['cena']
    m.assign("z", nazwa, ilosc, cena, "")
    #m.assign("e", "", "", "", "")
    return render_template("index.html")

@app.route('/magazyn')
def magazynForm():
    magazyn=m.execute("l","","","")

    konto2= m.execute("k","","","")

    return render_template('magazynForm.html', magazyn=magazyn, konto=konto2.saldo)

@app.route('/magazyn/<wybor>')
def magazynFormWybor(wyborRzeczy):
    magazyn = m.execute("m", wyborRzeczy, "", "")

    konto2= m.execute("k","","","")

    return render_template('magazynForm.html',wyborRzeczy=wyborRzeczy, magazyn=magazyn, konto=konto2.saldo)

@app.route("/sprzedarz", methods=['POST'])
def sprzedarz():
    nazwa = request.form['nazwa']
    ilosc = request.form['ilosc']

    m.assign("s", nazwa, ilosc, "","")

    #m.assign("e","","","","")
    return render_template("index.html")
@app.route("/konto", methods=['POST'])
def konto():
    ilosc = request.form['kwota']
    tryb = request.form.get('tryb')
    m.assign("k", "", ilosc,"", tryb)

    #m.assign("e","","","","")
    return  render_template("index.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        m = Manager()

    app.run(debug=True)  #to je