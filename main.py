from flask import Flask  # ✅ Correct import

app = Flask(__name__)    # ✅ Correct usage

@app.route("/")
def home():
    return "Hello, Render!"

if __name__ == "__main__":
    app.run()

app=flask(__name__)
@app.route('/')
def hello():
    return"hello,world from render!"