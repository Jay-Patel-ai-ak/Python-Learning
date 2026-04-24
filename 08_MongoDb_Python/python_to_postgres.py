import psycopg2
import psycopg2.extras

hostname = '127.0.0.1'
database = 'Cars'
username = 'postgres'
pwd = 'Master@0510'
port_id = 5432
conn = None
cur = None
try:
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id
    )
    
    cur = conn.cursor (cursor_factory=psycopg2.extras.DictCursor)
    
    create_script = ''' CREATE TABLE IF NOT EXISTS BIKES (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        price FLOAT NOT NULL
    )'''
    
    cur.execute(create_script)
    
    insert_script = ''' INSERT INTO BIKES (name, price) VALUES (%s, %s) '''
    data = [
        ('Yamaha R1', 15000),
        ('Ducati Panigale V4', 25000),
        ('Kawasaki Ninja H2', 30000)
    ]
    for record in data:
        print(record)
    cur.executemany(insert_script, data) 
    
    update_script = ''' UPDATE BIKES SET price = price * 1.1 WHERE name = %s '''
    cur.execute(update_script, ('Yamaha R1',))
    
    delete_script = ''' DELETE FROM BIKES WHERE name = %s '''
    cur.execute(delete_script, ('Kawasaki Ninja H2',))
    
    # Whenever you are using context manager, use WITH Clause to fetch data from the database.
    
    cur.execute('SELECT * FROM BIKES')
    # for record in cur.fetchall():
       # print(record[name], record[price])
        
    conn.commit()
    
    
except Exception as error:
    print(error)
finally: 
    if conn is not None:
        conn.close()
    if cur is not None:
        cur.close() 