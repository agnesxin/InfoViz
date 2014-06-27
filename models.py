from run import db

class CompetitionRecord(db.Model):

    __tablename__ = "record"

    id = db.Column(db.Integer, primary_key=True)
    character = db.Column(db.String, nullable=False)
    position = db.Column(db.Integer, nullable=False)
    win = db.Column(db.Integer, nullable=False)

    def __init__(self, character, position, win):
        self.character = character
        self.position = position
        self.win = win
#  
#     # print to test
#     def __repr__(self):
#         return '<{}-{}-{}'.format(self.character, self.position, self.win)

