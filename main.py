
def check_int(*verifiable):
    try:
        for i in verifiable:
            int(i)
        return True
    except ValueError:
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
        if not(8 >= i[0] >= 1) or not(8 >= i[1] >= 1):
            variable_2.remove(i)

    return variable_2


def meeting():
    pass

def turns_num():
    start = input("Стартовая позиция коня: ").split()
    end = input("Конечная позиция коня: ").split()
    start = tuple(map(int, start))
    end = tuple(map(int, end))
    answer = variable_cells(*start)
    
    new_answer = list()
    flag = True
    k = 1

    while flag:
        new_answer = answer.copy()
        if end in new_answer:
            print(f"Чтобы попасть в клетку {end} необходимов {k} ходов")
            flag = False

        answer = []

        for i in new_answer:
            z = variable_cells(*i)
            for x in z:
                answer.append(x)

        k += 1


def main():
    menu_commands = (
        ("Выход", exit),
        ("Количество ходов до клетки", turns_num),
        ("Через сколько ходов встретятся кони", meeting)
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
        menu_commands[int(choice)][1]()



main()