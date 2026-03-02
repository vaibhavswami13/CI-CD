from flask import Flask
from demo import demo
app = Flask(__name__)

@app.route("/")
def home():
    return (demo())

    return "DevOps CI/CD Working Successfully!!, test1test28"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

    #app1.py

    def demo():
        return"welcome to demo!"
