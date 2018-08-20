from robot_project import db


class Robot(db.Model):

    __tablename__ = 'robots'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    owner = db.relationship('Owner', backref='robot', uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f"Robot Id {self.id} with name {self.name} and owner {self.owner.name}"
        return f"Robot Id {self.id} with name {self.name} with no owner yet"
