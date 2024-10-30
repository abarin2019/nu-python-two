correct_year = False
correct_day = False

while not correct_year:
    year_of_born = int(input('\nВведите год рождения А.С Пушкина:  '))

    if year_of_born == 1799:
        correct_year = True
        while not correct_day:
            day_of_born = input('А теперь введите его день рождения: ')
            if day_of_born.lower() == '6 июня':
                correct_day = True
                print('Верно')
            else:
                print('Неверный день рождения\n')
    else:
        print('Неверный год рождения')
