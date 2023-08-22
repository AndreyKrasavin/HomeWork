import sqlite3 as sl

con = sl.connect("gb.db")
cur = con.cursor()

def show_data(): # показываем все записи таблицы users
    cur.execute("select * from users")
    for row in cur.fetchall():
        print(*row[1:])

def create_table():

#создаем пустую таблицу users со столбцами id, name, age если ее не было в БД

    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        numTel TEXT,
        mail TEXT
        
        
    )""")

    con.commit()
def add_into_empty():#если таблица пустая то добавляется 2 записи
    me = input('name? ')
    tel = input('numbers? ')
    mail = input('mail?')

    cur.execute("INSERT INTO users (name, numTel , mail) VALUES (?,?,?)",(me.capitalize(),tel,mail))
    con.commit()

def del_users():
    me = input('Кого удалить?')
    cur.execute(f"DELETE FROM users WHERE name='{me}'")
    print(f'>>> {me} <<<  вышел(а) из чата')
    con.commit()

def search_contact():
    x = input('Кого потерял?  ')
    x.capitalize()
    find = cur.execute(f"SELECT * FROM users WHERE name = '{x}'")
    print(find)


while True:
    print("""Что сделаем ? 
1. Посмотреть контакты ?
2. Добавить контакт ?
3. Удалить контакт ?
4. Найти контакт ?
5. Выйти? """)
    answer = input('>>>')
    if answer == '2':
        add_into_empty()
    elif answer == '3':
        del_users()
    elif answer == '4':
        search_contact()
    elif answer == '1':
        show_data()
    elif answer == '5':
        break


# create_table()

print('Вышли')
