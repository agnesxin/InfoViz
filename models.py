from run import db

class CompetitionRecord(db.Model):

    # create record table to store characters' position, and win or not in every combat 
    __tablename__ = "record"

    id = db.Column(db.Integer, primary_key=True)
    character = db.Column(db.String, nullable=False)
    position = db.Column(db.Integer, nullable=False)
    win = db.Column(db.Integer, nullable=False)

    def __init__(self, character, position, win):
        self.character = character
        self.position = position
        self.win = win

  