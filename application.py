from flask import Flask, render_template, request, jsonify, Response

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


# APIs

# The following method sets the nth interval and discount code for all customers
# an example url to call the api: /admin/set?n=3&code=abc
@app.route("/admin/set", methods=['POST'])
def set():
    if request.method == 'POST':
        n = request.args.get('n', type=int)
        code = request.args.get('code', type=str)
        for names in storeApi:
            storeApi.get(i).update({'n':n})
            storeApi.get(i).update({'code':code})
        return jsonify({'msg':'created/updated'}), 201

    # When request is GET, return error
    return jsonify({'msg':'method not allowed'}), 405
    
# The following method returns the Admin report, report includes count of purchases and the total count of discounts that were given
# an example url to call the api: /admin/report?name=scarlett. Only GET method is possible
@app.route('/admin/report')
def report():
    name = request.args.get('name', type=str)
    if storeApi.get(name) is not None:
        purchaseCount = storeApi.get(name).get('n')
        discountUsed = storeApi.get(name).get('purchaseCount')
        reportApi = {'Number of purchases made: ': purchaseCount, 'Amount of discount used: ':discountUsed}
        return jsonify(reportApi), 200
    else:
        return jsonify({'msg':'user not found'}), 404

# The following method lets customers make purchase while automatically checks for discount
# an example url to call the api: /buy?name=scarlett
@app.route("/buy", methods=['GET', 'POST'])
def buy():
    if request.method == 'POST':
        # TODO: make purchase
        pass

    # if request is GET, return error
    return jsonify({'msg':'method not allowed'}), 405

    
# Route used using debugging program to check all current customers
@app.route("/check-api/")
def checkApi():
    return jsonify(storeApi)


'''
    METHODS FOR ACCESSING PAGES
'''

# index
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/admin/")
def admin():
    customerNames = []
    for names in storeApi:
        customerNames.append(names)
    return render_template("admin.html", names=customerNames)
