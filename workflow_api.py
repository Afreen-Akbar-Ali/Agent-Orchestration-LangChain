from flask import Flask, request, jsonify, render_template

from workflow_agents import run_workflow

app = Flask(__name__)

# -----------------------------
# HOME PAGE
# -----------------------------

@app.route("/")

def home():

    return render_template("index.html")


# -----------------------------
# API ROUTE
# -----------------------------

@app.route("/process", methods=["POST"])

def process():

    data = request.get_json()

    topic = data.get("topic")

    result = run_workflow(topic)

    return jsonify(result)


# -----------------------------
# RUN SERVER
# -----------------------------

if __name__ == "__main__":

    app.run(debug=True)