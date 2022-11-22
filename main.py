from math import ceil
import tkinter as tk



def check_int(*verifiable):
    try:
        for i in verifiable:
            int(i)
        return True
    except ValueError:
        return False


def check_pos(*args):

    nums = range(1, 9)
    for i in args:
        if i in nums:
            return True
        else:
            return False


def variable_cells(x, y):
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


def enter_position(option):
    if option == 1:
        start = input("Стартовая позиция коня: ").split()
        end = input("Конечная позиция коня: ").split()
    else:
        start = input("Позиция первого коня: ").split()
        end = input("Позиция второго коня: ").split()

    if not check_int(*start, *end) and check_pos(start, end) and len(start) == 2 and len(end) == 2:
        print("Неверные координаты!")
        return

    start = tuple(map(int, start))
    end = tuple(map(int, end))

    ans = turns_num(start, end)

    if option == 1:
        print(f"Чтобы попасть в клетку {end} коню необходимо {ans} ходов")
    else:
        print(f"Кони встретятся через {ceil(ans/2)} ходов")


def turns_num(pos1, pos2):

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


def main():
    menu_commands = (
        ("Выход", exit),
        ("Количество ходов до клетки", enter_position),
        ("Через сколько ходов встретятся кони", enter_position)
    )
    s = ""
    for n, v in enumerate(menu_commands):
        s += f"{n} = {v[0]}\n"
    while True:
        print("-" * 50)
        choice = input(f"{s}Введите номер команды: ")
        if not check_int(choice) or not(len(menu_commands) > int(choice) > -1):
            print("Неверный ввод!")
            continue
        print("-" * 50)
        menu_commands[int(choice)][1](int(choice))


def create_window():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    def press(x, y):
        if len(pressed_cells) < 2:
            pressed_cells.append((x, y))

        else:

            last_x, last_y = pressed_cells[0]
            if (last_x + last_y) % 2:
                color = "#FFDAB9"
            else:
                color = "#800000"
            btns[8 - last_x][last_y].configure(bg=color)
            btns[8 - last_x][last_y].pack()
            pressed_cells[0] = pressed_cells[1]
            pressed_cells[1] = (x, y)

        btns[8 - x][y].configure(bg="#778899")
        btns[8 - x][y].pack()
        output.configure(bg="LightGreen", text=f"Вы выбрали клетку {x} {y + 1}")
        output.pack()

    def task1_func():
        if len(pressed_cells) != 2:
            output.configure(bg="pink", text=f"Сначала выберите две клетки!")
            output.pack()
            return
        k = turns_num(pressed_cells[0], pressed_cells[1])
        output.configure(bg="LightGreen", text=f"Чтобы попасть в клетку {pressed_cells[1]} необходимо: {k} ходов")
        output.pack()

    def task2_func():
        if len(pressed_cells) != 2:
            output.configure(bg="pink", text=f"Сначала выберите две клетки!")
            output.pack()
            return
        k = turns_num(pressed_cells[0], pressed_cells[1])
        output.configure(bg="LightGreen", text=f"Чтобы кони встретились необходимо: {ceil(k/2)} ходов")
        output.pack()


    pressed_cells = list()

    root = tk.Tk()

    choice_buttons = tk.Frame(master=root)

    task1 = tk.Button(master=choice_buttons, text="Количество ходов до клетки", command=lambda : task1_func())
    task2 = tk.Button(master=choice_buttons, text="Через сколько ходов встретятся кони", command=lambda : task2_func())
    output = tk.Label(master=choice_buttons, bg='LightGreen', text="Для начала выберите две клетки, а потом нажмите на одну из кнопку слева", width=60)

    task1.pack(side='left')
    task2.pack(side='left')
    output.pack(side='left')

    choice_buttons.pack()

    board = tk.Frame(master=root)
    btns = list()
    for x in range(1, 9):
        lines = list()
        line = tk.Frame(master=board)
        tk.Label(master=line, bg='#C0C0C0', width=5, height=2, text=str(9 - x)).pack(side='left')

        for y in range(1, 9):
            if (x + y) % 2:
                color = "#FFDAB9"
            else:
                color = "#800000"

            lines.append(tk.Button(master=line, width=5, height=2, bg=color, command=lambda p1=9-x, p2=y - 1: press(p1, p2)))

            lines[-1].pack(side="left")

        btns.append(lines)
        line.pack(side="top")







    board.pack()




    root.mainloop()


if __name__ == '__main__':
    create_window()
