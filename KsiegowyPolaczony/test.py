from app import app
from dbInit import db
from KontoEncja import KontoEncja

with app.app_context():
    print("Baza istnieje?", db.engine.url)
    print("Tabele:", db.engine.table_names())

    konto = db.session.get(KontoEncja, 1)
    print("Konto ID=1:", konto)

    if konto is None:
        konto = KontoEncja(saldo=1000)
        db.session.add(konto)
        db.session.commit()
        print("Utworzono nowe konto.")

    print("Po operacji:", db.session.get(KontoEncja, 1))