from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>DevOps Pipeline Success!</h1><p>The Python App is running on the Docker Node.</p>'

if __name__ == "__main__":
    # It MUST be 0.0.0.0 to be accessible outside the container
    app.run(host='0.0.0.0', port=8080)
