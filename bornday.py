year_of_born = int(input('Введите год рождения А.С Пушкина:  '))

if year_of_born == 1799:
    day_of_born = input('А теперь введите его день рождения: ')
    if day_of_born.lower() == '6 июня':
        print('Верно')
    else:
        print('Неверный день рождения')
else:
    print('Неверный год рождения')
