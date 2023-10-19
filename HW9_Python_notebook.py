import sqlite3 as sl

con = sl.connect("BAZA.db")
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

#create_table()
def repeat(me):
    x = cur.execute(f"select name from users where name = '{me}'")

def add_into_empty():
    me = input('name? ')
    while True:
        me = me.capitalize()
        x = cur.execute(f"select name from users where name = '{me}'")
        if x.fetchall() == []:
            break
        else:
            x = cur.execute(f"select name from users where name = '{me}'")
            s = x.fetchall()
            if me in s[0][0] :
                q = cur.execute(f"select * from users where name = '{me}'")
                print(f"Такой контакт уже есть {q.fetchall()}")
                me = input('Введи другое имя? >>>')

    tel = input('numbers? ')
    while True:
        if len(tel) == 11 and tel[0] == '8':
            break
        elif tel == '':
            tel = 'Номера телефона нет'
            print(tel)
            break
        else:
            print('ERROR')
            tel = input('Номер с восьмеркой и 11 цифр')
    mail = input('mail?')




    cur.execute("INSERT INTO users (name, numTel , mail) VALUES (?,?,?)",(me.capitalize(),tel,mail))
    print(f'Добавили {me} ')
    con.commit()

def del_users():
    me = input('Кого удалить?')
    x = cur.execute(f"DELETE FROM users WHERE name='{me.capitalize()}'")
    x = x.fetchall()
    if x == []:
        print('Такого контакта нет')
    else:
        print(f'>>> {me} <<<  вышел(а) из чата')
    con.commit()

def search_contact():
    x = input('Кого потерял?  ')
    x.capitalize()
    find = cur.execute(f"SELECT * FROM users WHERE name = '{x}'")
    print(find)


while True:
    create_table()
    x = cur.execute("select * from users")
    print("""Что сделаем ? 
1. Посмотреть контакты ?
2. Добавить контакт ?
3. Удалить контакт ?
4. Найти контакт ?
5. Выйти? """)
    print(f"Контактов в записной книжке {len(x.fetchall())}")
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




print('Вышли')
