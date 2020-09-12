import sqlite3



filelist = ('information.docx','hello.txt','myimage.png',\
                'myMovie.mpg','world.txt','data.pdf','myphoto.jpg')

    
connect = sqlite3.connect('example.db')
c = connect.cursor()

with connect:
    c.execute("CREATE TABLE IF NOT EXISTS tbl_ReadTable(\
            ID INTEGER PRIMARY KEY AUTOINCREMENT , \
            col_String TEXT \
            )")
    connect.commit()
connect.close()



conn = sqlite3.connect('example.db')

with conn:
    cursor = conn.cursor()
    for e in filelist:
        if e.endswith('.txt'):
                store = e
                print(store)
                cursor.execute('INSERT INTO tbl_ReadTable (col_String) VALUES (?)',
                         (e,))
                conn.commit()
conn.close()



conn = sqlite3.connect('example.db')

with conn:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tbl_ReadTable')
    results = cursor.fetchall()
    print(results)
conn.close()



        
    
