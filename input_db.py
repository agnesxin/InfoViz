import sqlite3 as sqlite
import sys

# connect to a database
con = sqlite.connect('game_record.db')


cur = con.cursor()
# create Record table
cur.execute("DROP TABLE IF EXISTS Record")
cur.execute("CREATE TABLE Record(Id INT, Character TEXT, Position INT, Win INT)")



def create_db(path):
    f = open(path, 'rU')    
    count = 0
    for line in f:
        tmp_ls = line.rstrip().split(',')
        # when team1 win
        if tmp_ls[10] == '1':
            for i in range(5):
                count += 1
                cur.execute('INSERT INTO Record VALUES('+str(count)+',"'+tmp_ls[i]+'",'+str(i)+',1)')
            for i in range(5,10):
                count += 1
                cur.execute('INSERT INTO Record VALUES('+str(count)+',"'+tmp_ls[i]+'",'+str(i-5)+',0)')
        # when team2 win
        elif tmp_ls[10] == '2':
            for i in range(5):
                count += 1
                cur.execute('INSERT INTO Record VALUES('+str(count)+',"'+tmp_ls[i]+'",'+str(i)+',0)')
            for i in range(5,10):
                count += 1
                cur.execute('INSERT INTO Record VALUES('+str(count)+',"'+tmp_ls[i]+'",'+str(i-5)+',1)')
        # print out bad records
        else:
            print "Bad Record: "+temp_ls

    con.commit()
    con.close()        







create_db('game_data.txt')