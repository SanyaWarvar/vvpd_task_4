from math import ceil


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
        if (args[0] and args[1]) in nums:
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


if __name__ == '__main__':
    main()
    