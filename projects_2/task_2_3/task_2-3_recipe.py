name_medium = input("Введите название питательной среды:")
name_medium_big = name_medium.upper()
agar_concentration = input("Введите концентрацию агара:")
sterilization_tempreture = input("Введите температуру стерилизации:")
with open("C:/Users/Оля/Documents/komrakova_as/projects_2/task_2_3/recipe.txt", "w", encoding="utf-8") as card:
    card.write(f"НАЗВАНИЕ СРЕДЫ: {name_medium_big}\n")
    card.write(f"\tКонцентрация агара:\t{agar_concentration}%\n")
    card.write(f"\tТемпература стерилизации:\t{sterilization_tempreture}К\n")
print("Файл 'recipe.txt' успешно сформирован!")
