from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'Hello World from Flask!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)