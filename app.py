from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'NOBODYBOTz'


if __name__ == "__main__":
    app.run()
