def exercise1():
    # Вывести последнюю букву в слове
    print("Вывести последнюю букву в слове")
    word = 'Архангельск'
    print(f"{word[-1]}")

def exercise2():
    # Вывести количество букв "а" в слове
    print("Вывести количество букв а в слове")
    word = 'Архангельск'
    print(word.lower().count('а'))

def exercise3():
    # Вывести количество гласных букв в слове
    print("Вывести количество гласных букв в слове")
    word = 'Архангельск'
    letters = "аеёиоуыэюя"
    number = 0
    for letter in word.lower():
        if letter in letters:
            number = number + 1
    print(number)

def exercise4():
    # Вывести количество слов в предложении
    print("Вывести количество слов в предложении")
    sentence = 'Мы приехали в гости'
    sentence_list =sentence.split()
    print(len(sentence_list))

def exercise5():
    # Вывести первую букву каждого слова на отдельной строке
    print("Вывести первую букву каждого слова на отдельной строке")
    sentence = 'Мы приехали в гости'
    sentence_list =sentence.split()
    for word in sentence_list:
        print(word[0])        

def exercise6():
    # Вывести усреднённую длину слова в предложении
    print("Вывести усреднённую длину слова в предложении")
    sentence = 'Мы приехали в гости'
    sentence_list =sentence.split()
    words_len = 0
    for word in sentence_list:
        words_len = words_len + len(word)
    print(words_len/len(sentence_list))

if __name__ == "__main__":
    exercise1()
    exercise2()
    exercise3()
    exercise4()
    exercise5()
    exercise6()