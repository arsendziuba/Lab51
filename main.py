# Определение функции для расчета дней в году на заданной планете
def calculate_days_in_year(orbital_radius, orbital_speed):
    # Рассчитываем дни в году на основе орбитальных параметров планеты
    days_in_year = 2 * 3.14159265359 * orbital_radius / orbital_speed
    return days_in_year

# Определение функции для определения, на какой планете год длится дольше
def compare_planet_years(days1, days2):
    if days1 > days2:
        return "Первая планета имеет более длинный год."
    elif days2 > days1:
        return "Вторая планета имеет более длинный год."
    else:
        return "Обе планеты имеют одинаковую длительность года."

if __name__ == "__main__":
    # Получаем ввод от пользователя для названий планет и орбитальных параметров
    planet1 = input("Введите название первой планеты: ")
    planet2 = input("Введите название второй планеты: ")
    orbital_radius = float(input("Введите орбитальный радиус: "))
    orbital_speed = float(input("Введите орбитальную скорость: "))

    # Рассчитываем дни в году для обеих планет
    days1 = calculate_days_in_year(orbital_radius, orbital_speed)
    days2 = calculate_days_in_year(orbital_radius, orbital_speed)

    # Сравниваем длительность годов на планетах
    result = compare_planet_years(days1, days2)
    print(result)
