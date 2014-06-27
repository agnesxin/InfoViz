# -*- coding: utf-8 -*-

# import sqlite3 
from flask import Flask,render_template
from flask.ext.sqlalchemy import SQLAlchemy
from models import *


app = Flask(__name__)

# connect to the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/game_record.db'

# create the sqlalchemy object
db = SQLAlchemy(app)




@app.route('/')
def show_entries():
    records = db.session.query(CompetitionRecord).all()
    
    # store the character information in a dictionary
    # char_info[char] = [po0: xx, po1: xx, po2: xx, po3: xx, po4: xx, show: xx, win: xx]
    
    char_info = {}
    for r in records:   
        if r.character not in char_info:
            # po0, po1, po2, po3, po4, show, win
            char_info[r.character] = [0, 0, 0, 0, 0, 1, r.win]
            # add one on the position if win
            char_info[r.character][r.position] += r.win
        else:
            # show time plus one
            char_info[r.character][5] += 1
            # win number plus one if win
            char_info[r.character][6] += r.win
            # position win number plus one if win
            char_info[r.character][r.position] += r.win
    
    # store in a list of dictionary for pushing
    entries = [dict(character=char, po0=char_info[char][0],po1=char_info[char][1], po2=char_info[char][2], po3=char_info[char][3], po4=char_info[char][4], show=char_info[char][5], win_perc=float(char_info[char][6])/float(char_info[char][5])) for char in char_info]
    
    # sort it in the order of winning percentage
    entries = sorted(entries, key=lambda k: k['win_perc'], reverse = True) 
    return render_template('show_heros.html', entries=entries)


if __name__ == '__main__':
    app.run()   

