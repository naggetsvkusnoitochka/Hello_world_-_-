name_researcher = input("Введите ФИО:")
date =  input("Введите дату эксперимента:")
experiment = input("Введите название экперимента:")
conclusion = input("Напишите вывод к эксперименту:")
with open("C:/Users/Оля/Documents/komrakova_as/projects_2/task_2_3/journal.txt", "w", encoding="utf-8") as journal:
    journal.write("+-------------------------------------------------------+\n")
    journal.write("|\tЭлектронный лабораторный журнал\t\t\t|\n")
    journal.write("+-------------------------------------------------------+\n")
    journal.write(f"|ФИО исследователя\t:\t{name_researcher}\t\t|\n")
    journal.write(f"|Дата\t\t\t:\t{date}\t\t|\n")
    journal.write(f"|Название эксперимента\t:\t{experiment}\t|\n")
    journal.write("+-------------------------------------------------------+\n")
    journal.write(f"|Вывод\t\t\t:\t{conclusion}\t\t|\n")
    journal.write("+-------------------------------------------------------+\n")



    

