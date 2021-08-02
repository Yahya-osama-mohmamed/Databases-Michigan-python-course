import sqlite3
conn=sqlite3.connect("emaildb.sqlite")
cur=conn.cursor()
cur.execute('DROP TABLE IF EXISTS Counts')
fname=input('Enter File Name')

cur.execute('CREATE TABLE Counts(org TEXT, count INTEGER)')
if len(fname)<1: 

    fname= 'a.txt'
fh=open(fname)
for line in fh:
    if line.startswith ('From: '):
        word=line.split()
        y=word[1]
        x=y.split('@')
        email=x[1]
        cur.execute('SELECT*FROM Counts WHERE org=?',(email,))
        row = cur.fetchone()
        if row is None:
            cur.execute('INSERT INTO Counts (org,count) VALUES (?,1)',(email,))
        else:
            cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?',(email,))   
        
    conn.commit()         

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()