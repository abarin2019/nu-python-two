correct_answer = False

while not correct_answer:
    year_of_born = int(input("\nВведите год рождения А.С Пушкина:  "))

    if year_of_born == 1799:
        correct_answer = True
        print('Верно')
    else:
        print('Неверно')
