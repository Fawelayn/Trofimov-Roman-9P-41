temperature = int(input("Введите температуру\n"))
is_rainy = input("Есть ли осадки?(да/нет)\n").lower()
if is_rainy == "да":
    is_rainy_heavly = input("Сильный дождь?(да/нет)\n").lower()
if 20 < temperature < 30:
    if is_rainy == "да":
        print("Наденьте футболку, шорты и дожевик")
    else:
        print("Наденьте футболку и шорты")
else:
    if temperature > 0:
        if is_rainy == "да":
            if is_rainy_heavly == "да":
                print("Наденьте пальто, резиновые сапоги и возьмите зонт")
            else:
                print("Наденьте пальто и дождевик")
        else:
            print("Наденьте пальто")
    else:
        print("Наденьте пуховик")