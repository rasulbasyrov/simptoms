from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# База данных симптомов и диагнозов
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

# Маршрут для главной страницы с чатом
@app.route('/')
def home():
    return render_template('chat.html')

# Маршрут для приема POST-запросов с симптомами
@app.route('/diagnose', methods=['POST'])
def diagnose():
    data = request.json
    symptoms = data.get('symptoms', '').split(',')
    symptoms = [symptom.strip() for symptom in symptoms]
    diagnoses = get_possible_diagnoses(symptoms)
    return jsonify(diagnoses)

# Запуск приложения
if __name__ == '__main__':
    app.run(debug=True)