from dbInit import db


class KontoEncja(db.Model):
    __tablename__ = 'konto'
    id = db.Column(db.Integer, primary_key=True)
    saldo= db.Column(db.Integer, default=0)
    # produkt = db.relationship("Produkt", back_populates="konto", cascade="all, delete-orphan")

    def __repr__(self):
        return f"Konto(id={self.id}, saldo={self.saldo})"



