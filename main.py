#Метод Ньютона.
def newtons_method():
    pass

#Метод хорд.
def chord_method():
    pass

#Метод биссекций.
def bissection_method():
    pass

def main():
    operating = True
    print('=============Численное решение нелинейных уравнений=============')

    while operating:
        print('Выберите способ решения уравнения, выбрав соответствующее число.')
        print('Метод бисекций - 1.')
        print('Метод хорд - 2.')
        print('Метод Ньютона - 3.')
        print('Для выхода введите exit.')

        guess_choice = input()

        if (guess_choice == 'exit'):
            operating = False
        else:
            try:
                guess_choice = int(guess_choice)
            except ValueError:
                print('Введено некорректное значение. Попробуйте снова!\n')
                continue

            if (guess_choice == 1):
                bissection_method()
            elif (guess_choice == 2):
                chord_method()
            elif (guess_choice == 3):
                newtons_method()
            else:
                print('Введено некорректное значение. Попробуйте снова!\n')
                continue

if __name__ == '__main__':
    main()