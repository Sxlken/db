import psycopg2

conn= psycopg2.connect(host = 'localhost',
                        database = 'practice2',
                        user = 'postgres',
                        password = '123')
cur = conn.cursor()
cur.execute('SELECT superhero.name FROM superhero.superhero LIMIT 5;')
usernames = [r[0] for r in cur.fetchall()]
found = False
while not Found:
    username = input('введите ваш логин:')
    if username in usernames:
        print('вы есть в списке')
        Found=True
else:
        print('мы не смогли вас найти')

def binary_search(user):
     return True
     return False
      
conn.commit()
cur.close()
conn.close()