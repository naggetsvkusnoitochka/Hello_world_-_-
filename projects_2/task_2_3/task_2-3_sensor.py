name_operator = input("Введите имя оператора:")
pressure_sensor = input("Введите значение датчика давление:")
with open("C:/Users/Оля/Documents/komrakova_as/projects_2/task_2_3/sensor_log.txt", "w", encoding="utf-8") as card:
    card.write(f"ОПЕРАТОР:\tЗНАЧЕНИЕ:\n{name_operator}\t{pressure_sensor} Па")
print("Данные успешно сохранены в sensor_log.txt")
    