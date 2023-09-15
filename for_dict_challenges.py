from collections import Counter

# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2
def exercise1():   
    print("Задание 1")
    students = [
        {'first_name': 'Вася'},
        {'first_name': 'Петя'},
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Петя'},
    ]
    names = [person['first_name'] for person in students]
    ctr = Counter(names)
    for name, count in ctr.items():
        print(f"{name}: {count}")


    # Задание 2
    # Дан список учеников, нужно вывести самое часто повторящееся имя
    # Пример вывода:
    # Самое частое имя среди учеников: Маша
def exercise2():
    print("Задание 2")
    students = [
        {'first_name': 'Вася'},
        {'first_name': 'Петя'},
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ]
    names = [person['first_name'] for person in students]
    ctr = Counter(names)
    print(f"Самое частое имя среди учеников: {ctr.most_common(1)[0][0]}")
            


    # Задание 3
    # Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
    # Пример вывода:
    # Самое частое имя в классе 1: Вася
    # Самое частое имя в классе 2: Маша
def exercise3():
    print("Задание 3")
    school_students = [
        [  # это – первый класс
            {'first_name': 'Вася'},
            {'first_name': 'Вася'},
        ],
        [  # это – второй класс
            {'first_name': 'Маша'},
            {'first_name': 'Маша'},
            {'first_name': 'Оля'},
        ],[  # это – третий класс
            {'first_name': 'Женя'},
            {'first_name': 'Петя'},
            {'first_name': 'Женя'},
            {'first_name': 'Саша'},
        ],
    ]
    for i in range(len(school_students)):
        names = [person['first_name'] for person in school_students[i]]
        ctr = Counter(names)
        print(f"Самое частое имя в классе {i + 1}: {ctr.most_common(1)[0][0]}")


    # Задание 4
    # Для каждого класса нужно вывести количество девочек и мальчиков в нём.
    # Пример вывода:
    # Класс 2a: девочки 2, мальчики 0 
    # Класс 2б: девочки 0, мальчики 2
def exercise4():
    print("Задание 4")
    school = [
        {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
        {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
        {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
    ]
    is_male = {
        'Олег': True,
        'Маша': False,
        'Оля': False,
        'Миша': True,
        'Даша': False,
    }
    for i in range(len(school)):
        girls = 0
        boys = 0
        for name in school[i]["students"]:
            if is_male[name['first_name']]:
                boys = boys + 1
            else: 
                girls = girls + 1
        class_number = school[i]["class"]
        print(f"Класс {class_number}: девочки {girls}, мальчики {boys}")

        


    # Задание 5
    # По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
    # Пример вывода:
    # Больше всего мальчиков в классе 3c
    # Больше всего девочек в классе 2a
def exercise5():
    print("Задание 5")
    school = [
        {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
        {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    ]
    is_male = {
        'Маша': False,
        'Оля': False,
        'Олег': True,
        'Миша': True,
    }
    number_male = 0
    number_female = 0
    for classes in school:
        female = [name['first_name'] for name in classes['students'] if not is_male[name['first_name']]]
        male = [name['first_name'] for name in classes['students'] if is_male[name['first_name']]]
        if len(female) > number_female:
           class_female = classes['class']
           number_female = len(female)
        if len(male) > number_male:
           class_male = classes['class']
           number_male = len(male)
    print(f"Больше всего мальчиков в классе {class_male}")       
    print(f"Больше всего девочек в классе {class_female}")

if __name__ == "__main__":
    exercise1()
    exercise2()
    exercise3()
    exercise4()
    exercise5()