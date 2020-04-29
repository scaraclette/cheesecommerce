from flask import Flask, render_template, request, jsonify, Response

app = Flask(__name__)
app.config["DEBUG"] = True

storeApi = {
    "n":0,
    "code":None,
    "purchaseCount":0,
    "discountUsed":0,
}

'''
    APIs
'''
# The following method sets the nth interval and discount code as Admin
# API is called through JavaScript with example URL /admin/set?n=3&code=abc
@app.route("/admin/set", methods=['POST'])
def setAdmin():
    if request.method == 'POST':
        n = request.args.get('n', type=int)
        code = request.args.get('code', type=str)
        storeApi.update({'n':n})
        storeApi.update({'code':code})
        return jsonify({'msg':'created/updated'}), 201

    # When request is GET, return error
    return jsonify({'msg':'method not allowed'}), 405
    
# The following method returns the Admin report, report includes count of purchases and the total count of discounts that were given
# Only GET method is possible
@app.route('/admin/report')
def report():
    purchaseCount = storeApi.get('purchaseCount')
    discountUsed = storeApi.get('discountUsed')
    reportApi = {'Number of purchases made: ': purchaseCount, 'Amount of discount used: ':discountUsed}
    return jsonify(reportApi), 200

# The following method lets customers make purchase while automatically checks for discount
# an example url to call the api: /buy?name=scarlett
@app.route("/buy", methods=['GET', 'POST'])
def buy():
    if request.method == 'POST':
        currentPurchaseCount = storeApi.get('purchaseCount')
        nValue = storeApi.get('n')
        # If n is 0, first purchase will never have coupon
        if nValue == 0:
            storeApi.update({'purchaseCount':currentPurchaseCount+1})
            return jsonify({'msg':'purchase made, no coupon'}), 200     

        if nValue != 0 and currentPurchaseCount % nValue == 0:
            discountUsed = storeApi.get('discountUsed')
            storeApi.update({'purchaseCount':currentPurchaseCount+1})
            storeApi.update({'discountUsed':discountUsed+1})
            return jsonify({'msg':'purchase made, COUPON AVAILABLE!'}), 200 
        
        # By default, nth value is either 0 or it is not nth purchase
        storeApi.update({'purchaseCount':currentPurchaseCount+1})
        return jsonify({'msg':'purchase made, no coupon'}), 200 

    # if request is GET, return error
    return jsonify({'msg':'method not allowed'}), 405

    
# Route used using debugging program to check all data
@app.route("/check-api/")
def checkApi():
    return jsonify(storeApi)


'''
    METHODS FOR UI
'''
# Method that directs to index page
@app.route("/")
def index():
    return render_template("index.html")

# Method that directs to admin page
@app.route("/admin/")
def admin():
    return render_template("admin.html")
