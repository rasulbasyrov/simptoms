import numpy as np
from flask import Flask, request, jsonify, render_template
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

app = Flask(__name__)

# Пример данных для обучения (симптомы и диагнозы)
X = np.array([[1, 0, 0],  # Headache
              [0, 1, 0],  # Fever
              [0, 0, 1],  # Foot pain
              [1, 1, 0],  # Headache + Fever
              [0, 1, 1],  # Fever + Foot pain
              [1, 0, 1]]) # Headache + Foot pain
y = np.array([0, 1, 2, 0, 1, 2])  # Диагнозы: 0 - Migraine, 1 - Flu, 2 - Arthritis

# Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Обучение модели (RandomForest)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Словарь для отображения диагноза
diagnosis_map = {0: "Migraine", 1: "Flu", 2: "Arthritis"}

# Функция для преобразования симптомов в бинарные признаки
def symptoms_to_features(symptoms):
    feature_map = ["headache", "fever", "foot pain"]
    features = np.zeros(len(feature_map))
    for symptom in symptoms:
        if symptom in feature_map:
            features[feature_map.index(symptom)] = 1
    return features

@app.route('/')
def home():
    return render_template('chat.html')

# Маршрут для диагностики
@app.route('/diagnose', methods=['POST'])
def diagnose():
    data = request.json
    symptoms = data.get('symptoms', '').split(',')
    symptoms = [symptom.strip().lower() for symptom in symptoms]
    
    # Преобразование симптомов в признаки
    features = symptoms_to_features(symptoms)
    
    # Предсказание диагноза
    predicted = model.predict([features])[0]
    diagnosis = diagnosis_map[predicted]
    
    return jsonify({"diagnosis": diagnosis})

if __name__ == '__main__':
    app.run(debug=True)
