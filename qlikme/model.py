from qlikme import db

class Pet(db.Model):
    name = db.Column(db.String(25), primary_key=True)
    color = db.Column(db.String(25))
    pet = db.Column(db.String(25))

    def __init__(self, name, color, pet):
        self.name = name
        self.color = color
        self.pet = pet
