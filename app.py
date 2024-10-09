# База данных симптомов и диагнозов в формате словаря
symptoms_db = {
    "headache": ["migraine", "tension headache", "cluster headache"],
    "fever": ["flu", "infection", "covid-19"],
    "foot pain": ["arthritis", "sprain", "gout"],
    "swollen foot": ["sprain", "venous thrombosis", "infection"],
    "numbness in toes": ["nerve compression", "diabetes", "circulatory problems"]
}

# Функция для получения возможных диагнозов по симптомам
def get_possible_diagnoses(symptoms):
    possible_diagnoses = []
    for symptom in symptoms:
        if symptom in symptoms_db:
            possible_diagnoses.extend(symptoms_db[symptom])
    return list(set(possible_diagnoses))

# Получаем ввод от пользователя
user_input = input("Enter your symptoms separated by commas: ")
user_symptoms = [symptom.strip().lower() for symptom in user_input.split(",")]

# Получаем возможные диагнозы
diagnoses = get_possible_diagnoses(user_symptoms)

# Выводим результаты
if diagnoses:
    print(f"Possible diagnoses: {', '.join(diagnoses)}")
else:
    print("No diagnoses found for the given symptoms.")
