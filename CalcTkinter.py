from tkinter import *

win = Tk()
win.geometry(f'400x470+100+200')
win['bg'] = 'black'
win.title('CalcV2.1')

def input_main(symbol): # добавление символов в основное поле
     main_windows.insert(END,symbol)

def symbol(symbol: str):

    if '=' not in temp_windows.get():

        temp_windows.insert(END, f'{ubrat_nol(main_windows.get())}{symbol}')
        main_windows.delete(0,END)

    else:
        x =temp_windows.get()
        x = x[x.find('=') +1 :]
        temp_windows.delete(0,END)

        temp_windows.insert(END, f'{x}{symbol}')



def ubrat_nol(num: str) -> str: # убирает лишнии нули после запятой, работает только с float
    x = str(float(num))
    return x[:-2] if x[-2:] == '.0' else x


def input_point(symbol): # вывод точки
    if '.' not in main_windows.get(): # если точки нет, то добавить
        main_windows.insert(END, symbol)

def clin(): # очистить все
    main_windows.delete(0,END)
    temp_windows.delete(0,END)
result = 0
def calc():
    temp_windows.insert(END,main_windows.get())
    main_windows.delete(0, END)
    expression = temp_windows.get()

    if '+' in expression:
        split_text = expression.split('+')
        result = float(split_text[0]) + float(split_text[1])
    elif'*' in expression:
        split_text = expression.split('*')
        result = float(split_text[0]) * float(split_text[1])
    if '/' in expression:
        split_text = expression.split('/')
        result = float(split_text[0]) / float(split_text[1])
    if '-' in expression:
        split_text = expression.split('-')
        result = float(split_text[0]) - float(split_text[1])

    temp_windows.insert(END,f'={ubrat_nol(result)}')






# основное окно
main_windows = Entry(win, width= 16, font=('',20))
main_windows.place(x = 80, y = 55)
temp_windows = Entry(win, width= 16, font=('',20))
temp_windows.place(x = 80, y = 20, )


# кнопочки
btn_1 = Button(win, bg = '#2a4858', fg = 'white', text = '1',font=('', 30), command = lambda : input_main('1'))
btn_1.place(x = 100, y = 150, width = 50, height= 50,  )
btn_2 = Button(win, bg = '#2a4858', fg = 'white', text = '2',font=('', 30), command = lambda : input_main('2'))
btn_2.place(x = 152, y = 150, width = 50, height= 50, )
btn_3 = Button(win, bg = '#2a4858', fg = 'white', text = '3',font=('', 30), command = lambda : input_main('3'))
btn_3.place(x = 204, y = 150, width = 50, height= 50, )
btn_4 = Button(win, bg = '#2a4858', fg = 'white', text = '4',font=('', 30), command = lambda : input_main('4'))
btn_4.place(x = 100, y = 202, width = 50, height= 50, )
btn_5 = Button(win, bg = '#2a4858', fg = 'white', text = '5',font=('', 30), command = lambda : input_main('5'))
btn_5.place(x = 152, y = 202, width = 50, height= 50, )
btn_6 = Button(win, bg = '#2a4858', fg = 'white', text = '6',font=('', 30), command = lambda : input_main('6'))
btn_6.place(x = 204, y = 202, width = 50, height= 50, )
btn_7 = Button(win, bg = '#2a4858', fg = 'white', text = '7',font=('', 30), command = lambda : input_main('7'))
btn_7.place(x = 100, y = 254, width = 50, height= 50, )
btn_8 = Button(win, bg = '#2a4858', fg = 'white', text = '8',font=('', 30), command = lambda : input_main('8'))
btn_8.place(x = 152, y = 254, width = 50, height= 50, )
btn_9 = Button(win, bg = '#2a4858', fg = 'white', text = '9',font=('', 30), command = lambda : input_main('9'))
btn_9.place(x = 204, y = 254, width = 50, height= 50, )
btn_0 = Button(win, bg = '#2a4858', fg = 'white', text = '0',font=('', 30), command = lambda : input_main('0'))
btn_0.place(x = 100, y = 306, width = 102, height= 50, )
btn_point = Button(win, bg = '#2a4858', fg = 'white', text = '.',font=('', 30), command = lambda : input_point('.'))
btn_point.place(x = 204, y = 306, width = 50, height= 50, )
btn_clear = Button(win, bg = '#2a4858', fg = 'white', text = 'CE',font=('', 20), command = lambda : clin())
btn_clear.place(x = 100, y = 98, width = 50, height= 50, )
btn_delenie = Button(win, bg = '#2a4858', fg = 'white', text = '/',font=('', 20), command = lambda : symbol('/'))
btn_delenie.place(x = 152, y = 98, width = 50, height= 50, )
btn_umnojit = Button(win, bg = '#2a4858', fg = 'white', text = 'x',font=('', 20), command = lambda : symbol('*'))
btn_umnojit.place(x = 204, y = 98, width = 50, height= 50, )
btn_dif = Button(win, bg = '#2a4858', fg = 'white', text = '-',font=('', 20), command = lambda : symbol('-'))
btn_dif.place(x = 256, y = 98, width = 50, height= 50, )
btn_sum = Button(win, bg = '#2a4858', fg = 'white', text = '+',font=('', 20), command = lambda : symbol('+'))
btn_sum.place(x = 256, y = 150, width = 50, height= 102, )
btn_calc = Button(win, bg = '#2a4858', fg = 'white', text = '=',font=('', 20), command = lambda : calc())
btn_calc.place(x = 256, y = 254, width = 50, height= 102, )



win.mainloop()
