from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>DevOps Pipeline Success!</h1><p>The Python App is running on the Docker Node.</p>"

if __name__ == "__main__":
    # host='0.0.0.0' is REQUIRED for Docker to let outside traffic in
    app.run(host='0.0.0.0', port=8080)
