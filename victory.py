# Программа викторина:  Года рождения знаменитых людей

# Альберт Эйнштейн:  1879
# Леонардо ДиКаприо:  1974
# Лев Толстой:  1828
# А.П.Чехов:  1860
# Юрий Гагарин:  1934
# Владимир Высоцкий:  1938

famous_people = {'Альберт Эйнштейн': 1879, 'Леонардо ДиКаприо': 1974, 'Лев Толстой': 1828,
                 'А.П.Чехов': 1860, 'Юрий Гагарин': 1934, 'Владимир Высоцкий': 1938}

again = True

while again:
    score = 0
    print('\nВведите год рождения знаменитости: ')
    for i in famous_people:
        answer = int(input(i + ' : '))
        if answer == famous_people[i]:
            score += 1

    errors = len(famous_people) - score

    print(f'\nКоличество правильных ответов:  {score}')
    print(f"Количество ошибок:  {errors}")
    print(f"Процент правильных ответов:  {score / len(famous_people) * 100:.2f}%")
    print(f"Процент неправильных ответов:  {errors / len(famous_people) * 100:.2f}%\n")

    again_answer = input('Начать игру сначала? (Да/Нет):  ')

    if again_answer.lower() == 'нет':
        again = False
