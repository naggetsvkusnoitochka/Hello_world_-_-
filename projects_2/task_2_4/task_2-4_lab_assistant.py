volume = float(input("Введите объем раствора:"))
salt_mass = volume * 0.009
total_volume = volume
with open("C:/Users/Оля/Documents/komrakova_as/projects_2/task_2_4/recipe.txt", "w", encoding = "utf-8") as file:
    file.write("ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ\n")
    file.write("-" * 25)
    file.write(f"\nОбщий объем:\t{total_volume} мл\nМасса соли:\t{salt_mass:.2f} г\nОбъем воды:\t{volume} мл")
