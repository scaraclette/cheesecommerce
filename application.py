from flask import Flask, render_template, request, jsonify, Response

app = Flask(__name__)
app.config["DEBUG"] = True

storeApi = {
    'n':0,
    'code':None,
    'purchaseCount':0,
    'discountUsed':0,
}

'''
    APIs
'''
# The following method sets the nth interval and discount code as Admin
# POST /admin/set
# request body {
#    'n': <nth interval> <int>,
#    'code': <discount code> <string>
# }
#
# response body: {
#   'msg': <message> <string>
# }
# status 201
# status 405
@app.route("/admin/set", methods=['POST'])
def setAdmin():
    if request.method == 'POST':
        data = request.get_json()
        n = data['n']
        code = data['code']

        storeApi.update({'n':int(n)})
        storeApi.update({'code':code})
        return jsonify({'msg':'created/updated'}), 201

    # When request is GET, return error
    return jsonify({'msg':'method not allowed'}), 405
    
# The following method returns the Admin report, report includes count of purchases and the total count of discounts that were given
# GET /admin/report
# response body {
#   'Number of purchases made: ' : <purchaseCount> <int>,
#   'Amount of discount used: ' : <discountUsed> <int>
# }
# status 200
@app.route('/admin/report')
def report():
    purchaseCount = storeApi.get('purchaseCount')
    discountUsed = storeApi.get('discountUsed')
    reportApi = {'Number of purchases made: ': purchaseCount, 'Amount of discount used: ':discountUsed}
    return jsonify(reportApi), 200

# The following method lets customers make purchase while automatically checks for discount
# POST /customer/buy
# request body {
#   'applyCoupon' : <applied> <boolean>
# }
# response body {
#   'msg' : <message> <string>
# }
# status 200
# status 405
@app.route("/customer/buy", methods=['POST'])
def buy():
    if request.method == 'POST':
        # Check if coupon was applied
        data = request.get_json()
        applied = data['applyCoupon']

        # Customer makes purchase which increments count
        incrementPurchase()

        # Call hasCoupon method to check if there is discount
        purchaseCount = storeApi.get('purchaseCount')
        if hasCoupon(purchaseCount, applied):
            incrementDiscount()
            return jsonify({'msg': 'purchase made, COUPON USED'}), 200
        
        # By default coupon is not available
        return jsonify({'msg': 'purchase made'}), 200

    # if request is GET, return error
    return jsonify({'msg':'method not allowed'}), 405

# The following method returns a JSON object of whether or not customer has discount
# GET /customer/get-discount
# response body {
#   'msg' : <message> <string>
# }
# status 200
# status 404
@app.route("/customer/get-discount")
def getDiscount():
    # Call hasCoupon method to check if there is discount
    purchaseCount = storeApi.get('purchaseCount')
    if hasCoupon(purchaseCount + 1, True):
        return jsonify({'msg':'discount available','code':storeApi.get('code')}), 200
    
    return jsonify({'msg':'no discount available'}), 404
    

'''
    HELPER METHODS
'''
# Helper method to increment purchase
def incrementPurchase():
    currentPurchaseCount = storeApi.get('purchaseCount')+1
    storeApi.update({'purchaseCount':currentPurchaseCount})

# Helper method to increment discount
def incrementDiscount():
    discountUsed = storeApi.get('discountUsed')+1
    storeApi.update({'discountUsed':discountUsed})

# Helper method to determin whether purhcase has coupon, returns boolean
def hasCoupon(purchaseCount, applied):
    n = storeApi.get('n')
    if n == 0 or applied == False:
        return False
    if purchaseCount % n == 0:
        return True    
    return False
    
# Route used using debugging program to check all data
@app.route("/check-api/")
def checkApi():
    return jsonify(storeApi)


'''
    METHODS FOR UI
'''
# Method that directs to index page
@app.route("/customer/")
def index():
    return render_template("customer.html")

# Method that directs to admin page
@app.route("/admin/")
def admin():
    return render_template("admin.html")
