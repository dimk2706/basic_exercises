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
    students_2 =[]
    for student in students:
        if (student in students_2) == False:
            name_count = students.count(student)
            name = student["first_name"]
            print(f"{name}: {name_count}")
            students_2.append(student)


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
    name_count = 0
    students_3 = []
    for student in students:
        if (student in students_3) == False and students.count(student) > name_count:
            name = student["first_name"]
            name_count = students.count(student)
            students_3.append(student)
    print(f"Самое частое имя среди учеников: {name}")
            


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
        name_count = 0
        students_4 = []
        for student in school_students[i]:
            if (student in students_4) == False and school_students[i].count(student) > name_count:
                name = student["first_name"]
                name_count = school_students[i].count(student)
                students_4.append(student)
        print(f"Самое частое имя в классе {i + 1}: {name}")


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
    boys_max = 0
    girls_max = 0
    for i in range(len(school)):
        girls = 0
        boys = 0
        for name in school[i]["students"]:
            if is_male[name['first_name']]:
                boys = boys + 1
            else: 
                girls = girls + 1
        if boys > boys_max:
            class_boys = school[i]["class"]
        if girls > girls_max:
            class_girls = school[i]["class"]
    print(f"Больше всего мальчиков в классе {class_boys}")
    print(f"Больше всего девочек в классе {class_girls}")

if __name__ == "__main__":
    exercise1()
    exercise2()
    exercise3()
    exercise4()
    exercise5()