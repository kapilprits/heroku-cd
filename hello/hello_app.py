from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "World, I love continuous delivery a lot using heroku!"

if __name__ == "__main__":
    app.run()
