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

# The following method sets the nth interval and discount code
# an example url to call the api: /admin/set?name=scarlett&n=3&code=abc
@app.route("/admin/set", methods=['POST'])
def set():
    name = request.args.get('name', type=str)
    nInterval = request.args.get('n', type=int)
    code = request.args.get('code', type=str)
    
    
    



# Route used using debugging program to check all current customers
@app.route("/check-api/")
def checkApi():
    return jsonify(storeApi)
