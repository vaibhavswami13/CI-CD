from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
<<<<<<< HEAD
    return "DevOps CI/CD Working Successfully!!, test1test28"
=======
    return "DevOps CI/CD Working Successfully!!, test1test25"
>>>>>>> refs/remotes/origin/main

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

