from dbInit import db



class Operacje(db.Model):
    __tablename__ = "operacje"

    id = db.Column(db.Integer, primary_key=True)
    typ = db.Column(db.String(50), nullable=False)   # np. "kupno" / "sprzedaż"

    # dane produktu w momencie operacji (kopie)
    nazwa = db.Column(db.String(100))
    cena = db.Column(db.Integer)
    ilosc = db.Column(db.Integer)

    # przedmiot_id = db.Column(db.Integer, db.ForeignKey("przedmiot.id"),nullable=False)
    # przedmiot=db.relationship("Przedmiot",back_populates="operacje")
    #produkt_id = db.Column(db.Integer, db.ForeignKey("produkt.id"), nullable=True)
    #produkt = db.relationship("Produkt", back_populates="operacje")
    #
    # def __repr__(self):
    #     return f"<Operacja id={self.id} typ={self.typ} Produkt={self.produkt.nazwa}>"