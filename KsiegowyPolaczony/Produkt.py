from dbInit import db


class Produkt(db.Model):
    __tablename__ = 'produkt'

    id = db.Column(db.Integer, primary_key=True)
    nazwa = db.Column(db.String(100), nullable=False)
    cena = db.Column(db.Float, nullable=False)
    ilosc = db.Column(db.Integer, default=1)

    # konto_id = db.Column(db.Integer, db.ForeignKey("konto.id"), nullable=False)
    # konto = db.relationship("KontoEncja", back_populates="produkt")
    operacje = db.relationship("Operacje", back_populates="produkt", cascade="all")




