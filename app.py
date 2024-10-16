import os
import openai
from flask import Flask, request, jsonify, render_template
from flask_babel import Babel, _, get_locale

app = Flask(__name__)

# Настройка Flask-Babel для мультиязычности
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'ru', 'tr']
babel = Babel(app)

@babel.localeselector
def get_locale():
    # Выбираем язык из параметра запроса, либо используем английский по умолчанию
    return request.args.get('lang', 'en')

# Устанавливаем API-ключ OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

# Маршрут для главной страницы с чатом
@app.route('/')
def home():
    return render_template('chat.html')

# Маршрут для диагностики симптомов
@app.route('/diagnose', methods=['POST'])
def diagnose():
    data = request.json
    symptoms = data.get('symptoms', '')

    # Формирование запроса для OpenAI на выбранном языке
    prompt = _("I have the following symptoms: {}. What might be the diagnosis?").format(symptoms)

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )

    diagnosis = response.choices[0].text.strip()

    return jsonify({"diagnosis": diagnosis})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)