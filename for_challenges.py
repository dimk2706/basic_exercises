

def main():
# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки

    names = ['Оля', 'Петя', 'Вася', 'Маша']
    for name in names:
        print(name)


# Задание 2
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём
# Пример вывода:
# Оля: 3
# Петя: 4

    names = ['Оля', 'Петя', 'Вася', 'Маша']
    for i in range(len(names)):
        print(f"{names[i]}: {i + 1}")



# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика

    is_male = {
        'Оля': False,  # если False, то пол женский
        'Петя': True,  # если True, то пол мужской
        'Вася': True,
        'Маша': False,
    }
    names = ['Оля', 'Петя', 'Вася', 'Маша']
    for i in range(len(names)):
        if is_male[names[i]]:
            gender = "Мужской"
        else:
            gender = "Женский"
        print(f"{names[i]}: {gender}")


# Задание 4
# Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# Группа 1: 2 ученика.
# Группа 2: 4 ученика.

    groups = [
        ['Вася', 'Маша'],
        ['Вася', 'Маша', 'Саша', 'Женя'],
        ['Оля', 'Петя', 'Гриша'],
    ]
    print(f"Всего {len(groups)} группы")
    for i in range(len(groups)):
        print(f"Группа {i + 1}: {len(groups[i])} ученика.")


# Задание 5
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят
# Пример вывода:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша

    groups = [
        ['Вася', 'Маша'],
        ['Оля', 'Петя', 'Гриша'],
        ['Вася', 'Маша', 'Саша', 'Женя'],
    ]
    for i in range(len(groups)):
        names = ", ".join(groups[i])
        print(f"Группа {i + 1}: {names}")



if __name__ == "__main__":
    main()