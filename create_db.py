from run import db
from models import CompetitionRecord

# create the database and the db tables
db.create_all()


def get_lines(f):
    for line in f:
        yield line

#insert data
f = open('game_data.txt', 'rU')    
for line in get_lines(f):
    tmp_ls = line.rstrip().split(',')
    # when team1 win
    if tmp_ls[10] == '1':
        for i in range(5):
            db.session.add(CompetitionRecord(tmp_ls[i], str(i),1))
        for i in range(5,10):
            db.session.add(CompetitionRecord(tmp_ls[i], str(i-5),0))
    # when team2 win
    elif tmp_ls[10] == '2':
        for i in range(5):
            db.session.add(CompetitionRecord(tmp_ls[i], str(i),0))
        for i in range(5,10):
            db.session.add(CompetitionRecord(tmp_ls[i], str(i-5),1))


    # commit the changes
    db.session.commit()



