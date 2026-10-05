from flask import Flask
app = Flask(__name__)
@app.route("/")

def home():
    return {"message": "Smart Task Manager Backend is Running! "}

@app.route("/tasks", methods=["GET"])   
def task():
    return {"message": "All task retrived sucessfully"}
if __name__ == "__main__":
    app.run (debug=True, port=5000)