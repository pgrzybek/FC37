from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    my_list = [1,2,3,4,5]
    return render_template('index.html', my_list=my_list)

@app.route('/hello/<name>')
def hello(name):
    return render_template('index.html', name=name)
@app.route('/redirect/')
def redirect_test():
    return redirect(url_for ('hello ',name=' przekierowanie'))
@app.route('/myform/', methods=['GET', 'POST'])
def getData():
    print('Reading data')
   #print('imie ' +request.form['name'])
    print('imie ' + request.args['name'])
    #print('nazwisko ' + request.form['surname'])
    print('nazwisko ' + request.args['surname'])
    return 'Success'

if __name__ == '__main__':
    app.run()