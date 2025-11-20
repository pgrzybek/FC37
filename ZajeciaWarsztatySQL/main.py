from flask import Flask, render_template, request
from werkzeug.utils import redirect
from flask_sqlalchemy import SQLAlchemy


from Car import Car

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cars.db'
db = SQLAlchemy(app)

car_list = []


class CarDb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mark = db.Column(db.String(50), unique=False, nullable=False)
    model = db.Column(db.String(50), unique=False, nullable=False)
    year = db.Column(db.Integer, unique=False, nullable=False)


@app.route('/')
def main_page():
    car_list.clear()
    for car in db.session.query(CarDb).all():
        car_list.append(Car(car.mark, car.model, car.year))

    return render_template("index.html", car_list=car_list, size=len(car_list))

@app.route('/myform', methods = ["POST"])
def get_data():
    print("Reading data from 'myform'")
    print("form_mark: " + request.form["form_mark"])
    print("form_model: " + request.form["form_model"])
    print("form_year: " + request.form["form_year"])

    # car_list.append(Car(request.form["form_mark"], request.form["form_model"], request.form["form_year"]))

    car = CarDb(mark=request.form["form_mark"],
                model=request.form["form_model"],
                year=request.form["form_year"]
        )

    db.session.add(car)
    db.session.commit()

    return redirect("http://127.0.0.1:5000")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        db.session.commit()
    app.run()
