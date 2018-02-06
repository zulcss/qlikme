from qlikme import db
from qlikme.model import Pet

def insert(name, color, pet):
    db.create_all()
    pet = Pet(name, color, pet)
    db.session.add(pet)
    db.session.commit()
