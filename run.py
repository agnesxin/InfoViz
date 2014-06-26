# -*- coding: utf-8 -*-

import sqlite3 
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing


app = Flask(__name__)

app.config.update(dict(
    DATABASE='./db/game_record.db',
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)




def connect_db():
    return sqlite3.connect(app.config['DATABASE'])
# 
# def init_db():
#     with closing(connect_db()) as db:
#         with app.open_resource('schema.sql') as f:
#             db.cursor().executescript(f.read())
#         db.commit()


@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    g.db.close()

@app.route('/')
def show_entries():
    cur = g.db.execute('select Id, Character, Position, Win from Record')
    char_info = {}
    for row in cur.fetchall():   
        if row[1] not in char_info:
            # po0, po1, po2, po3, po4, show, win
            char_info[row[1]] = [0, 0, 0, 0, 0, 1, row[3]]
            # add one on the position if win
            char_info[row[1]][row[2]] += row[3]
        else:
            # show time plus one
            char_info[row[1]][5] += 1
            # win number plus one if win
            char_info[row[1]][6] += row[3]
            # position win number plus one if win
            char_info[row[1]][row[2]] += row[3]
    
    entries = [dict(character=char, po0=char_info[char][0],po1=char_info[char][1], po2=char_info[char][2], po3=char_info[char][3], po4=char_info[char][4], show=char_info[char][5], win_perc=float(char_info[char][6])/float(char_info[char][5])) for char in char_info]
    entries = sorted(entries, key=lambda k: k['win_perc'], reverse = True) 
    return render_template('show_heros.html', entries=entries)



if __name__ == '__main__':
    app.debug = app.config['DEBUG']
    app.run()   


