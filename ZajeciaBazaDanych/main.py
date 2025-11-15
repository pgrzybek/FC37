from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_alembic import Alembic

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

alembic = Alembic()
alembic.init_app(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    firstname = db.Column(db.String(120), unique=False, nullable=False)
    lastname = db.Column(db.String(120), unique=False, nullable=False, server_default="")
    # user_type = db.Column(db.String(120), unique=False, nullable=False, server_default="", default="student")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

        #C - create
        me = User(
            username = "marwis1",
            email = "marwis1@gmail.com",
            firstname = "Marek"
        )

        # db.session.add(me)
        # db.session.commit()


        #R - read
        print(db.session.query(User).all())
        print(db.session.query(User).first().username)
        print(db.session.query(User).filter(User.username=="marwis95").all())
        print(db.session.query(User).filter(User.username=="marwis95").first())


        #U - uptade
        fromDb = db.session.query(User).filter(User.username=="marwis95").first()
        fromDb.lastname = "Wisniewski"
        db.session.add(fromDb)
        db.session.commit()


        #D - delete
        db.session.query(User).filter(User.username=="marwis1").delete()
        db.session.commit()


    app.run()


# pip freeze > requirements.txt
# pip install -r \requirements.txt
# flask --app main2 db revision initial
