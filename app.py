from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Im Ibrahim trying to update!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
