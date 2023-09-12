def main():
    # Вывести последнюю букву в слове
    print("Вывести последнюю букву в слове")
    word = 'Архангельск'
    print(f"{word[-1]}")


    # Вывести количество букв "а" в слове
    print("Вывести количество букв а в слове")
    word = 'Архангельск'
    number =word.count("А") + word.count("а")
    print(number)


    # Вывести количество гласных букв в слове
    print("Вывести количество гласных букв в слове")
    word = 'Архангельск'
    letters = ["А","а","е", "Е", "ё", "Ё", "и", "И", "о", "О", "у", "У", "ы", "Ы", "э", "Э", "ю", "Ю", "я", "Я"]
    number = 0
    for letter in word:
        if letter in letters:
            number = number + 1
    print(number)


    # Вывести количество слов в предложении
    print("Вывести количество слов в предложении")
    sentence = 'Мы приехали в гости'
    sentence_list =sentence.split()
    print(len(sentence_list))


    # Вывести первую букву каждого слова на отдельной строке
    print("Вывести первую букву каждого слова на отдельной строке")
    sentence = 'Мы приехали в гости'
    sentence_list =sentence.split()
    for word in sentence_list:
        print(word[0])        


    # Вывести усреднённую длину слова в предложении
    print("Вывести усреднённую длину слова в предложении")
    sentence = 'Мы приехали в гости'
    sentence_list =sentence.split()
    words_len = 0
    for word in sentence_list:
        words_len = words_len + len(word)
    print(words_len/len(sentence_list))

if __name__ == "__main__":
    main()