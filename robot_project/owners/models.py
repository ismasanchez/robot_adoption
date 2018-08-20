from robot_project import db


class Owner(db.Model):

    __tablename__ = 'owners'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    robot_id = db.Column(db.Integer, db.ForeignKey('robots.id'))

    def __init__(self, name, robot_id):
        self.name = name
        self.robot_id = robot_id

    def __repr__(self):
        return f"Owner name: {self.name}"
