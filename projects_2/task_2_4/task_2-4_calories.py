protein = float(input("Введите массу белков в продукте (г):"))
lipid = float(input("Введите массу жиров в продукте (г):"))
carbohydrate = float(input("Введите массу углеводов в продукте (г):"))
KAL = protein * 4 + lipid * 9 + carbohydrate * 4
print(f"Общая каллорийность продукта = {KAL} калл")
