def main():
    try:
        a = int(input('Введите A: '))
        b = int(input('Введите B: '))
        x = int(input('Введите X: '))
        if x <= 4:
            y = (a ** 2) / (x ** 2) + (6 * x)
        else:
            y = b ** 2 * ((4 + x) ** 2)
        print("y = %.1f" % y)
    except ValueError:
        print("Неверные входные данные!")
    except:
        print("Нет решения!")
    input("Нажмите Enter для выхода")
if __name__ == '__main__':
    main()