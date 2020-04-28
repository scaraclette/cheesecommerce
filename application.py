from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.config["DEBUG"] = True

# Initial application has two customers
storeApi = {
    "scarlett": {
        "n":3,
        "code":"ABC",
        "purchaseCount":7,
        "discountUsed":2
    },
    "adrian": {
        "n":0,
        "code":None,
        "purchaseCount":0,
        "discountUsed":2,
    }
}

# index
@app.route("/")
def index():
    return render_template("index.html")

# APIs

# The following method sets the nth interval and discount code
# an example url to call the api: /admin/set?name=scarlett&n=3&code=abc
@app.route("/admin/set", methods=['POST'])
def set():
    if request.method == 'post':
        name = request.args.get('name', type=str)
        n = request.args.get('n', type=int)
        code = request.args.get('code', type=str)
        # if customer exists, updates data from dictionary, else create new customer
        if storeApi.get(name) is not None:
            storeApi.get(name).update({'n':n})
            storeApi.get(name).update({'code':code})
        else:
            newCustomer = {
                'n' : n,
                'purchases' : 0,
                'code' : code,
                'discountUsed': 0, 
            }
            # Appends to dictionary
            storeApi.update({name:newCustomer})

        return jsonify({'msg':'created/updated'}), 201

    # When request is GET
    return jsonify({'msg':'invalid method'}), 404
    
    
    



# Route used using debugging program to check all current customers
@app.route("/check-api/")
def checkApi():
    return jsonify(storeApi)
