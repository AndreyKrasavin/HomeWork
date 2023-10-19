import sqlite3 as sl


con = sl.connect("BAZA.db")
cur = con.cursor()


def show_data():  # показываем все записи таблицы users
    cur.execute("select * from users")
    for row in cur.fetchall():
        print(*row[1:])


def create_table():
    # создаем пустую таблицу  со столбцами id, notes, если ее не было в БД

    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Notes TEXT,
        


    )""")

    con.commit()


# create_table()
def repeat(me):
    x = cur.execute(f"select Notes from users where Notes = '{me}'")


def add_into_empty():
    me = input('Заметка? ')
    while True:
        me = me.capitalize()
        x = cur.execute(f"select Notes from users where Notes = '{me}'")
        if x.fetchall() == []:
            break
        else:
            x = cur.execute(f"select Notes from users where Notes = '{me}'")
            s = x.fetchall()
            if me in s[0][0]:
                q = cur.execute(f"select * from Notes where Notes = '{me}'")
                print(f"Такая заметка уже есть {q.fetchall()}")
                me = input('Введи другую заметку >>>')



    cur.execute("INSERT INTO Notes (Notes) VALUES (?)", (me.capitalize(),))
    print(f'Добавили {me} ')
    con.commit()


def del_users():
    me = input('Какую заметку удалить?')
    x = cur.execute(f"DELETE FROM users WHERE Notes='{me.capitalize()}'")
    x = x.fetchall()
    if x == []:
        print('Такого контакта нет')
    else:
        print(f'>>> {me} <<<  вышел(а) из чата')
    con.commit()


def search_contact():
    x = input('Кого потерял?  ')
    x.capitalize()
    find = cur.execute(f"SELECT * FROM users WHERE Notes = '{x}'")
    print(find)


while True:
    x = cur.execute("select * from users")
    print("""Что сделаем ? 
1. Посмотреть заметки ?
2. Добавить заметки ?
3. Удалить заметки ?
4. Найти заметки ?
5. Выйти? """)
    print(f"заметок всего {len(x.fetchall())}")
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
