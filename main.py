from math import ceil
import tkinter as tk


def check_int(*args):
    """Проверка на то, состоит ли стркоа только из чисел

    :param args: проверяемые числа
    :type args: str
    :return: True, если строка состоит только из чисел.
        Иначе False
    """
    try:
        for i in args:
            int(i)
        return True
    except ValueError:
        return False


def check_pos(*args):
    """Проверка координат

    Если координата не пренадлежит отрезку [1;8],
    то ее не может быть на шахматной доске.
    :param args: кортеж из двух координат
    :type args: tuple(int, int)
    :return: True, если оба числа находятся в промежутке.
        Иначе - False
    """
    nums = range(1, 9)
    for i in args:
        if i in nums:
            return True
        else:
            return False


def variable_cells(x, y):
    """Поиск возможных ходов коня

    Находит все возможные ходы из заданной позиции
    :param x: позиция по горизонтали
    :param y: позиция по вертикали
    :type x: int
    :type y: int
    :return: Кортеж с вложенными кортежами в каждом из которых пара координат
    """

    "наверное можно попробовать оптимизировать как то"
    variable = list()

    variable.append((x + 2, y + 1))
    variable.append((x + 1, y + 2))
    variable.append((x - 2, y - 1))
    variable.append((x - 1, y - 2))

    variable.append((x + 2, y - 1))
    variable.append((x - 1, y + 2))
    variable.append((x - 2, y + 1))
    variable.append((x + 1, y - 2))

    variable_2 = variable.copy()

    for i in variable:
        if not check_pos(*i):
            variable_2.remove(i)

    return variable_2


def turns_num(pos1, pos2):
    """

    :param pos1:
    :param pos2:
    :return:
    """

    answer = variable_cells(*pos1)
    k = 1

    while True:
        new_answer = answer.copy()
        if pos2 in new_answer:
            return k

        answer = []

        for i in new_answer:
            z = variable_cells(*i)
            for x in z:
                answer.append(x)

        k += 1


def press(x, y, pressed_cells, btns, output):
    """Выбирает клетку на доске

    Вызывается, когда пользователь нажимает на клетку.
    Клетка подсвечивается и
    добавляется в массив с выбранными клетками pressed_cells.

    :param x: Координата клетки по x
    :param y: Координата клетки по y
    :type x: int
    :type x: int
    :param pressed_cells: Массив с выбранными на данный момент клетками
    :param pressed_cells: list
    :param btns: Массив со всеми клетками доски
    :type btns: list
    :param output: Label в котором пишется вывод для пользователя
    :type output: tk.Label
    """

    if len(pressed_cells) < 2:
        pressed_cells.append((x, y))

    else:
        last_x, last_y = pressed_cells[0]
        if (last_x + last_y) % 2:
            clr = "#FFDAB9"
        else:
            clr = "#800000"
        btns[8 - last_x][last_y].configure(bg=clr)
        btns[8 - last_x][last_y].pack()
        pressed_cells[0] = pressed_cells[1]
        pressed_cells[1] = (x, y)

    btns[8 - x][y].configure(bg="#778899")
    btns[8 - x][y].pack()
    output.configure(bg="LightGreen", text=f"Вы выбрали клетку {x} {y + 1}")
    output.pack()


def task_func(pressed_cells, output, option):
    """Основная функция

    Если option == True, то выполняется первое задание -
    поиск количества ходов между двумя клетками
    Иначе - поиск количества ходов, чтобы два коня встретились
    :param pressed_cells: Массив с выбранными на данный момент клетками
    :param pressed_cells: list
    :param output: Label в котором пишется вывод для пользователя
    :type output: tk.Label
    :param option: Если True, то выполняется первое задание. Иначе - второе.
    :type option: bool
    """
    if len(pressed_cells) != 2:
        output.configure(bg="pink", text=f"Сначала выберите две клетки!")
        output.pack()
        return
    k = turns_num(pressed_cells[0], pressed_cells[1])
    if option is True:
        output.configure(bg="LightGreen", text=f"Чтобы попасть в клетку {pressed_cells[1]} необходимо: {k} ходов")
    else:
        output.configure(bg="LightGreen", text=f"Чтобы кони встретились необходимо: {ceil(k / 2)} ходов")
    output.pack()


def create_window():
    """Фронтенд

    Создается шахматная доска, кнопки для выполнения заданий.
    """
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    pressed_cells = list()

    root = tk.Tk()

    choice_buttons = tk.Frame(master=root)

    task1 = tk.Button(
        master=choice_buttons, text="Количество ходов до клетки",
        command=lambda opt=True: task_func(pressed_cells, output, opt)
    )
    task2 = tk.Button(
        master=choice_buttons, text="Через сколько ходов встретятся кони",
        command=lambda opt=False: task_func(pressed_cells, output, opt)
    )

    output = tk.Label(
        master=choice_buttons, bg='LightGreen',
        text="Для начала выберите две клетки, а потом нажмите на одну из кнопку слева", width=60
    )

    task1.pack(side='left')
    task2.pack(side='left')
    output.pack(side='left')

    choice_buttons.pack()

    board = tk.Frame(master=root)
    btns = list()

    for y in range(1, 9):
        lines = list()
        line = tk.Frame(master=board)
        tk.Label(master=line, bg='#C0C0C0', width=5, height=2, text=str(9 - y)).pack(side='left')

        for x in range(1, 9):
            if (y + x) % 2:
                color = "#FFDAB9"
            else:
                color = "#800000"

            lines.append(tk.Button(
                master=line, width=5, height=2, bg=color,
                command=lambda p1=9-y, p2=x - 1: press(p1, p2, pressed_cells, btns, output)
            ))

            lines[-1].pack(side="left")

        btns.append(lines)
        line.pack(side="top")

    let = tk.Frame(master=board)
    tk.Label(master=let, width=5, height=2).pack(side='left')
    for i in letters:
        tk.Label(master=let, bg='#C0C0C0', width=5, height=2, text=i).pack(side='left', ipadx=2)
    let.pack()

    board.pack()

    root.mainloop()


if __name__ == '__main__':
    create_window()
print("******-*******")