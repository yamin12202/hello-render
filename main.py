from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, world from Render!"  # You can change this message

if __name__ == "__main__":
    app.run()
