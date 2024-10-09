import os
import openai
from flask import Flask, request, jsonify

# Забираем ключ из переменной окружения
openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)

@app.route('/diagnose', methods=['POST'])
def diagnose():
    data = request.json
    symptoms = data.get('symptoms', '')

    # Формирование запроса для OpenAI
    prompt = f"I have the following symptoms: {symptoms}. What might be the diagnosis?"

    response = openai.Completion.create(
        engine="text-davinci-003",  # Используй нужную модель OpenAI
        prompt=prompt,
        max_tokens=100
    )

    diagnosis = response.choices[0].text.strip()

    return jsonify({"diagnosis": diagnosis})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)