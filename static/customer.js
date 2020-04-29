document.addEventListener('DOMContentLoaded', () => {

    // getCoupon function is called to updated whether customer has coupon during visiting page
    getCoupon();

    document.getElementById("buyMore").onclick = () => {
        const buyRequest = new XMLHttpRequest();
        buyRequest.open('POST', '/customer/buy');
        buyRequest.onload = () => {
            // after customer makes purchase, getCoupon is updated to show whether next purchase has code
            getCoupon();
            const data = JSON.parse(buyRequest.responseText);
            alert(JSON.stringify(data));
        }

        let applied = false;
        if (document.getElementById("applyCoupon").checked) {
            applied = true;
        }        
        let buyData = JSON.stringify({'applyCoupon':applied})
        buyRequest.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
        buyRequest.send(buyData);
    }

});


// function to call GET method from getDiscount route
function getCoupon() {
    const couponRequest = new XMLHttpRequest();
    couponRequest.open('GET', '/customer/get-discount');
    couponRequest.onload = () => {
        const data = JSON.parse(couponRequest.responseText);
        document.getElementById("hasCoupon").innerHTML = JSON.stringify(data);

    }
    couponRequest.send();
}