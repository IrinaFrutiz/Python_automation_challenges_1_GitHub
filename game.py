import random

word_list = ["человек", "слово", "лицо", "дверь", "земля", "работа", "ребенок", "история", "женщина", "развитие",
             "власть", "правительство", "начальник", "спектакль", "автомобиль", "экономика", "литература", "граница",
             "магазин", "председатель", "сотрудник", "республика", "личность"]
tries = 6
guessed_letters = []  # список уже названных букв
guessed_words = []  # список уже названных слов


def get_word():
    # print("генератор слова")
    word = random.choice(word_list)
    # print(word)
    return word


def display_hangman(attempts):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        # голова, торс, обе руки, одна нога
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        # голова, торс, обе руки
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        # голова, торс и одна рука
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        # голова и торс
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        # голова
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        # начальное состояние
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    print(stages[attempts])
    return stages[attempts]


def play(word, word_completion, attempts):
    print('Давайте играть в угадайку слов!')
    guessed = False
    display_hangman(attempts)
    print("Количество попыток: ", attempts)
    if len(guessed_letters) > 0 or len(guessed_words) > 0:
        print("Cписок неверных значений:", *guessed_letters, *guessed_words)
    print(*word_completion, sep='')
    word_or_letter = input()
    if word_or_letter.isalpha():
        if len(word_or_letter) == 1:
            if word_or_letter in word:
                for i in range(len(word)):
                    if word_or_letter == word[i]:
                        word_completion[i] = word_or_letter
                return if_guessed(word, word_completion, attempts, guessed)
            else:
                if word_or_letter in guessed_letters:
                    print("Этой буквы всё ещё нет в слове")
                else:
                    print("Этой буквы нет в слове")
                    guessed_letters.append(word_or_letter)
                    attempts -= 1
                return if_guessed(word, word_completion, attempts, guessed)
        else:
            if word_or_letter == word:
                guessed = True
                return if_guessed(word, word_completion, attempts, guessed)
            else:
                guessed_words.append(word_or_letter)
                attempts -= 1
                print("Попробуй ещё разок")
                return if_guessed(word, word_completion, attempts, guessed)
    else:
        print("ВВЕДИ БУКВУ")
        play(word, word_completion, attempts)


def if_guessed(word, word_completion, attempts, guessed):
    wyw = ""
    for i in word_completion:
        wyw += i
    print(wyw)
    if guessed or wyw == word:
        print('Поздравляем, вы угадали слово! Вы победили!')
    elif attempts == 0:
        print("Игра окончена. Слово", word)
    else:
        return play(word, word_completion, attempts)
    guessed_letters.clear()
    guessed_words.clear()
    return if_again(), guessed_words, guessed_letters


def if_again():
    again = int(input("Хочешь сыграть ещё разок? Да - нажми не 0, Нет - нажми 0  "))
    if again:
        game_body()
    else:
        print("Увидимся позже!")


def game_body():
    word = get_word()
    word_completion = ['_'] * len(word)
    play(word, word_completion, tries)


game_body()
