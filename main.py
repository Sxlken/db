import psycopg2
import csv

conn= psycopg2.connect(host = 'localhost',
                        database = 'postgres2',
                        user = 'postgres'
                        password = '1234',
                        )
cur = conn.cursor()
cur.execute('SELECT superhero.name FROM superhero.superhero LIMIT 5;')

with open('csv2.csv', 'w', newline='', encoding='utf-8') as csvfile:  
    csvwriter = csv.writer(csvfile)  
    csvwriter.writerows(results)  
  
  
  
cur.close()  
conn.close()

usernames = [r[0] for r in cur.fetchall()]
# found = False
# while not Found:
#    username = input('введите ваш логин:')
#   if username in usernames:
#       print('вы есть в списке')
#       Found=True
#        else:
#       print('мы не смогли вас найти')

'''' создать функцию бинарного поиска вхождения параметка в список usernames'''
def binary_search(username):
     # если есть в списке 
     return True
     # если нету в списке
     return False
      
conn.commit()
cur.close()
conn.close()