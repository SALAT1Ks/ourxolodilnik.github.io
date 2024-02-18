from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return open('index.html').read()

@app.route('/start_countdown', methods=['POST'])
def start_countdown():
    user_input = request.form['userInput'] # Получаем значение из поля ввода
    print("Данные получены на сервере:", user_input) # Выводим полученные данные на сервере
    return "Данные успешно получены на сервере"

if __name__ == '__main__':
    app.run(debug=True)
