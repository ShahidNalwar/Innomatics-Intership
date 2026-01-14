from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    name = request.args.get("name", "Guest")
    name_upper = name.upper()

    return f"""
    <h1>HELLO {name_upper} 👋</h1>
    <p>Welcome to the Flask Playground 🚀</p>
    <p>Try these:</p>
    <ul>
        <li><b>/reverse?name=yourname</b></li>
        <li><b>/length?name=yourname</b></li>
        <li><b>/time</b></li>
    </ul>
    """

# BONUS 1: Reverse the name
@app.route("/reverse")
def reverse_name():
    name = request.args.get("name", "Guest")
    return f"<h2>Reversed Name 🔄 : {name[::-1]}</h2>"

# BONUS 2: Length of the name
@app.route("/length")
def name_length():
    name = request.args.get("name", "Guest")
    return f"<h2>Length of your name 📏 : {len(name)}</h2>"

# BONUS 3: Current Server Time
@app.route("/time")
def current_time():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"<h2>Current Server Time ⏰ : {now}</h2>"

if __name__ == "__main__":
    app.run(debug=True)
