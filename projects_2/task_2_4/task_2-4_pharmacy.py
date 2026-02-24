quantity_capsules = int(input("Введите количество произведенных капсул:"))
capacity = int(input("Введите количество капсул в одной упаковке:"))
full_packaging = quantity_capsules // capacity
remains =  quantity_capsules % capacity
print("--- Отчет фасоночного цеха ---")
print(f"Полных упаковок:\t{full_packaging}\nОстаток капсул:\t{remains}")