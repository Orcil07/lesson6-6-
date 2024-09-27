my_dict = {"Лавкрафт": "Рлаейех", "Кинг": "Лад",
           "Пратчетт": "Анк-Морпорк"}
print(my_dict)
print(my_dict["Кинг"])
my_dict["Пратчетт"] = "Агатовая империя"
print(my_dict)
my_dict["Линдгрен"] = "Нангияла"
print(my_dict)
my_dict["Герберт"] = "Каладан"
print(my_dict)
my_dict.pop("Лавкрафт")
print(my_dict)
a = my_dict.pop("Пратчетт")
print(a)
print(my_dict)
my_set = {4,5,6,6,5,4,"Долина Терновника", (7,9)}
print(my_set.discard(6))
print(my_set)
