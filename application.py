from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.config["DEBUG"] = True

# Initial application has two customers
storeApi = [
    {"scarlett": [
        {"n":3},
        {"code":"ABC"},
        {"purchaseCount":7},
        {"discountUsed":2}
    ]},
    {"adrian": [
        {"n":None},
        {"code":None},
        {"purchaseCount":0},
        {"discountUsed":0}
    ]}
]

# index
@app.route("/")
def index():
    return render_template("index.html")

# APIs



# Route used using debugging program to check all current customers
@app.route("/check-api/")
def checkApi():
    return jsonify(storeApi)

# TODO delete later
@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    return jsonify({'sum': data['a'] + data['b']})