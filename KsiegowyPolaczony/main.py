from flask import Flask, render_template, request

from Manager import Manager

app = Flask(__name__)
m=Manager()
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/home")
def home2():
    return render_template("index.html")
@app.route("/history/")
def history():
    operacje=m.operacje
    return render_template('history.html',data=operacje)

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
    values = list(magazyn.values())
    konto2= m.execute("k","","","")

    return render_template('magazynForm.html', magazyn=values, konto=konto2)

@app.route("/sprzedarz", methods=['POST'])
def sprzedarz():
    nazwa = request.form['nazwa']
    ilosc = request.form['ilosc']
    cena = request.form['cena']
    m.assign("s", nazwa, ilosc, cena, "")

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
    app.run(debug=True)  #to je