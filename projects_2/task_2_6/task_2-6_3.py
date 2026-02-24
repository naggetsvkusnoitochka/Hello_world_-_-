phenotype_donor = input("Введите группу крови донора:").upper()
phenotype_patient = input("Введите группу крови пациента:").upper()
if phenotype_donor == "I" and (phenotype_patient == "I" or phenotype_patient == "II" or phenotype_patient == "III" or phenotype_patient == "IV"):
   print(f"Возможно переливание пациенту с {phenotype_patient} группой крови.")
elif phenotype_donor == "II":
    if phenotype_patient == "II" or phenotype_patient == "IV":
        print(f"Возможно переливание пациенту с {phenotype_patient} группой крови.")
    else:
        print(f"Невозможно переливание пациенту с {phenotype_patient} группой крови.")
elif phenotype_donor == "III":
    if phenotype_patient == "III" or phenotype_patient == "IV":
        print(f"Возможно переливание пациенту с {phenotype_patient} группой крови.")
    else:
        print(f"Невозможно переливание пациенту с {phenotype_patient} группой крови.")
elif phenotype_donor == "IV":
    if phenotype_patient == "IV":
        print(f"Возможно переливание пациенту с {phenotype_patient} группой крови.")
    else:
        print(f"Невозможно переливание пациенту с {phenotype_patient} группой крови.")
else:
   print("Таких групп крови не существует, переливание невозможно.")